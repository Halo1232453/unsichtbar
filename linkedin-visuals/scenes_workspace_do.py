# Workspace-Kampagne im digitalONLY-Editorial-Stil (Papier, Schwarz, Mono, Rot), englisch.
# A «Outage»: Terminal + Umfrage. B «Migration»: Umzug von Microsoft 365 zu Google Workspace.
# Beacons und ein klickender Pixel-Cursor führen den Blick.
from scenes import SCENES

FT = {"seite": "DIGITAL-ONLY.CH", "kyrill": "KYRILL ELSENSOHN · DIGITAL-ONLY.CH"}
HOOK = 'Outlook went down last night. <span class="red">You could only watch.</span>'
CUR = ('<svg class="cursor" id="cur" viewBox="0 0 16 20" shape-rendering="crispEdges"><path fill="#0b0b0b" stroke="#fff" stroke-width="1" '
       'd="M1 1h2v1h1v1h1v1h1v1h1v1h1v1h1v1h1v1h1v1h1v2H9v1h1v2h1v2H9v1H8v-2H7v-2H6v-1H5v1H4v1H3v1H1z"/></svg><div class="click" id="clk"></div>')


def bcn(x, y, n, t):
    rings = ''.join('<div class="ring"></div>' for _ in range(3))
    return (f'<div class="bcn" data-a="pop" data-t="{t}" style="left:{x}px;top:{y}px;transform:translate(-50%,-50%)">'
            f'<div data-rings="{t}" style="position:absolute;inset:0">{rings}</div><b>{n}</b></div>')


def head(live):
    return f'''<div class="abs" data-a="pop" data-t=".2" style="right:80px;top:70px;background:#0b0b0b;color:#fff;font:700 16px 'JetBrains Mono';letter-spacing:.16em;padding:12px 18px;display:flex;align-items:center;gap:10px"><i id="live" style="width:10px;height:10px;background:var(--red);display:block"></i>{live}</div>
<div class="rule" data-a="fade" data-t=".3"></div>
<div class="eyebrow" data-a="fade" data-t=".4" style="top:172px"><i></i>// MICROSOFT 365 OUTAGE</div>
<h1 data-words data-t=".5" style="top:214px;font-size:62px">{HOOK}</h1>'''


def band(t):
    return f'''<div class="abs" data-a="rise" data-t="{t}" style="left:0;right:0;top:1090px;height:160px;background:#0b0b0b;padding:30px 80px;display:flex;align-items:center;justify-content:space-between;gap:24px">
 <div style="color:#fff;font:800 40px/1.05 Jost;letter-spacing:-.02em">We'll move you to<br>Google Workspace.</div>
 <div id="cta" data-tap="9.7" data-buzz="9.72" style="flex:none;background:var(--red);color:#fff;font:700 18px 'JetBrains Mono';letter-spacing:.06em;padding:18px 22px;text-transform:uppercase">■ Switch check →</div></div>'''


def foot(konto, extra=""):
    return f'<div class="foot" data-a="fade" data-t="9.9" style="bottom:42px"><span>// As of 13 Nov 2026 · ORF, CNBC, The Register{extra}</span><span>{FT[konto]}</span></div>'


TYPE_JS = '''const typ=[...document.querySelectorAll('[data-typ]')];typ.forEach(e=>{e._full=e.textContent;e.textContent=''});
const cur=document.getElementById('cur'),clk=document.getElementById('clk'),live=document.getElementById('live');
function path(t){let a=K[0];for(let i=1;i<K.length;i++){const b=K[i];if(t<=b[0]){const p=(t-a[0])/(b[0]-a[0]),e=p<.5?4*p*p*p:1-Math.pow(-2*p+2,3)/2;return [a[1]+(b[1]-a[1])*e,a[2]+(b[2]-a[2])*e]}a=b}return [a[1],a[2]]}
function base(t){typ.forEach(e=>{const t0=+e.dataset.typ,n=Math.round(e._full.length*R(t,t0,+e.dataset.dur||.8));e.textContent=e._full.slice(0,n)});
 const [x,y]=path(t);cur.style.left=x+'px';cur.style.top=y+'px';cur.style.opacity=t<K[0][0]?0:1;
 let ck=0;C.forEach(c=>{const k=t-c;if(k>=0&&k<.5)ck=k});const on=C.some(c=>t-c>=0&&t-c<.5);
 clk.style.opacity=on?String(1-ck/.5):'0';const s=10+70*ck;clk.style.width=clk.style.height=s+'px';clk.style.left=(x+2-s/2)+'px';clk.style.top=(y+2-s/2)+'px';
 cur.style.transform=on&&ck<.12?'scale(.86)':'scale(1)';live.style.opacity=(Math.floor(t*2)%2)?'.25':'1'}'''


# ---------- A: Outage + Poll ----------
def body_a(konto):
    lines = [("> ping outlook.office365.com", 1.6, ""), ("  request timed out", 2.4, "color:var(--red)"), ("> teams --status", 3.0, ""),
             ("  degraded", 3.7, "color:var(--red)"), ("> since thu 12 nov ~19:00 cet", 4.1, ""), ("> jan 2026: ~10 h outage", 4.8, "color:#a3a097")]
    term = ''.join(f'<div data-typ="{t}" data-dur=".6" style="white-space:pre;{st}">{s}</div>' for s, t, st in lines)
    return f'''{head("LIVE · 13 NOV 2026")}
<div class="abs term" data-a="left" data-t="1.2" data-buzz="2.45,3.75" style="left:80px;top:440px;width:540px;height:330px;padding:28px 30px;font-size:22px;line-height:1.75;box-shadow:12px 12px 0 rgba(229,50,31,.9)">
 <div style="display:flex;gap:8px;margin-bottom:10px"><i style="width:12px;height:12px;background:#e5321f;display:block"></i><i style="width:12px;height:12px;background:#555;display:block"></i><i style="width:12px;height:12px;background:#555;display:block"></i></div>{term}</div>
<div class="abs" style="left:80px;top:820px;display:flex;flex-wrap:wrap;gap:12px;width:560px">
 <span class="sq" data-a="pop" data-t="5.2" data-buzz="5.3" style="text-decoration:line-through;text-decoration-color:var(--red);text-decoration-thickness:3px">■ Outlook</span>
 <span class="sq" data-a="pop" data-t="5.45" data-buzz="5.55" style="text-decoration:line-through;text-decoration-color:var(--red);text-decoration-thickness:3px">■ Teams</span>
 <span class="sq" data-a="pop" data-t="5.7" data-buzz="5.8" style="text-decoration:line-through;text-decoration-color:var(--red);text-decoration-thickness:3px">■ SharePoint</span>
 <span class="sq" data-a="pop" data-t="5.95" style="border-color:var(--red);color:var(--red)">Worldwide</span></div>
<div class="abs phone" data-a="up" data-t="5.6" data-d=".9" style="right:80px;top:420px;width:370px;height:620px;padding:86px 28px 26px"><div class="notch"></div>
 <div style="font:700 15px 'JetBrains Mono';letter-spacing:.2em;color:#a3a097">// POLL</div>
 <div style="font:800 32px/1.1 Jost;margin:12px 0 26px">Switch or stay: what's actually safer?</div>
 <div id="o1" data-tap="7.0" style="position:relative;overflow:hidden;border:2px solid #f4f2ee;padding:16px 18px;margin-bottom:14px;font:700 19px 'JetBrains Mono'"><div id="b1" style="position:absolute;inset:0 auto 0 0;width:0;background:rgba(255,255,255,.22)"></div><span style="position:relative">STAY · MICROSOFT</span></div>
 <div id="o2" data-tap="7.8" style="position:relative;overflow:hidden;border:2px solid var(--red);padding:16px 18px;font:700 19px 'JetBrains Mono'"><div id="b2" style="position:absolute;inset:0 auto 0 0;width:0;background:rgba(229,50,31,.45)"></div><span style="position:relative">SWITCH · GOOGLE</span></div>
 <div data-a="fade" data-t="8.4" style="margin-top:24px;font:500 18px/1.4 Inter;color:#a3a097">Your answer? In the comments.</div>
 <div data-a="fade" data-t="8.4" style="margin-top:8px;font:400 13px Inter;color:#77746d">Illustration, not real poll data</div></div>
{bcn(605, 520, 1, 2.5)}{bcn(1000, 425, 2, 6.6)}{bcn(1000, 1170, 3, 9.3)}
{band(8.9)}{foot(konto)}{CUR}'''

JS_A = TYPE_JS + '''
const K=[[6.2,1100,1300],[6.9,820,703],[7.0,820,703],[7.6,820,778],[7.8,820,778],[9.1,900,1250],[9.7,880,1170],[11,880,1170]],C=[7.0,7.8,9.7];
const b1=document.getElementById('b1'),b2=document.getElementById('b2');
window.SCENE=t=>{base(t);const a=R(t,7.0,3.0),w=46+18*Math.sin(a*Math.PI*2.5)*Math.exp(-a*1.2);b1.style.width=(t<7?0:w)+'%';b2.style.width=(t<7.8?0:100-w-6)+'%'};'''


# ---------- B: Migration ----------
ITEMS = ["Mailboxes", "Calendars", "Contacts", "Files"]


def card(x, label, title, side, t):
    rows = ''.join(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:13px 0;border-top:2px solid #0b0b0b;font:700 19px \'JetBrains Mono\';text-transform:uppercase">'
                   f'<span>■ {n}</span><span class="{side}s" style="{"color:var(--red)" if side == "l" else "color:#bbb"}">{"OFFLINE" if side == "l" else "—"}</span></div>' for n in ITEMS)
    return (f'<div class="abs box" data-a="{"left" if side == "l" else "right"}" data-t="{t}" style="left:{x}px;top:450px;width:410px;padding:24px 26px 12px">'
            f'<div style="font:700 15px \'JetBrains Mono\';letter-spacing:.2em;color:{"var(--red)" if side == "l" else "#0b0b0b"}">{label}</div>'
            f'<div style="font:800 36px Jost;letter-spacing:-.02em;margin:6px 0 14px">{title}</div>{rows}</div>')


def body_b(konto):
    fly = ''.join(f'<div class="fly abs" style="width:34px;height:34px;background:#0b0b0b;box-shadow:4px 4px 0 var(--red);opacity:0"></div>' for _ in ITEMS)
    steps = ''.join(f'<span class="sq" data-a="pop" data-t="{7.4 + i * .3:.1f}" data-buzz="{7.5 + i * .3:.1f}">■ 0{i + 1} {s}</span>' for i, s in enumerate(["Check", "Plan", "Move", "First Monday"]))
    return f'''{head("LIVE · 13 NOV 2026")}
<div class="abs sq" data-a="pop" data-t="1.1" data-buzz="1.25" style="left:80px;top:384px;border-color:var(--red);color:var(--red);font-size:15px;padding:6px 12px">● Disrupted since Thu 12 Nov ~19:00 CET</div>
{card(80, "// TODAY", "Microsoft 365", "l", 1.5)}{card(590, "// GOAL", "Google Workspace", "r", 2.3)}
{fly}
<div class="abs term" data-a="rise" data-t="3.0" style="left:80px;right:80px;top:850px;padding:22px 28px;font-size:21px;box-shadow:12px 12px 0 rgba(229,50,31,.9)">
 <div data-typ="3.2" data-dur=".7" style="white-space:pre">&gt; migrate --from microsoft365 --to google-workspace</div>
 <div style="display:flex;align-items:center;gap:16px;margin-top:14px"><div style="flex:1;height:16px;background:#2a2a2a"><div id="bar" style="height:100%;width:0;background:#f4f2ee;box-shadow:inset -8px 0 0 var(--red)"></div></div><span id="pct" style="width:70px;text-align:right">0%</span></div></div>
<div class="abs" style="left:80px;right:80px;top:1010px;display:flex;flex-wrap:wrap;gap:10px">{steps}</div>
{bcn(480, 452, 1, 1.6)}{bcn(990, 452, 2, 7.0)}{bcn(1000, 1170, 3, 9.3)}
{band(8.9)}{foot(konto, " · Illustration")}{CUR}'''

JS_B = TYPE_JS + '''
const fl=[...document.querySelectorAll('.fly')],rs=[...document.querySelectorAll('.rs')],ls=[...document.querySelectorAll('.ls')],bar=document.getElementById('bar'),pc=document.getElementById('pct');
const K=[[8.8,1100,1300],[9.6,880,1170],[9.7,880,1170],[11,880,1170]],C=[9.7];
window.SCENE=t=>{base(t);fl.forEach((e,i)=>{const t0=3.9+i*.7,p=R(t,t0,.65),q=1-Math.pow(1-p,3),y0=588+i*58;
  const x=400+(880-400)*q,y=y0-Math.sin(q*Math.PI)*110;e.style.left=x+'px';e.style.top=y+'px';e.style.opacity=p>0&&p<1?1:0;e.style.transform='rotate('+(q*180)+'deg)';
  const d=t>=t0+.65;rs[i].textContent=d?'■ DONE':'—';rs[i].style.color=d?'#0b0b0b':'#bbb';ls[i].style.opacity=t>=t0?'.3':'1'});
 const p=eo(R(t,3.9,2.9));bar.style.width=(p*100)+'%';pc.textContent=Math.round(p*100)+'%'};'''

for konto, suf in (("seite", ""), ("kyrill", "-kyrill")):
    SCENES[f"do-workspace-a{suf}-en"] = dict(theme="theme-do", grid=False, end=11, body=body_a(konto), scene=JS_A)
    SCENES[f"do-workspace-b{suf}-en"] = dict(theme="theme-do", grid=False, end=11, body=body_b(konto), scene=JS_B)
