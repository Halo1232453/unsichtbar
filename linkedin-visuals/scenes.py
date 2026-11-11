# Vier Motive im digitalONLY-Premium-Stil. build.py setzt sie in engine.html ein.
ICON = {
 "target": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.2"/></svg>',
 "pin": '<svg viewBox="0 0 24 24"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.6"/></svg>',
 "star": '<svg viewBox="0 0 24 24"><path d="M12 3.5l2.6 5.4 5.9.8-4.3 4.1 1 5.8L12 16.8l-5.2 2.8 1-5.8-4.3-4.1 5.9-.8z"/></svg>',
 "qr": '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><path d="M14 14h3v3h-3zM18 18h3v3h-3zM14 20h1M20 14v1"/></svg>',
 "chat": '<svg viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4z"/></svg>',
 "reply": '<svg viewBox="0 0 24 24"><path d="M10 8L5 12l5 4"/><path d="M5 12h9a5 5 0 0 1 5 5v1"/></svg>',
 "check": '<svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
}

def item(icon, title, text, t, buzz=None):
    b = f' data-buzz="{buzz}"' if buzz else ''
    return f'<div class="item" data-a="rise" data-t="{t}"{b}><div class="tile">{ICON[icon]}</div><div><h3>{title}</h3><p>{text}</p></div></div>'

def rings(left, top, size, t, color="rgba(255,90,74,.35)"):
    r = ''.join(f'<div class="ring" style="inset:0;border-color:{color}"></div>' for _ in range(3))
    return f'<div class="abs" data-rings="{t}" style="left:{left}px;top:{top}px;width:{size}px;height:{size}px">{r}</div>'

FOOT = lambda l, r, t=9: f'<div class="foot" data-a="fade" data-t="{t}"><span>{l}</span><span>{r}</span></div>'

SCENES = {}

# ---------- Bertan: Verzeichnis-Abo ----------
bars = ''.join(f'<div class="bar" data-h="{h}" style="flex:1;border-radius:8px 8px 3px 3px;background:{"linear-gradient(180deg,#f3d697,#b8935a);box-shadow:0 0 30px rgba(226,192,122,.55)" if i == 6 else "rgba(255,255,255,.16)"}"></div>' for i, h in enumerate([38, 52, 45, 64, 58, 72, 94]))
SCENES["2026-11-09-mo-bertan"] = dict(theme="theme-gold", grid=False, end=10, body=f'''
<div class="eyebrow" data-a="fade" data-t=".15"><i></i>Unbequeme Frage</div>
<h1 data-words data-t=".35">Wie viele Anrufe hat Ihnen Ihr Abo <span class="gold">letztes Jahr gebracht?</span></h1>
<div class="abs card" data-a="left" data-t="1.6" data-buzz="4.35" style="left:80px;top:580px;width:470px;padding:34px 36px 30px">
 <div class="label mono" style="color:var(--gold)">Rechnung 2025</div>
 <div style="font:700 36px 'Inter Tight';margin:12px 0 8px;letter-spacing:-.02em">Verzeichnis-Abo</div>
 <div class="row"><span style="color:var(--muted)">Jahresgebühr</span><b>CHF <span class="q flick">?</span></b></div>
 <div class="row"><span style="color:var(--muted)">Aufrufe</span><span class="q flick">?</span></div>
 <div class="row"><span style="color:var(--muted)">Klicks</span><span class="q flick">?</span></div>
 <div class="row"><span style="color:var(--muted)">Anrufe</span><span class="q flick">?</span></div>
</div>
<div class="abs" data-a="slam" data-t="4.2" data-d=".35" style="left:118px;top:968px;transform:rotate(-9deg);border:4px solid var(--red);color:var(--red);font:700 32px 'JetBrains Mono';letter-spacing:.12em;padding:10px 22px;border-radius:10px;background:rgba(9,9,11,.82);box-shadow:0 0 30px rgba(255,90,74,.35)">BLIND BEZAHLT</div>
{rings(520, 580, 560, 5.6, "rgba(226,192,122,.30)")}
<div class="abs phone" data-a="up" data-t="5.1" data-d=".9" style="right:80px;top:540px;width:400px;height:640px;padding:84px 32px 28px"><div class="notch"></div>
 <div style="font:700 30px 'Inter Tight';letter-spacing:-.02em">Ihr Google-Profil</div>
 <div style="font:400 17px Inter;color:var(--muted);margin:4px 0 14px">Leistung · letzte 12 Monate</div>
 <div class="row"><span style="color:var(--muted)">Kosten</span><b class="gold" data-a="pop" data-t="7.1" data-buzz="7.25" style="font:800 36px 'Inter Tight';display:inline-block">CHF 0</b></div>
 <div class="row"><span style="color:var(--muted)">Anrufe</span><b>Monat für Monat</b></div>
 <div style="display:flex;align-items:flex-end;gap:12px;height:190px;margin-top:26px;border-bottom:2px solid rgba(255,255,255,.25)">{bars}</div>
 <div style="display:flex;justify-content:space-between;font:500 14px Inter;color:var(--dim);margin-top:8px"><span>M</span><span>J</span><span>J</span><span>A</span><span>S</span><span>O</span><span>N</span></div>
 <div style="font:400 13px Inter;color:var(--dim);margin-top:8px">Darstellung beispielhaft</div>
</div>
<div class="abs" data-a="rise" data-t="8.0" style="left:80px;top:1080px;width:500px">
 <div style="font:500 26px Inter;color:var(--muted)">Vielleicht lohnt sich Ihr Abo.</div>
 <div style="font:700 29px Inter;color:var(--gold);margin-top:6px">Nur blind zahlen sollten Sie nicht.</div></div>
{FOOT("Fiktive Darstellung", "Bertan Findik · digital-only.ch", 8.6)}''',
scene='''
const fl=[...document.querySelectorAll('.flick')], bs=[...document.querySelectorAll('.bar')];
window.SCENE=t=>{fl.forEach((e,i)=>{const a=2.3+i*.2;e.textContent=(t>a&&t<a+1.3)?String(Math.floor((Math.sin(t*41+i*7)+1)*4.99)):'?'});
 bs.forEach((b,i)=>{b.style.height=(+b.dataset.h*spring(R(t,6+i*.12,.8)))+'%'})};''')

# ---------- Seite Di: Website ist nicht der Grund ----------
SCENES["2026-11-17-di"] = dict(theme="theme-blue blue-t", grid=True, end=10, body=f'''
<div class="eyebrow" data-a="fade" data-t=".15" style="color:var(--blue)"><i></i>Google Maps</div>
<h1 data-words data-t=".35" style="font-size:68px">Ihre Website ist nicht der Grund, warum Sie auf <span class="blue">Google Maps fehlen.</span></h1>
<div class="abs" style="left:80px;top:560px;width:500px">
 {item("target", "Relevanz", "Hauptkategorie, Leistungen und Beschreibung im Google-Profil.", 1.9, "2.4")}
 {item("pin", "Entfernung", "Können Sie nicht ändern. Wer in Zug sucht, sieht zuerst Zug.", 2.6, "3.1")}
 {item("star", "Bekanntheit", "Bewertungen, Erwähnungen und ja, auch die Website.", 3.3, "3.8")}
</div>
<div class="abs card" data-a="right" data-t="1.3" style="right:80px;top:560px;width:390px;height:460px;overflow:hidden">
 <svg viewBox="0 0 390 460" style="position:absolute;inset:0"><g fill="none" stroke="rgba(142,157,255,.30)" stroke-width="7" stroke-linecap="round">
  <path d="M-20 300 C 90 280, 180 330, 410 250"/><path d="M110 -20 C 130 160, 120 300, 160 480"/><path d="M-20 120 C 120 140, 260 90, 410 130"/><path d="M290 -20 C 270 200, 300 330, 280 480"/></g>
  <g fill="rgba(255,255,255,.18)"><circle cx="60" cy="170" r="9"/><circle cx="330" cy="70" r="9"/><circle cx="320" cy="380" r="9"/><circle cx="70" cy="390" r="9"/></g></svg>
 {rings(95, 125, 200, 4.1, "rgba(142,157,255,.45)")}
 <svg class="abs" data-a="drop" data-t="3.9" data-buzz="4.15" viewBox="0 0 60 80" style="left:165px;top:150px;width:60px;height:80px;filter:drop-shadow(0 0 22px rgba(142,157,255,.9))"><path d="M30 78C30 78 4 48 4 28a26 26 0 0 1 52 0c0 20-26 50-26 50z" fill="#fff"/><circle cx="30" cy="28" r="9" fill="#5a68d8"/></svg>
 <div class="abs chip" data-a="pop" data-t="4.5" style="left:118px;top:250px;background:rgba(10,12,24,.85);border:1px solid rgba(142,157,255,.4)">Ihre Praxis</div>
</div>
<div class="abs card" data-a="rise" data-t="5.0" data-hover="1" style="right:118px;top:952px;width:330px;padding:16px 20px;opacity:.9">
 <div style="display:flex;gap:7px;margin-bottom:10px"><i style="width:11px;height:11px;border-radius:50%;background:#555;display:block"></i><i style="width:11px;height:11px;border-radius:50%;background:#555;display:block"></i><i style="width:11px;height:11px;border-radius:50%;background:#555;display:block"></i></div>
 <div style="font:600 21px Inter">Ihre Website</div><div style="font:400 17px Inter;color:var(--muted)">spielt mit, ist aber nur ein Teil</div></div>
<div class="abs card" data-a="rise" data-t="6.2" data-buzz="6.7" style="left:80px;right:80px;top:1086px;padding:24px 30px;display:flex;gap:28px;align-items:center">
 <div style="font:700 60px 'Inter Tight';letter-spacing:-.04em;color:var(--blue);white-space:nowrap">15 Min.</div>
 <div><div style="font:600 25px Inter">Profil-Check vor jeder neuen Website</div><div style="font:400 20px Inter;color:var(--muted)">Hauptkategorie, Leistungen, letzte Bewertung</div></div></div>
{FOOT("Faktoren laut Google-Hilfe · Beispiel", "digital-only.ch", 7.2)}''', scene='')

# ---------- Seite Mi: Um Bewertungen bitten ----------
stars = ''.join(f'<span class="star" data-tap="{5.6 + i * .28:.2f}" data-on="{5.6 + i * .28:.2f}" style="border-radius:50%;padding:0 3px">★</span>' for i in range(5))
SCENES["2026-11-18-mi"] = dict(theme="theme-gold", grid=False, end=11, body=f'''
<div class="eyebrow" data-a="fade" data-t=".15"><i></i>Google-Bewertungen</div>
<h1 data-words data-t=".35">Sie dürfen um eine <span class="gold">Bewertung bitten.</span></h1>
<div class="abs" style="left:80px;top:470px;width:480px">
 {item("qr", "QR-Code am Empfang", "Führt direkt zum Bewertungsformular.", 1.5, "1.95")}
 {item("chat", "Nach dem Termin fragen", "«Würden Sie das kurz auf Google schreiben?»", 2.1, "2.55")}
 {item("reply", "Jede Bewertung beantworten", "Innert 2 Tagen, auch die kritische.", 2.7, "3.15")}
</div>
<div class="abs card" data-a="rise" data-t="7.6" data-buzz="8.0" style="left:80px;top:905px;width:480px;padding:24px 28px;border-color:rgba(255,90,74,.4)">
 <div class="label" style="color:var(--red)">2 Grenzen</div>
 <div style="font:600 22px/1.35 Inter;margin-top:10px">Keine Gegenleistung, kein Rabatt, kein Geschenk.</div>
 <div style="font:600 22px/1.35 Inter;margin-top:6px">Nicht nur die Zufriedenen fragen.</div></div>
{rings(500, 520, 600, 3.9, "rgba(226,192,122,.28)")}
<div class="abs phone" data-a="up" data-t="3.4" data-d=".9" style="right:80px;top:470px;width:390px;height:660px;padding:80px 34px 28px;text-align:center"><div class="notch"></div>
 <div style="font:700 28px 'Inter Tight'">Ihr Feedback zählt</div>
 <div style="font:400 17px Inter;color:var(--muted);margin:4px 0 20px">Code scannen, Sterne wählen</div>
 <div style="position:relative;width:230px;height:230px;margin:0 auto;background:#fff;border-radius:22px;padding:16px;overflow:hidden"><canvas id="qr" width="198" height="198" style="width:198px;height:198px;display:block"></canvas><div id="scan" style="position:absolute;left:10px;right:10px;height:4px;border-radius:4px;background:var(--gold);box-shadow:0 0 18px var(--gold);top:20px;opacity:0"></div></div>
 <div style="margin:26px 0 18px;display:flex;justify-content:center;gap:2px">{stars}</div>
 <div class="chip" data-tap="7.15" style="justify-content:center;background:linear-gradient(180deg,#f0d394,#c39d5f);color:#1a1408;font-weight:700;padding:15px 30px">Bewertung senden</div>
</div>
<div class="abs" data-a="rise" data-t="8.7" style="left:80px;top:1150px;font:700 40px 'Inter Tight';letter-spacing:-.03em">Fragen ist erlaubt. <span class="gold">Kaufen nicht.</span></div>
{FOOT("Fiktives Beispiel", "digital-only.ch", 9.2)}''',
scene='''
(()=>{const c=document.getElementById('qr').getContext('2d');let s=7;const rnd=()=>(s=(s*16807)%2147483647)/2147483647;const n=25,k=198/n;c.fillStyle='#111';
 for(let y=0;y<n;y++)for(let x=0;x<n;x++){const f=(x<7&&y<7)||(x>=n-7&&y<7)||(x<7&&y>=n-7);if(!f&&rnd()>.52)c.fillRect(x*k,y*k,k+.3,k+.3)}
 [[0,0],[n-7,0],[0,n-7]].forEach(([a,b])=>{c.fillRect(a*k,b*k,7*k,7*k);c.fillStyle='#fff';c.fillRect((a+1)*k,(b+1)*k,5*k,5*k);c.fillStyle='#111';c.fillRect((a+2)*k,(b+2)*k,3*k,3*k)})})();
const sc=document.getElementById('scan'),st=[...document.querySelectorAll('.star')];
window.SCENE=t=>{const p=R(t,4.3,1.1);sc.style.opacity=p>0&&p<1?1:0;sc.style.top=(10+200*eo(p))+'px';
 st.forEach(e=>{e.classList.toggle('on',t>=+e.dataset.on)})};''')

# ---------- Seite Do: Dreimal anders ----------
def src_card(top, lab, val, t, bad):
    b = f' data-buzz="{t + .7}"' if bad else ''
    mark = '<span class="q abs" style="right:22px;top:22px">≠</span>' if bad else ''
    return f'<div class="abs card" data-a="left" data-t="{t}"{b} style="left:80px;top:{top}px;width:520px;padding:22px 28px">{mark}<div class="label">{lab}</div><div style="font:600 30px Inter;margin-top:8px;letter-spacing:-.01em">{val}</div></div>'
checks = ''.join(f'<div class="chip" data-a="pop" data-t="{7.2 + i * .35}" data-buzz="{7.35 + i * .35}" style="background:rgba(63,191,106,.10);border:1px solid rgba(63,191,106,.4)"><span style="color:var(--green);font-weight:800">✓</span>{x}</div>' for i, x in enumerate(["Name, Adresse, Telefon überall gleich", "Alte Einträge korrigieren", "Schema.org auf der Website"]))
SCENES["2026-11-19-do"] = dict(theme="theme-red", grid=False, end=11, body=f'''
<div class="eyebrow" data-a="fade" data-t=".15"><i></i>KI-Sichtbarkeit</div>
<h1 data-words data-t=".35">Dreimal im Netz, <span class="red">dreimal anders.</span></h1>
{src_card(470, "Website", "Bahnhofstrasse 12", 1.5, False)}
{src_card(612, "Google-Profil", 'Bahnhofstr. 12<span class="red">a</span>', 2.1, True)}
{src_card(754, "Altes Verzeichnis", 'Tel. von <span class="red">vor dem Umzug</span>', 2.7, True)}
<div class="abs card" data-a="right" data-t="3.6" style="right:80px;top:470px;width:360px;height:420px;padding:26px">
 <div style="display:flex;align-items:center;gap:10px;font:600 20px Inter"><i style="width:10px;height:10px;border-radius:50%;background:var(--blue);box-shadow:0 0 12px var(--blue);display:block"></i>KI-Assistent</div>
 <div data-a="pop" data-t="4.1" style="margin:22px 0 0 auto;width:fit-content;max-width:280px;background:#f2efe9;color:#141414;border-radius:18px 18px 4px 18px;padding:14px 18px;font:500 19px/1.35 Inter">Physio in Zug, wer hat heute offen?</div>
 <div data-a="pop" data-t="4.9" style="margin-top:16px;max-width:290px;background:rgba(255,255,255,.07);border:1px solid var(--line);border-radius:18px 18px 18px 4px;padding:14px 18px;font:500 19px/1.35 Inter;min-height:58px"><span id="dots" class="mono" style="letter-spacing:.2em">···</span><span id="ans" style="display:none">Zu diesem Betrieb finde ich <span class="red">widersprüchliche Angaben.</span></span></div>
 <div class="chip" data-a="pop" data-t="6.3" data-buzz="6.45" style="margin-top:22px;background:rgba(255,90,74,.12);border:1px solid rgba(255,90,74,.45);color:var(--red)">Unscharfes Bild</div></div>
<div class="abs card" data-a="rise" data-t="6.9" style="left:80px;right:80px;top:930px;padding:26px 30px">
 <div class="label" style="color:var(--gold)">Diese Woche prüfen</div>
 <div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:16px">{checks}</div></div>
<div class="abs" data-a="rise" data-t="8.6" style="left:80px;top:1150px;font:600 28px Inter;color:var(--muted)">Keine Garantie, dass eine KI Sie nennt. <span style="color:var(--ink)">Aber die Voraussetzung.</span></div>
{FOOT("Fiktive Darstellung", "digital-only.ch", 9.2)}''',
scene='''
const dots=document.getElementById('dots'),ans=document.getElementById('ans');
window.SCENE=t=>{const typing=t<5.9;dots.style.display=typing?'inline':'none';ans.style.display=typing?'none':'inline';
 dots.textContent=['·  ','·· ','···'][Math.floor(t*4)%3]};''')
