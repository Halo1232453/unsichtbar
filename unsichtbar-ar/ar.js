/* Unsichtbar · AR-Effekte
   Baut pro Station: Scan-Effekt, Video, Karten mit Linien, 3D-Objekt, Partikel und Quiz.
   Texte, Positionen und Zeiten stehen in index.html unter "Einstellungen". */
(() => {
const T = AFRAME.THREE;
const DEMO = new URLSearchParams(location.search).has('demo');
const COL = { paper: '#f6f4ef', ink: '#141414', grey: '#78766f', line: '#d7d4cd', acc: '#be3c28' };
const FONT = 'Inter, -apple-system, "Helvetica Neue", Roboto, Arial, sans-serif';
const POSTER_H = 1.4145;

// ---------- Kleine Animations-Engine ----------
const EASE = {
  linear: k => k,
  outCubic: k => 1 - Math.pow(1 - k, 3),
  inCubic: k => k * k * k,
  inOutCubic: k => k < 0.5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2,
  outBack: k => 1 + 2.4 * Math.pow(k - 1, 3) + 1.4 * Math.pow(k - 1, 2),
};
let tweens = [];
let now = 0;
const lerp = (a, b, k) => a + (b - a) * k;
const clamp01 = k => Math.max(0, Math.min(1, k));
const rand = (a, b) => a + Math.random() * (b - a);
const tiny = 0.0001;

// update(eased, roh) wird jedes Bild aufgerufen, done() am Schluss. Mit dem tag lassen sich Gruppen stoppen.
function tween(tag, { delay = 0, dur = 600, ease = 'outCubic', update, done }) {
  const tw = { tag, start: now + delay, dur, e: EASE[ease], update, done };
  tweens.push(tw);
  return tw;
}
const later = (tag, delay, fn) => tween(tag, { delay, dur: 1, update() {}, done: fn });
function stopTweens(prefix) { tweens = tweens.filter(t => !t.tag.startsWith(prefix)); }

const tickers = [];
AFRAME.registerComponent('fx-loop', {
  tick(t, dt) {
    now = t;
    for (const tw of tweens.slice()) {
      if (t < tw.start || !tweens.includes(tw)) continue;
      const raw = Math.min(1, (t - tw.start) / tw.dur);
      tw.update(tw.e(raw), raw);
      if (raw >= 1) {
        const i = tweens.indexOf(tw);
        if (i >= 0) tweens.splice(i, 1);
        if (tw.done) tw.done();
      }
    }
    const s = Math.min(dt || 16, 100) / 1000;
    for (const f of tickers) f(t / 1000, s);
  }
});

// ---------- Bewegungssensor: wie ist das Handy gerade gedreht? ----------
const gyro = { q: new T.Quaternion(), ok: false };
{
  const RAD = Math.PI / 180, e = new T.Euler(), qs = new T.Quaternion(), zee = new T.Vector3(0, 0, 1);
  const back = new T.Quaternion(-Math.sqrt(0.5), 0, 0, Math.sqrt(0.5)); // Kamera schaut aus der Handy-Rückseite
  gyro.listen = () => window.addEventListener('deviceorientation', ev => {
    if (ev.alpha == null) return;
    const orient = ((screen.orientation && screen.orientation.angle) || window.orientation || 0) * RAD;
    e.set(ev.beta * RAD, ev.alpha * RAD, -ev.gamma * RAD, 'YXZ');
    gyro.q.setFromEuler(e).multiply(back).multiply(qs.setFromAxisAngle(zee, -orient));
    gyro.ok = true;
  });
}

// ---------- Inhalt folgt dem Plakat, ruhig gehalten ----------
// 1. Das Gyroskop gleicht jede Drehung des Handys sofort aus (zittert nicht).
// 2. Die Bilderkennung korrigiert nur sanft: kleine Abweichungen (Zittern) sehr langsam, grosse schnell.
// Ist das Plakat kurz weg, bleibt der Inhalt dank Gyroskop im Raum stehen.
AFRAME.registerComponent('follow-anchor', {
  schema: { anchor: { type: 'selector' } },
  init() {
    this.p = new T.Vector3(); this.q = new T.Quaternion(); this.s = new T.Vector3();
    this.tp = new T.Vector3(); this.tq = new T.Quaternion(); this.ts = new T.Vector3();
    this.gPrev = new T.Quaternion(); this.d = new T.Quaternion();
    this.hasPrev = false;
    this.el.object3D.matrixAutoUpdate = false;
    this.snap = true;
  },
  tick() {
    if (!this.active) return;
    const a = this.data.anchor.object3D;
    const obj = this.el.object3D;
    const useGyro = TRACKING.gyro && gyro.ok;
    // Handy-Drehung seit dem letzten Bild rückgängig machen
    if (useGyro) {
      if (this.hasPrev && !this.snap) {
        this.d.copy(this.gPrev).invert().multiply(gyro.q).invert();
        this.p.applyQuaternion(this.d);
        this.q.premultiply(this.d);
      }
      this.gPrev.copy(gyro.q);
      this.hasPrev = true;
    }
    if (a.visible) {
      a.matrix.decompose(this.tp, this.tq, this.ts);
      if (this.snap) { this.p.copy(this.tp); this.q.copy(this.tq); this.s.copy(this.ts); this.snap = false; }
      else {
        // Wie weit liegt die Erkennung daneben? (in Plakatbreiten bzw. Bogenmass)
        const dist = this.p.distanceTo(this.tp) / Math.max(this.s.x, 1e-6);
        const move = clamp01(Math.max(dist / 0.15, this.q.angleTo(this.tq) / 0.25));
        const k = lerp(TRACKING.calm, TRACKING.fast, move * move);
        this.p.lerp(this.tp, k); this.q.slerp(this.tq, k); this.s.lerp(this.ts, k);
      }
      obj.visible = true;
    } else if (!useGyro) {
      // Ohne Bewegungssensor: ausblenden statt am Bildschirm kleben (Video läuft weiter)
      obj.visible = false;
    }
    obj.matrix.compose(this.p, this.q, this.s);
    obj.matrixWorldNeedsUpdate = true;
  }
});

// ---------- Zeichnen auf Canvas ----------
function canvasTex(w, h) {
  const cv = document.createElement('canvas');
  cv.width = w; cv.height = h;
  const tex = new T.CanvasTexture(cv);
  tex.colorSpace = T.SRGBColorSpace;
  tex.anisotropy = 4;
  return { cv, ctx: cv.getContext('2d'), tex, w, h };
}
const fadeMat = (map, extra) => new T.MeshBasicMaterial(Object.assign({ map, transparent: true, opacity: 0 }, extra));

function wrapText(ctx, text, maxW) {
  const out = [];
  let cur = '';
  for (const word of text.split(' ')) {
    const test = cur ? cur + ' ' + word : word;
    if (ctx.measureText(test).width > maxW && cur) { out.push(cur); cur = word; } else cur = test;
  }
  if (cur) out.push(cur);
  return out;
}
function paperFrame(c, bg = COL.paper) {
  const { ctx, w, h } = c;
  ctx.clearRect(0, 0, w, h);
  ctx.fillStyle = bg; ctx.fillRect(0, 0, w, h);
  ctx.strokeStyle = COL.ink; ctx.lineWidth = 4; ctx.strokeRect(2, 2, w - 4, h - 4);
  ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic'; ctx.globalAlpha = 1;
}
// Zählt alle Zahlen in einem Text von 0 hoch, Format bleibt gleich ("2'000 l", "1,56 Mio.", "7 bis 15 %")
function countUp(str, k) {
  return str.replace(/\d{1,3}(?:'\d{3})+|\d+(?:,\d+)?/g, m => {
    const dec = (m.split(',')[1] || '').length;
    const v = parseFloat(m.replace(/'/g, '').replace(',', '.')) * k;
    const [i, d] = v.toFixed(dec).split('.');
    const int = m.includes("'") ? i.replace(/\B(?=(\d{3})+(?!\d))/g, "'") : i;
    return d ? int + ',' + d : int;
  });
}

function drawFront(c, f, s) {
  const { ctx, w } = c;
  paperFrame(c);
  ctx.fillStyle = COL.ink; ctx.font = `500 104px ${FONT}`;
  ctx.fillText(countUp(f.big, s.n), 44, 158);
  ctx.fillStyle = COL.acc; ctx.fillRect(44, 186, 120 * clamp01(s.line), 6);
  ctx.fillStyle = COL.ink; ctx.font = `400 34px ${FONT}`;
  wrapText(ctx, f.text, 712).forEach((l, i) => {
    ctx.globalAlpha = clamp01(s.text * 1.6 - i * 0.5);
    ctx.fillText(l, 44, 258 + i * 46);
  });
  ctx.globalAlpha = 1; ctx.fillStyle = COL.grey; ctx.font = `400 22px ${FONT}`;
  ctx.fillText('Quelle: ' + f.src, 44, 404);
  ctx.globalAlpha = clamp01(s.hint); ctx.textAlign = 'right';
  ctx.fillText('antippen ↻', w - 40, 404);
  ctx.globalAlpha = 1;
  c.tex.needsUpdate = true;
}
function drawBack(c, f) {
  const { ctx, w } = c;
  paperFrame(c);
  ctx.fillStyle = COL.grey; ctx.font = `600 22px ${FONT}`;
  ctx.fillText('MEHR DAZU', 44, 70);
  ctx.fillStyle = COL.acc; ctx.fillRect(44, 90, 60, 5);
  ctx.fillStyle = COL.ink; ctx.font = `500 40px ${FONT}`;
  wrapText(ctx, f.more, 712).forEach((l, i) => ctx.fillText(l, 44, 160 + i * 52));
  ctx.fillStyle = COL.grey; ctx.font = `400 22px ${FONT}`;
  if (f.moreSrc) ctx.fillText('Quelle: ' + f.moreSrc, 44, 404);
  ctx.textAlign = 'right'; ctx.fillText('zurück ↻', w - 40, 404);
  c.tex.needsUpdate = true;
}
function drawHeader(c, st) {
  const { ctx } = c;
  paperFrame(c);
  ctx.fillStyle = COL.grey; ctx.font = `400 40px ${FONT}`;
  ctx.fillText('Station ' + st.nr, 46, 116);
  ctx.fillStyle = COL.ink; ctx.font = `600 72px ${FONT}`;
  ctx.fillText(st.title, 300, 124);
  c.tex.needsUpdate = true;
}
function drawQuestion(c, st, open) {
  const { ctx, w, h } = c;
  ctx.clearRect(0, 0, w, h);
  ctx.fillStyle = COL.ink; ctx.fillRect(0, 0, w, h);
  ctx.textAlign = 'center'; ctx.fillStyle = COL.paper; ctx.font = `600 54px ${FONT}`;
  ctx.fillText(st.question, w / 2, 102);
  ctx.fillStyle = '#b9b6ae'; ctx.font = `400 26px ${FONT}`;
  ctx.fillText(open ? 'Quiz schliessen ▴' : 'Antippen für ein Quiz ▾', w / 2, 160);
  ctx.textAlign = 'left';
  c.tex.needsUpdate = true;
}
const QUIZ_BOX = [36, 352, 668].map(x => ({ x, y: 236, w: 296, h: 104 }));
function drawQuiz(c, q, chosen) {
  const { ctx, w } = c;
  paperFrame(c);
  ctx.fillStyle = COL.grey; ctx.font = `600 22px ${FONT}`;
  ctx.fillText('QUIZ', 44, 62);
  ctx.fillStyle = COL.ink; ctx.font = `600 38px ${FONT}`;
  wrapText(ctx, q.q, 912).forEach((l, i) => ctx.fillText(l, 44, 118 + i * 48));
  QUIZ_BOX.forEach((b, i) => {
    let fill = null, stroke = COL.ink, txt = COL.ink, mark = '';
    if (chosen != null) {
      if (i === q.right) { fill = COL.ink; txt = COL.paper; mark = '✓ '; }
      else if (i === chosen) { stroke = COL.acc; txt = COL.acc; mark = '✗ '; }
      else { stroke = COL.line; txt = COL.grey; }
    }
    if (fill) { ctx.fillStyle = fill; ctx.fillRect(b.x, b.y, b.w, b.h); }
    ctx.strokeStyle = stroke; ctx.lineWidth = 4; ctx.strokeRect(b.x, b.y, b.w, b.h);
    const label = mark + q.a[i];
    let size = 32;
    do { ctx.font = `500 ${size}px ${FONT}`; size -= 2; } while (ctx.measureText(label).width > b.w - 28 && size > 18);
    ctx.fillStyle = txt; ctx.textAlign = 'center';
    ctx.fillText(label, b.x + b.w / 2, b.y + b.h / 2 + 11);
    ctx.textAlign = 'left';
  });
  if (chosen == null) {
    ctx.fillStyle = COL.grey; ctx.font = `400 26px ${FONT}`;
    ctx.fillText('Tippe auf eine Antwort', 44, 420);
  } else {
    ctx.fillStyle = COL.ink; ctx.font = `400 30px ${FONT}`;
    const head = chosen === q.right ? 'Richtig! ' : 'Nicht ganz. ';
    wrapText(ctx, head + q.info, 912).forEach((l, i) => ctx.fillText(l, 44, 410 + i * 42));
  }
  c.tex.needsUpdate = true;
}

// ---------- Scan-Effekt: die Linien des Plakats leuchten auf ----------
const REVEAL_VS = `varying vec2 vUv;
void main() { vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }`;
const REVEAL_FS = `uniform sampler2D uMap; uniform float uT; uniform float uO; varying vec2 vUv;
void main() {
  vec3 c = texture2D(uMap, vUv).rgb;
  float ink = 1.0 - smoothstep(0.25, 0.8, dot(c, vec3(0.299, 0.587, 0.114)));
  float d = vUv.y - (1.0 - uT * 1.25);            // > 0: bereits gescannt
  float scanned = smoothstep(0.0, 0.015, d);
  float glow = exp(-max(d, 0.0) * 5.0);            // frisch gescannt leuchtet stärker
  float edge = exp(-abs(d) * 90.0);                // die Scan-Kante
  float a = max(ink * scanned * (0.35 + 0.65 * glow) + edge * 0.9, scanned * 0.08 * glow);
  vec3 col = mix(vec3(0.745, 0.235, 0.157), vec3(1.0, 0.6, 0.5), edge);
  gl_FragColor = vec4(col, a * uO);
}`;

// ---------- Partikel ----------
function sprite(kind) {
  const c = canvasTex(128, 128), x = c.ctx;
  x.translate(64, 64);
  if (kind === 'salz') {
    x.rotate(0.4); x.fillStyle = '#fff'; x.strokeStyle = 'rgba(20,20,20,.6)'; x.lineWidth = 7;
    x.beginPath(); x.rect(-34, -34, 68, 68); x.fill(); x.stroke();
  } else if (kind === 'fasern') {
    const curve = () => { x.beginPath(); x.moveTo(-56, 18); x.bezierCurveTo(-20, -40, 20, 40, 56, -18); x.stroke(); };
    x.lineCap = 'round';
    x.strokeStyle = 'rgba(0,0,0,.35)'; x.lineWidth = 11; curve();
    x.strokeStyle = '#fff'; x.lineWidth = 6; curve();
  } else {
    x.fillStyle = '#fff'; x.strokeStyle = 'rgba(0,0,0,.45)'; x.lineWidth = 5;
    x.beginPath(); x.ellipse(0, 0, 34, 52, 0, 0, Math.PI * 2); x.fill(); x.stroke();
    x.strokeStyle = 'rgba(0,0,0,.35)'; x.lineWidth = 4;
    x.beginPath(); x.moveTo(0, -40); x.quadraticCurveTo(10, 0, 0, 40); x.stroke();
  }
  return c.tex;
}
const PARTICLES = {
  // Salzkristalle steigen auf (Verdunstung)
  salz:   { n: 50, size: [0.014, 0.028], v: [0.04, 0.09], axis: 'y', dir: 1, range: [-0.85, 1.0], spread: 0.6,
            colors: ['#ffffff', '#f0f3f5', '#e3e8ec'] },
  // Textilfasern ziehen quer durchs Bild
  fasern: { n: 40, size: [0.04, 0.08], v: [0.03, 0.06], axis: 'x', dir: 1, range: [-1.3, 1.3], spread: 0.9,
            colors: ['#be3c28', '#8f8a80', '#2b2b2b', '#d8cfc0'] },
  // Kakaobohnen fallen
  bohnen: { n: 30, size: [0.028, 0.042], v: [0.05, 0.1], axis: 'y', dir: -1, range: [-0.95, 1.0], spread: 0.6,
            colors: ['#6b3f22', '#8a5232', '#4a2a17'] },
};
function makeParticles(kind) {
  const P = PARTICLES[kind];
  const mesh = new T.InstancedMesh(new T.PlaneGeometry(1, 1),
    new T.MeshBasicMaterial({ map: sprite(kind), transparent: true, depthWrite: false, side: T.DoubleSide }), P.n);
  mesh.frustumCulled = false;
  const other = P.axis === 'y' ? 'x' : 'y';
  const [a, b] = P.range;
  const items = [];
  const col = new T.Color();
  const spawn = (p, anywhere) => {
    p[P.axis] = anywhere ? rand(a, b) : (P.dir > 0 ? a : b);
    p[other] = P.axis === 'y' ? rand(-P.spread, P.spread) : rand(-0.9, 0.9);
    p.z = rand(0.03, 0.35); p.v = rand(...P.v); p.s = rand(...P.size);
    p.rz = rand(0, 6.28); p.spin = rand(-1.2, 1.2); p.ph = rand(0, 6.28);
    return p;
  };
  for (let n = 0; n < P.n; n++) {
    items.push(spawn({}, true));
    mesh.setColorAt(n, col.set(P.colors[n % P.colors.length]));
  }
  const dummy = new T.Object3D();
  const api = {
    mesh, fade: 0,
    tick(t, dt) {
      items.forEach((p, n) => {
        p[P.axis] += P.dir * p.v * dt;
        p[other] += Math.sin(t * 0.9 + p.ph) * 0.015 * dt;
        p.rz += p.spin * dt;
        if (p[P.axis] > b || p[P.axis] < a) spawn(p, false);
        const u = (p[P.axis] - a) / (b - a);
        const f = clamp01(Math.min(u, 1 - u) / 0.12);
        dummy.position.set(p.x, p.y, p.z);
        dummy.rotation.set(0, kind === 'fasern' ? Math.sin(t * p.spin + p.ph) * 1.2 : 0, p.rz);
        dummy.scale.setScalar(Math.max(tiny, p.s * f * api.fade));
        dummy.updateMatrix();
        mesh.setMatrixAt(n, dummy.matrix);
      });
      mesh.instanceMatrix.needsUpdate = true;
    }
  };
  return api;
}

// ---------- 3D-Objekte ----------
// Jedes Objekt: obj (Group), reset(), play(tag), tick(t, dt)
function modelAkku() {
  const obj = new T.Group(), spin = new T.Group();
  obj.add(spin);
  const H = 0.3, R = 0.075;
  const roll = canvasTex(64, 256);
  ['#c27a4a', '#9aa0a6', '#2a2a2a', '#d9d4c7'].forEach((c, i) => {
    roll.ctx.fillStyle = c;
    for (let y = i * 6; y < 256; y += 24) roll.ctx.fillRect(0, y, 64, 6);
  });
  spin.add(new T.Mesh(new T.CylinderGeometry(R, R, H, 40),
    new T.MeshStandardMaterial({ map: roll.tex, roughness: 0.45, metalness: 0.4 })));
  const shell = canvasTex(512, 256);
  shell.ctx.fillStyle = '#1b1b1b'; shell.ctx.fillRect(0, 0, 512, 256);
  shell.ctx.fillStyle = COL.acc; shell.ctx.fillRect(0, 96, 512, 64);
  shell.ctx.fillStyle = COL.paper; shell.ctx.font = `600 40px ${FONT}`; shell.ctx.textAlign = 'center';
  shell.ctx.fillText('Li-ion', 256, 142);
  const shellMat = new T.MeshStandardMaterial({ map: shell.tex, roughness: 0.35, metalness: 0.5, side: T.DoubleSide });
  const halves = [0, 1].map(j => {
    const m = new T.Mesh(new T.CylinderGeometry(R + 0.008, R + 0.008, H + 0.006, 32, 1, true, j * Math.PI, Math.PI), shellMat);
    spin.add(m);
    return m;
  });
  const silver = new T.MeshStandardMaterial({ color: '#c9c9c9', metalness: 0.8, roughness: 0.3 });
  [[R + 0.008, 0.006, H / 2 + 0.003], [R + 0.008, 0.006, -H / 2 - 0.003], [0.03, 0.016, H / 2 + 0.014]].forEach(([r, h, y]) => {
    const m = new T.Mesh(new T.CylinderGeometry(r, r, h, 40), silver);
    m.position.y = y; spin.add(m);
  });
  // Elemente als Kacheln wie im Periodensystem
  const tiles = [['3', 'Li', 'Lithium'], ['27', 'Co', 'Kobalt']].map(([nr, sym, name]) => {
    const c = canvasTex(256, 256);
    paperFrame(c);
    c.ctx.fillStyle = COL.acc; c.ctx.font = `600 44px ${FONT}`; c.ctx.fillText(nr, 24, 60);
    c.ctx.textAlign = 'center'; c.ctx.fillStyle = COL.ink; c.ctx.font = `600 116px ${FONT}`; c.ctx.fillText(sym, 128, 170);
    c.ctx.fillStyle = COL.grey; c.ctx.font = `400 32px ${FONT}`; c.ctx.fillText(name, 128, 228);
    const m = new T.Mesh(new T.PlaneGeometry(0.11, 0.11), fadeMat(c.tex, { opacity: 1, side: T.DoubleSide }));
    obj.add(m);
    return m;
  });
  let open = 0, tileS = 0;
  return {
    obj,
    reset() { open = 0; tileS = 0; },
    play(tag) {
      tween(tag, { dur: 1000, ease: 'inOutCubic', update: k => { open = k; } });
      tween(tag, { delay: 600, dur: 700, ease: 'outBack', update: k => { tileS = k; } });
    },
    tick(t, dt) {
      spin.rotation.y += dt * 0.7;
      halves[0].position.x = open * 0.07;
      halves[1].position.x = -open * 0.07;
      tiles.forEach((m, j) => {
        const a = t * 0.9 + j * Math.PI;
        m.position.set(Math.sin(a) * 0.2, 0.06 - j * 0.12, Math.cos(a) * 0.2);
        m.scale.setScalar(Math.max(tiny, tileS));
      });
    }
  };
}

function shirtShape() {
  const s = new T.Shape();
  s.moveTo(-0.06, 0.23); s.quadraticCurveTo(0, 0.17, 0.06, 0.23);
  [[0.13, 0.21], [0.24, 0.12], [0.18, 0.04], [0.13, 0.08], [0.13, -0.23],
   [-0.13, -0.23], [-0.13, 0.08], [-0.18, 0.04], [-0.24, 0.12], [-0.13, 0.21], [-0.06, 0.23]].forEach(p => s.lineTo(...p));
  return s;
}
function modelShirt() {
  const obj = new T.Group(), spin = new T.Group();
  obj.add(spin);
  const shape = shirtShape();
  const body = new T.Mesh(new T.ExtrudeGeometry(shape, { depth: 0.03, bevelEnabled: true, bevelThickness: 0.008, bevelSize: 0.008, bevelSegments: 2, curveSegments: 12 }),
    new T.MeshStandardMaterial({ color: '#f1eee8', roughness: 0.9 }));
  body.geometry.translate(0, 0, -0.015);
  spin.add(body);
  // Wasser, das im T-Shirt hochsteigt
  const water = new T.ShaderMaterial({
    uniforms: { uLevel: { value: -0.3 }, uTime: { value: 0 } },
    transparent: true,
    vertexShader: 'varying vec2 vP; void main() { vP = position.xy; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }',
    fragmentShader: `uniform float uLevel; uniform float uTime; varying vec2 vP;
      void main() {
        float surf = uLevel + 0.008 * sin(vP.x * 38.0 + uTime * 3.0);
        if (vP.y > surf) discard;
        float top = smoothstep(surf - 0.02, surf, vP.y);
        gl_FragColor = vec4(mix(vec3(0.23, 0.45, 0.7), vec3(0.55, 0.75, 0.92), top), 0.92);
      }`,
  });
  [0.026, -0.026].forEach(z => {
    const m = new T.Mesh(new T.ShapeGeometry(shape, 12), water);
    m.position.z = z;
    if (z < 0) m.rotation.y = Math.PI;
    spin.add(m);
  });
  const label = canvasTex(512, 192);
  const drawLabel = k => {
    paperFrame(label);
    label.ctx.textAlign = 'center';
    label.ctx.fillStyle = COL.ink; label.ctx.font = `600 84px ${FONT}`; label.ctx.fillText(countUp("2'700 l", k), 256, 104);
    label.ctx.fillStyle = COL.grey; label.ctx.font = `400 32px ${FONT}`; label.ctx.fillText('Wasser für 1 T-Shirt', 256, 160);
    label.tex.needsUpdate = true;
  };
  const labelMesh = new T.Mesh(new T.PlaneGeometry(0.3, 0.1125), fadeMat(label.tex, { opacity: 1 }));
  labelMesh.position.set(0, -0.32, 0.03);
  obj.add(labelMesh);
  return {
    obj,
    reset() { water.uniforms.uLevel.value = -0.3; drawLabel(0); },
    play(tag) {
      tween(tag, { dur: 2400, ease: 'inOutCubic', update: k => { water.uniforms.uLevel.value = lerp(-0.24, 0.235, k); drawLabel(k); } });
    },
    tick(t) {
      spin.rotation.y = Math.sin(t * 0.6) * 0.6;
      water.uniforms.uTime.value = t;
    }
  };
}

function modelKakao() {
  const obj = new T.Group(), spin = new T.Group(), tilt = new T.Group();
  obj.add(spin); spin.add(tilt);
  tilt.rotation.z = 0.35;
  const pts = [];
  for (let k = 0; k <= 24; k++) {
    const v = k / 24;
    pts.push(new T.Vector2(0.105 * Math.pow(Math.sin(Math.PI * v), 0.75) + tiny, (v - 0.5) * 0.4));
  }
  const halfGeo = phiStart => {
    const g = new T.LatheGeometry(pts, 40, phiStart, Math.PI);
    const p = g.attributes.position;
    for (let n = 0; n < p.count; n++) {   // Rillen der Kakaoschote
      const x = p.getX(n), z = p.getZ(n);
      const f = 1 + 0.1 * Math.pow(Math.abs(Math.cos(5 * Math.atan2(x, z))), 4);
      p.setX(n, x * f); p.setZ(n, z * f);
    }
    g.computeVertexNormals();
    return g;
  };
  const outside = new T.MeshStandardMaterial({ color: '#b8692a', roughness: 0.65 });
  const inside = new T.MeshStandardMaterial({ color: '#efe3c8', roughness: 0.9, side: T.BackSide });
  // Jede Hälfte hängt an einem Scharnier hinten an der Schote und klappt auf
  const hinges = [0, Math.PI].map(phi => {
    const hinge = new T.Group();
    hinge.position.z = -0.1;
    const g = halfGeo(phi);
    [outside, inside].forEach(m => { const mesh = new T.Mesh(g, m); mesh.position.z = 0.1; hinge.add(mesh); });
    tilt.add(hinge);
    return hinge;
  });
  const stem = new T.Mesh(new T.CylinderGeometry(0.008, 0.011, 0.05, 10), new T.MeshStandardMaterial({ color: '#5a3a1c' }));
  stem.position.y = 0.215; tilt.add(stem);
  const beanMat = new T.MeshStandardMaterial({ color: '#e9dfd2', roughness: 0.8 });
  const beans = [];
  for (let b = 0; b < 10; b++) {
    const m = new T.Mesh(new T.SphereGeometry(0.02, 14, 10), beanMat);
    const a = b * 2.4;
    m.position.set(Math.sin(a) * 0.03, -0.13 + b * 0.029, Math.cos(a) * 0.03);
    tilt.add(m); beans.push(m);
  }
  let open = 0, pop = 0;
  return {
    obj,
    reset() { open = 0; pop = 0; },
    play(tag) {
      tween(tag, { dur: 1100, ease: 'inOutCubic', update: k => { open = k; } });
      tween(tag, { delay: 500, dur: 900, ease: 'outBack', update: k => { pop = k; } });
    },
    tick(t, dt) {
      spin.rotation.y += dt * 0.5;
      hinges[0].rotation.y = open * 0.9;
      hinges[1].rotation.y = -open * 0.9;
      beans.forEach((m, b) => {
        const s = lerp(0.6, 1, clamp01(pop * 1.4 - b * 0.04));
        m.scale.set(s, s * 1.45, s);
      });
    }
  };
}
const MODELS = { akku: modelAkku, shirt: modelShirt, kakao: modelKakao };

// ---------- Station aufbauen ----------
const scene = document.getElementById('scene');
const loader = new T.TextureLoader();
const deg = d => d * Math.PI / 180;

function buildStation(st, i) {
  const tag = 'st' + i + ':';
  const root = document.createElement('a-entity');
  root.setAttribute('follow-anchor', 'anchor: #anchor' + i);
  root.setAttribute('visible', 'false');
  scene.appendChild(root);
  const R = root.object3D;
  const taps = [];
  // Antippbare Teile brauchen ein eigenes a-entity, damit der Raycaster sie findet
  function tappable(obj, onTap) {
    const el = document.createElement('a-entity');
    root.appendChild(el);
    el.setObject3D('mesh', obj);
    el.addEventListener('click', e => { if (st.active) onTap(e.detail && e.detail.intersection); });
    taps.push(el);
    return el;
  }

  if (DEMO) {   // Im Testmodus das Plakat selbst anzeigen
    const tex = loader.load(st.poster);
    tex.colorSpace = T.SRGBColorSpace;
    R.add(new T.Mesh(new T.PlaneGeometry(1, POSTER_H), new T.MeshBasicMaterial({ map: tex })));
  }

  // Scan-Effekt
  const U = { uMap: { value: loader.load(st.poster) }, uT: { value: 0 }, uO: { value: 0 } };
  const reveal = new T.Mesh(new T.PlaneGeometry(1, POSTER_H),
    new T.ShaderMaterial({ uniforms: U, vertexShader: REVEAL_VS, fragmentShader: REVEAL_FS, transparent: true, depthWrite: false }));
  reveal.position.z = 0.004;
  R.add(reveal);

  // Schatten unter dem Video, wenn es sich hebt
  const sh = canvasTex(256, 352);
  sh.ctx.shadowColor = '#000'; sh.ctx.shadowBlur = 28; sh.ctx.fillStyle = '#000';
  sh.ctx.fillRect(40, 40, 176, 272);
  const shadow = new T.Mesh(new T.PlaneGeometry(256 / 176, 352 / 272 * POSTER_H), fadeMat(sh.tex, { depthWrite: false }));
  shadow.position.set(0, -0.025, 0.006);
  R.add(shadow);

  // Video
  const vEl = document.getElementById(st.video);
  const vTex = new T.VideoTexture(vEl);
  vTex.colorSpace = T.SRGBColorSpace;
  const vMat = fadeMat(vTex);
  if (st.chroma) {   // Greenscreen: diese Farbe wird durchsichtig
    const key = new T.Color(st.chroma);
    vMat.onBeforeCompile = s => {
      s.uniforms.uKey = { value: new T.Vector3(key.r, key.g, key.b) };
      s.fragmentShader = 'uniform vec3 uKey;\n' + s.fragmentShader.replace('#include <map_fragment>',
        '#include <map_fragment>\n diffuseColor.a *= smoothstep(0.28, 0.42, distance(diffuseColor.rgb, uKey));');
    };
  }
  const video = new T.Mesh(new T.PlaneGeometry(1, 1.4139), vMat);
  R.add(video);

  // Karten
  const cards = [];
  let qGroup, qEl, qTex, questionTex;
  LAYOUT.forEach((c, k) => {
    const g = new T.Group(), flip = new T.Group();
    g.add(flip);
    g.visible = false;
    const cd = { c, k, g, flip, mats: [], base: new T.Vector3(c.x, c.y, c.z), bob: 0, ready: false, flipped: false,
                 s: { n: 0, line: 0, text: 0, hint: 0 } };
    const addPlane = (tex, back) => {
      const m = fadeMat(tex);
      const mesh = new T.Mesh(new T.PlaneGeometry(c.w, c.h), m);
      if (back) mesh.rotation.y = Math.PI;
      flip.add(mesh); cd.mats.push(m);
    };
    if (c.card.startsWith('fakt')) {
      const f = st.facts[parseInt(c.card.slice(4), 10) - 1];
      cd.fact = f;
      cd.front = canvasTex(800, 440);
      const back = canvasTex(800, 440);
      drawFront(cd.front, f, cd.s); drawBack(back, f);
      addPlane(cd.front.tex, false); addPlane(back.tex, true);
      tappable(g, () => flipCard(cd));
      // rote Linie vom Plakatrand zur Karte
      const sgn = Math.sign(c.x);
      const start = new T.Vector3(sgn * 0.52, c.y, 0.012);
      const end = new T.Vector3(-sgn * c.w / 2, 0, 0).applyAxisAngle(new T.Vector3(0, 1, 0), deg(c.rot)).add(new T.Vector3(c.x, c.y, c.z));
      const dir = end.sub(start);
      cd.len = dir.length();
      const lineMat = new T.MeshBasicMaterial({ color: COL.acc, transparent: true, depthWrite: false });
      const geo = new T.PlaneGeometry(1, 0.005);
      geo.translate(0.5, 0, 0);
      cd.line = new T.Mesh(geo, lineMat);
      cd.line.position.copy(start);
      cd.line.quaternion.setFromUnitVectors(new T.Vector3(1, 0, 0), dir.normalize());
      cd.dot = new T.Mesh(new T.CircleGeometry(0.011, 20), lineMat);
      cd.dot.position.copy(start);
      R.add(cd.line, cd.dot);
    } else if (c.card === 'header') {
      const t = canvasTex(1000, 200);
      drawHeader(t, st);
      addPlane(t.tex, false);
      R.add(g);
    } else if (c.card === 'frage') {
      questionTex = canvasTex(1000, 200);
      drawQuestion(questionTex, st, false);
      addPlane(questionTex.tex, false);
      tappable(g, () => { if (cd.ready) setQuiz(!st.quizOpen); });
      // Quiz klappt unter der Frage auf
      qTex = canvasTex(1000, 520);
      const qH = c.w * 520 / 1000;
      const qGeo = new T.PlaneGeometry(c.w, qH);
      qGeo.translate(0, -qH / 2, 0);
      qGroup = new T.Group();
      qGroup.add(new T.Mesh(qGeo, fadeMat(qTex.tex, { opacity: 1 })));
      qGroup.position.set(c.x, c.y - c.h / 2 - 0.02, c.z);
      qEl = tappable(qGroup, hit => {
        if (!st.quizOpen || st.quizChosen != null || !hit || !hit.uv) return;
        const x = hit.uv.x * 1000, y = (1 - hit.uv.y) * 520;
        QUIZ_BOX.forEach((b, j) => {
          if (x >= b.x && x <= b.x + b.w && y >= b.y && y <= b.y + b.h) { st.quizChosen = j; drawQuiz(qTex, st.quiz, j); }
        });
      });
    }
    cards.push(cd);
  });

  function flipCard(cd) {
    if (!cd.ready) return;
    cd.flipped = !cd.flipped;
    const from = cd.flip.rotation.y, to = cd.flipped ? Math.PI : 0;
    stopTweens(tag + 'f' + cd.k);
    tween(tag + 'f' + cd.k, { dur: 700, ease: 'inOutCubic', update: (e, raw) => {
      cd.flip.rotation.y = lerp(from, to, e);
      cd.flip.position.z = Math.sin(raw * Math.PI) * 0.08;
    } });
  }

  function setQuiz(open) {
    st.quizOpen = open;
    drawQuestion(questionTex, st, open);
    qEl.classList.toggle('tap', open);
    qGroup.visible = true;
    const from = qGroup.scale.y;
    stopTweens(tag + 'q');
    tween(tag + 'q', { dur: open ? 600 : 350, ease: open ? 'outBack' : 'inCubic',
      update: k => { qGroup.scale.y = Math.max(tiny, lerp(from, open ? 1 : 0, k)); },
      done: () => { if (!open) qGroup.visible = false; } });
  }

  // 3D-Objekt
  const model = MODELS[st.model]();
  const mg = model.obj;
  const m = { base: new T.Vector3(), s: tiny };
  const CENTER = new T.Vector3(0, 0.06, 0.38);
  const REST = new T.Vector3(MODEL_REST.x, MODEL_REST.y, MODEL_REST.z);
  function moveModel(to, s, dur) {
    const fb = m.base.clone(), fs = m.s;
    tween(tag + 'm', { dur, ease: 'inOutCubic', update: k => { m.base.lerpVectors(fb, to, k); m.s = lerp(fs, s, k); } });
  }
  function modelShow(fromStart) {
    stopTweens(tag + 'm');
    if (fromStart) {
      m.base.set(0, 0.02, 0.02); m.s = tiny;
      tween(tag + 'm', { delay: TIMING.model, dur: 900, ease: 'outBack', update: k => { m.base.lerpVectors(new T.Vector3(0, 0.02, 0.02), CENTER, k); m.s = lerp(tiny, 1, k); } });
    } else {
      moveModel(CENTER, 1, 700);
    }
    const t0 = fromStart ? TIMING.explode : 700;
    later(tag + 'm', t0, () => { model.reset(); model.play(tag + 'm'); });
    later(tag + 'm', fromStart ? TIMING.modelRest : 3300, () => moveModel(REST, MODEL_REST.scale, 900));
  }
  tappable(mg, () => modelShow(false));

  // Partikel
  const parts = makeParticles(st.particles);
  R.add(parts.mesh);

  st.root = root; st.tag = tag; st.taps = taps; st.qEl = qEl;

  st.reset = () => {
    stopTweens(tag);
    U.uT.value = 0; U.uO.value = 0;
    vMat.opacity = 0; video.position.z = 0.01; video.scale.setScalar(0.94);
    shadow.material.opacity = 0;
    cards.forEach(cd => {
      cd.g.visible = false; cd.ready = false; cd.bob = 0; cd.flipped = false;
      cd.flip.rotation.y = 0; cd.flip.position.z = 0;
      cd.mats.forEach(mm => { mm.opacity = 0; });
      Object.assign(cd.s, { n: 0, line: 0, text: 0, hint: 0 });
      if (cd.fact) drawFront(cd.front, cd.fact, cd.s);
      if (cd.line) { cd.line.scale.x = tiny; cd.dot.scale.setScalar(tiny); }
    });
    st.quizOpen = false; st.quizChosen = null;
    qGroup.visible = false; qGroup.scale.y = tiny;
    drawQuiz(qTex, st.quiz, null); drawQuestion(questionTex, st, false);
    model.reset(); m.s = tiny;
    parts.fade = 0;
  };

  st.intro = () => {
    // 1. Scan läuft über das Plakat
    U.uO.value = 1;
    tween(tag, { dur: 1800, ease: 'inOutCubic', update: k => { U.uT.value = k; } });
    tween(tag, { delay: 200, dur: 1500, update: k => { parts.fade = k; } });
    // 2. 3D-Objekt
    modelShow(true);
    // 3. Karten fliegen heraus, Zahlen zählen hoch
    cards.forEach(cd => {
      const c = cd.c, fact = !!cd.fact;
      const to = new T.Vector3(c.x, c.y, c.z);
      const from = fact ? new T.Vector3(c.x * 0.3, c.y, 0) : new T.Vector3(0, Math.sign(c.y) * 0.707, 0.02);
      tween(tag, { delay: c.delay, dur: 900, ease: 'outBack', update: (k, raw) => {
        cd.g.visible = true;
        cd.base.lerpVectors(from, to, k);
        cd.g.rotation.set(fact ? lerp(-1.1, 0, k) : 0, lerp(0, deg(c.rot), k), 0);
        cd.g.scale.set(lerp(fact ? 0.4 : 0.05, 1, k), fact ? lerp(0.4, 1, k) : 1, 1);
        cd.mats.forEach(mm => { mm.opacity = clamp01(raw * 2); });
      }, done: () => {
        cd.ready = true;
        tween(tag, { dur: 800, ease: 'inOutCubic', update: k => { cd.bob = k; } });
      } });
      if (cd.line) tween(tag, { delay: c.delay + 150, dur: 600, update: (k, raw) => {
        cd.line.scale.x = Math.max(tiny, cd.len * k);
        cd.dot.scale.setScalar(Math.max(tiny, clamp01(raw * 3)));
      } });
      if (fact) tween(tag, { delay: c.delay + 500, dur: 1400, update: (k, raw) => {
        Object.assign(cd.s, { n: k, line: raw * 1.8, text: raw * 1.5 - 0.3, hint: raw * 2 - 1 });
        drawFront(cd.front, cd.fact, cd.s);
      } });
    });
    // 4. Video hebt sich aus dem Plakat
    later(tag, TIMING.video, () => { vEl.currentTime = 0; vEl.play().catch(() => {}); });
    tween(tag, { delay: TIMING.video, dur: 1100, update: k => {
      vMat.opacity = k;
      video.position.z = lerp(0.01, 0.05, k);
      video.scale.setScalar(lerp(0.94, 1, k));
      shadow.material.opacity = 0.45 * k;
      U.uO.value = 1 - k;
    } });
  };

  st.tick = (t, dt) => {
    cards.forEach(cd => {
      cd.g.position.copy(cd.base);
      cd.g.position.y += cd.bob * 0.012 * Math.sin(t * (1.6 + cd.k * 0.15) + cd.k);
    });
    mg.position.copy(m.base);
    mg.scale.setScalar(Math.max(tiny, m.s));
    model.tick(t, dt);
    parts.tick(t, dt);
  };
  tickers.push((t, dt) => { if (st.active) st.tick(t, dt); });
}

// ---------- Ablauf ----------
const bar = document.getElementById('bar');
const scanning = document.getElementById('scanning');
const hint = document.getElementById('hint');
const videos = ['v0', 'v1', 'v2'].map(id => document.getElementById(id));
let hintShown = false;

function activate(st) {
  STATIONS.forEach(o => { if (o !== st && o.active) deactivate(o); });
  st.active = true;
  const follow = st.root.components['follow-anchor'];
  follow.snap = true; follow.active = true;
  st.root.setAttribute('visible', 'true');
  st.taps.forEach(el => { if (el !== st.qEl) el.classList.add('tap'); });
  st.reset();
  st.intro();
  if (!hintShown) {
    hintShown = true;
    later('hint', TIMING.hint, () => hint.classList.remove('hidden'));
    later('hint', TIMING.hint + 4500, () => hint.classList.add('hidden'));
  }
}

function deactivate(st) {
  st.active = false;
  clearTimeout(st.timer); st.timer = null;
  stopTweens(st.tag);
  st.root.components['follow-anchor'].active = false;
  st.root.setAttribute('visible', 'false');
  st.taps.forEach(el => el.classList.remove('tap'));
  document.getElementById(st.video).pause();
  updateUi();
}

function updateUi(lost) {
  const cur = STATIONS.find(s => s.active);
  if (!cur) { bar.classList.add('hidden'); if (!DEMO) scanning.classList.remove('hidden'); return; }
  scanning.classList.add('hidden');
  document.getElementById('barStation').textContent = 'Station ' + cur.nr;
  document.getElementById('barTitle').textContent = lost ? 'Plakat wieder ins Bild nehmen' : cur.title;
  bar.classList.remove('hidden');
}

function wire() {
  const fx = document.createElement('a-entity');
  fx.setAttribute('fx-loop', '');
  scene.appendChild(fx);
  STATIONS.forEach((st, i) => {
    st.active = false; st.timer = null;
    buildStation(st, i);
    const anchor = document.getElementById('anchor' + i);
    anchor.addEventListener('targetFound', () => {
      if (st.active) {            // nur kurz verloren: einfach weiterlaufen lassen
        clearTimeout(st.timer); st.timer = null;
        const v = document.getElementById(st.video); if (v.paused) v.play().catch(() => {});
      } else {
        activate(st);
      }
      updateUi(false);
    });
    anchor.addEventListener('targetLost', () => {
      if (!st.active) return;
      updateUi(true);
      clearTimeout(st.timer);
      st.timer = setTimeout(() => deactivate(st), GRACE_MS);
    });
  });
}
if (scene.hasLoaded) wire(); else scene.addEventListener('loaded', wire);

// ---------- Testmodus ohne Kamera: index.html?demo ----------
let demoIdx = -1, yaw = 0, pitch = 0, tYaw = 0, tPitch = 0;
const demoPos = new T.Vector3(0, 0.2, -2.3), demoQ = new T.Quaternion(), demoE = new T.Euler(), one = new T.Vector3(1, 1, 1);
function showDemo(i) {
  STATIONS.forEach((st, j) => { if (j !== i) document.getElementById('anchor' + j).object3D.visible = false; });
  demoIdx = i;
  const a = document.getElementById('anchor' + i);
  a.object3D.matrix = new T.Matrix4().compose(demoPos, demoQ, one);
  a.object3D.visible = true;
  a.emit('targetFound');
  document.querySelectorAll('#demoBar button').forEach(b => b.classList.toggle('on', +b.dataset.i === i));
}
function startDemo() {
  document.body.classList.add('demo');
  scene.setAttribute('background', 'color: #1d1d1d');
  document.getElementById('demoBar').classList.remove('hidden');
  document.querySelectorAll('#demoBar button').forEach(b => b.addEventListener('click', () => showDemo(+b.dataset.i)));
  window.addEventListener('keydown', e => { if ('123'.includes(e.key)) showDemo(+e.key - 1); });
  // Maus bewegt das Plakat leicht, damit man die Tiefe sieht
  window.addEventListener('pointermove', e => {
    tYaw = (e.clientX / innerWidth - 0.5) * 0.7;
    tPitch = (e.clientY / innerHeight - 0.5) * 0.4;
  });
  tickers.push(() => {
    if (demoIdx < 0) return;
    yaw += (tYaw - yaw) * 0.08; pitch += (tPitch - pitch) * 0.08;
    demoQ.setFromEuler(demoE.set(pitch, yaw, 0));
    document.getElementById('anchor' + demoIdx).object3D.matrix.compose(demoPos, demoQ, one);
  });
  showDemo(0);
}

if (DEMO) document.getElementById('startBtn').textContent = 'Test ohne Kamera starten';

const status = scanning.querySelector('p');
function showError(detail) {
  document.getElementById('errorDetail').textContent = detail || '';
  document.getElementById('error').classList.remove('hidden');
}
// Videos einmal per Klick "freischalten" (wichtig für iPhone). Höchstens 1.5 s warten, falls ein Video hängt.
function unlockVideos() {
  return Promise.all(videos.map(v => Promise.race([
    v.play().then(() => { v.pause(); v.currentTime = 0; }).catch(() => {}),
    new Promise(r => setTimeout(r, 1500)),
  ])));
}

// Nur beim Testen über den Tunnel: Zustand an den Test-Server melden
const dbg = location.hostname.endsWith('trycloudflare.com')
  ? msg => { fetch('log?' + encodeURIComponent(msg)).catch(() => {}); }
  : () => {};
window.addEventListener('error', e => dbg('JS-Fehler: ' + e.message));
window.addEventListener('unhandledrejection', e => dbg('Promise-Fehler: ' + (e.reason && (e.reason.message || e.reason))));

document.getElementById('startBtn').addEventListener('click', async () => {
  const unlocking = unlockVideos();   // muss direkt im Tipp starten
  // Bewegungssensor: das iPhone fragt danach, auch das muss direkt im Tipp passieren
  const DOE = window.DeviceOrientationEvent;
  const motion = !TRACKING.gyro || !DOE ? Promise.resolve('aus')
    : DOE.requestPermission ? DOE.requestPermission().catch(() => 'denied') : Promise.resolve('granted');
  motion.then(r => { dbg('Bewegungssensor: ' + r); if (r === 'granted') gyro.listen(); });
  if (DEMO) {
    await unlocking;
    document.getElementById('start').classList.add('hidden');
    startDemo();
    return;
  }
  if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
    showError('Dieser Browser erlaubt hier keine Kamera. Öffne die Seite in Safari (iPhone) oder Chrome (Android) über https.');
    return;
  }
  // Kamera nur EINMAL öffnen und die Verbindung an MindAR weitergeben.
  // (Auf dem iPhone scheitert ein zweites Öffnen kurz nach dem Schliessen.)
  let stream;
  try {
    stream = await navigator.mediaDevices.getUserMedia({ audio: false, video: { facingMode: 'environment' } });
    dbg('Kamera ok');
  } catch (e) {
    dbg('Kamera-Fehler ' + e.name);
    showError('Fehler: ' + e.name + (e.message ? ' (' + e.message + ')' : ''));
    return;
  }
  const md = navigator.mediaDevices, original = md.getUserMedia.bind(md);
  md.getUserMedia = () => { md.getUserMedia = original; return Promise.resolve(stream); };
  await unlocking;
  document.getElementById('start').classList.add('hidden');
  scanning.classList.remove('hidden');
  status.textContent = 'Bilderkennung wird geladen …';
  scene.addEventListener('arReady', () => { status.textContent = 'Halte die Kamera auf ein Plakat'; dbg('arReady'); }, { once: true });
  const sys = scene.systems['mindar-image-system'];
  sys.start();
  dbg('MindAR gestartet');
  // iPhone: das Kamerabild ausdrücklich stumm schalten und abspielen
  setTimeout(() => {
    const v = sys.video;
    if (!v) return;
    v.muted = true;
    v.play().catch(e => dbg('play-Fehler ' + e.name));
  }, 50);
  let n = 0;
  const watch = setInterval(() => {
    const v = sys.video, tr = stream.getVideoTracks()[0];
    dbg(`Stand ${++n}: video readyState=${v && v.readyState} ${v && v.videoWidth}x${v && v.videoHeight} paused=${v && v.paused} track=${tr && tr.readyState} controller=${!!sys.controller}`);
    if (n >= 8 || status.textContent.startsWith('Halte')) clearInterval(watch);
  }, 2000);
});

scene.addEventListener('arError', e => {
  showError('Fehler beim Start der Kamera' + (e.detail && e.detail.error ? ': ' + e.detail.error : ''));
});
})();
