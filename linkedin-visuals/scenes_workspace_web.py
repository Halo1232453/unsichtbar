# Workspace-Kampagne im Stil der Website digital-only.ch: Weiss, Schwarz, Blau #0D3B8B,
# drehende Partikel-Kugel, dünne Linien mit blauem Punkt (Beacons), Pill-Buttons. Deutsch und Englisch.
from scenes import SCENES

L = {
 "de": dict(eye="Microsoft-365-Ausfall · 13. November 2026", h1="Outlook war weg.<br>Sie konnten nur zuschauen.", h1size=76,
            status="Dienststatus", rows=[("Outlook", "Offline"), ("Teams", "Gestört"), ("SharePoint", "Offline")],
            poll="Wechseln oder bleiben: Was ist sicherer?", o1="Bei Microsoft bleiben", o2="Zu Google wechseln", pnote="Ihre Antwort? In den Kommentaren.",
            illu="Illustration, keine echten Umfragewerte", body="Zweiter grosser Microsoft-365-Ausfall in diesem Jahr. Im Januar waren es fast 10 Stunden.",
            cta="Wechsel-Check buchen", link="Link im ersten Kommentar", src="Stand 13.11.2026 · Quellen: ORF, CNBC, The Register",
            today="Heute", goal="Ziel", items=["Postfächer", "Kalender", "Kontakte", "Dateien"], off="Offline", done="Übernommen",
            mig="Umzug", steps=["Check", "Plan", "Umzug", "Erster Montag"], tag="Seit Do 12.11., ca. 19 Uhr gestört", fict="Illustration"),
 "en": dict(eye="Microsoft 365 outage · 13 November 2026", h1="Outlook went down.<br>You could only watch.", h1size=86,
            status="Service status", rows=[("Outlook", "Offline"), ("Teams", "Degraded"), ("SharePoint", "Offline")],
            poll="Switch or stay: what's actually safer?", o1="Stay with Microsoft", o2="Switch to Google", pnote="Your answer? In the comments.",
            illu="Illustration, not real poll data", body="Second major Microsoft 365 outage this year. In January it took almost 10 hours.",
            cta="Book a switch check", link="Link in the first comment", src="As of 13 Nov 2026 · Sources: ORF, CNBC, The Register",
            today="Today", goal="Goal", items=["Mailboxes", "Calendars", "Contacts", "Files"], off="Offline", done="Moved",
            mig="Migration", steps=["Check", "Plan", "Move", "First Monday"], tag="Disrupted since Thu 12 Nov, ~7 pm CET", fict="Illustration"),
}
FT = {"seite": "digital-only.ch", "kyrill": "Kyrill Elsensohn · digital-only.ch"}
ARROW = '<svg viewBox="0 0 24 24" style="width:22px;height:22px;fill:none;stroke:#fff;stroke-width:2.4;stroke-linecap:round"><path d="M7 17L17 7M9 7h8v8"/></svg>'
CUR = ('<svg class="cursor" id="cur" viewBox="0 0 26 36" style="width:34px;height:46px"><path d="M2 2v28l7-7 5 11 5-2-5-11h10z" fill="#0a0a0c" stroke="#fff" stroke-width="2" stroke-linejoin="round"/></svg>'
       '<div class="click" id="clk" style="border-color:#0d3b8b"></div>')


def dot(x, y, t):
    r = ''.join('<div class="ring"></div>' for _ in range(3))
    return (f'<div class="wdot" data-a="pop" data-t="{t}" style="left:{x}px;top:{y}px;transform:translate(-50%,-50%)">'
            f'<div data-rings="{t}" style="position:absolute;inset:0">{r}</div><b></b></div>')


def lines(paths):
    ps = ''.join(f'<path class="draw" data-t="{t}" data-d="{d}" d="{p}"/>' for p, t, d in paths)
    return f'<svg class="abs" viewBox="0 0 1080 1350" style="left:0;top:0;width:1080px;height:1350px;pointer-events:none;z-index:7"><g fill="none" stroke="#b9bec7" stroke-width="2">{ps}</g></svg>'


def head(l):
    return f'''<canvas id="sph" class="abs" style="left:420px;top:330px;width:720px;height:720px"></canvas>
<div class="abs pill" data-a="pop" data-t=".2" style="right:80px;top:54px;font-size:18px;padding:13px 22px">{l["cta"]}</div>
<div class="eyebrow" data-a="fade" data-t=".35" style="top:180px">{l["eye"]}</div>
<h1 data-words data-t=".5" style="top:228px;font-size:{l.get("h1size",94)}px">{l["h1"]}</h1>'''


def cta_row(l, konto, extra=""):
    return f'''<div class="abs" data-a="rise" data-t="8.8" style="left:80px;top:1130px;display:flex;align-items:center;gap:30px">
 <div class="pill" id="cta" data-tap="9.7" data-buzz="9.72">{l["cta"]} {ARROW}</div>
 <span style="font:500 22px Inter;color:#0a0a0c;text-decoration:underline;text-underline-offset:6px">{l["link"]}</span></div>
<div class="foot" data-a="fade" data-t="9.9"><span>{l["src"]}{extra}</span><span>{FT[konto]}</span></div>'''


SHARED_JS = '''
const sph=document.getElementById('sph'),dpr=window.devicePixelRatio||1,SZ=720;sph.width=SZ*dpr;sph.height=SZ*dpr;const sc=sph.getContext('2d');sc.scale(dpr,dpr);
const PTS=[];let seed=11;const rnd=()=>(seed=(seed*16807)%2147483647)/2147483647;const N=2600,GA=Math.PI*(3-Math.sqrt(5));
for(let i=0;i<N;i++){const y=1-2*(i+.5)/N,r=Math.sqrt(1-y*y),th=GA*i;PTS.push([Math.cos(th)*r,y,Math.sin(th)*r,1+(rnd()-.5)*.09,rnd()<.16])}
function sphere(t){sc.clearRect(0,0,SZ,SZ);const a=t*.32,cx=SZ/2,cy=SZ/2,R=300*(.96+.04*eo(R2(t,0,1.6)));const ca=Math.cos(a),sa=Math.sin(a),tx=.38,ct=Math.cos(tx),st=Math.sin(tx);
 for(const p of PTS){let x=p[0]*ca+p[2]*sa,z=-p[0]*sa+p[2]*ca,y=p[1];const y2=y*ct-z*st,z2=y*st+z*ct;const d=(z2+1)/2,rr=R*p[3];
  sc.globalAlpha=(.12+.72*d)*cl(t/1.2);sc.fillStyle=p[4]?'#0d3b8b':'#0a0a0c';const s=.7+1.9*d;sc.fillRect(cx+x*rr-s/2,cy+y2*rr-s/2,s,s)}}
function R2(t,a,d){return cl((t-a)/d)}
const dr=[...document.querySelectorAll('.draw')];dr.forEach(p=>{p._L=p.getTotalLength();p.style.strokeDasharray=p._L});
const cur=document.getElementById('cur'),clk=document.getElementById('clk');
function pos(e){let x=0,y=0,n=e;while(n&&n.id!=='stage'){x+=n.offsetLeft;y+=n.offsetTop;n=n.offsetParent}return [x+e.offsetWidth/2,y+e.offsetHeight/2]}
function path(t){let a=K[0];for(let i=1;i<K.length;i++){const b=K[i];if(t<=b[0]){const p=(t-a[0])/(b[0]-a[0]),e=p<.5?4*p*p*p:1-Math.pow(-2*p+2,3)/2;return [a[1]+(b[1]-a[1])*e,a[2]+(b[2]-a[2])*e]}a=b}return [a[1],a[2]]}
function base(t){sphere(t);dr.forEach(p=>{p.style.strokeDashoffset=p._L*(1-eo(R2(t,+p.dataset.t,+p.dataset.d)))});
 const [x,y]=path(t);cur.style.left=x+'px';cur.style.top=y+'px';cur.style.opacity=t<K[0][0]?0:1;
 let ck=0,on=false;C.forEach(c=>{const k=t-c;if(k>=0&&k<.5){ck=k;on=true}});
 clk.style.opacity=on?String(1-ck/.5):'0';const s=10+70*ck;clk.style.width=clk.style.height=s+'px';clk.style.left=(x+3-s/2)+'px';clk.style.top=(y+3-s/2)+'px';
 cur.style.transform=on&&ck<.12?'scale(.86)':'scale(1)'}'''


# ---------- A: Ausfall + Umfrage ----------
def body_a(l, konto):
    rows = ''.join(f'<div class="row" data-a="fade" data-t="{2.0 + i * .35:.2f}" data-buzz="{2.1 + i * .35:.2f}" style="font:500 23px Inter;padding:17px 0;border-color:#eceef1">'
                   f'<span style="display:flex;align-items:center;gap:14px"><i style="width:12px;height:12px;border-radius:50%;border:2px solid #0a0a0c;display:block"></i>{n}</span>'
                   f'<span style="font:600 20px Inter;color:#8b919c;text-decoration:line-through">{s}</span></div>' for i, (n, s) in enumerate(l["rows"]))
    return f'''{head(l)}
{lines([("M44 128 L44 190 C 60 380, 200 470, 330 520", .9, 1.2), ("M840 420 C 960 470, 1000 560, 900 650", 5.4, .9), ("M80 1250 C 300 1300, 520 1260, 560 1190", 8.6, .9)])}
<div class="abs wcard" data-a="rise" data-t="1.4" style="left:80px;top:540px;width:470px;padding:28px 32px">
 <div style="font:500 18px Inter;color:#0d3b8b">{l["status"]}</div>
 <div style="font:700 30px 'Inter Tight';letter-spacing:-.03em;margin:4px 0 8px">outlook.office365.com</div>{rows}</div>
<div class="abs" data-a="rise" data-t="4.2" style="left:80px;top:900px;width:470px;font:400 25px/1.45 Inter;color:#0a0a0c">{l["body"]}</div>
<div class="abs wcard" data-a="up" data-t="5.6" data-d=".9" style="left:600px;top:660px;width:400px;padding:30px 30px">
 <div style="font:500 18px Inter;color:#0d3b8b">Poll</div>
 <div style="font:700 31px/1.08 'Inter Tight';letter-spacing:-.03em;margin:8px 0 22px">{l["poll"]}</div>
 <div class="opt" id="o1" data-tap="7.0" style="margin-bottom:12px"><div id="b1" style="position:absolute;inset:0 auto 0 0;width:0;background:rgba(10,10,12,.08)"></div><span style="position:relative">{l["o1"]}</span></div>
 <div class="opt" id="o2" data-tap="7.8" style="border-color:#0d3b8b"><div id="b2" style="position:absolute;inset:0 auto 0 0;width:0;background:rgba(13,59,139,.16)"></div><span style="position:relative;color:#0d3b8b">{l["o2"]}</span></div>
 <div style="margin-top:18px;font:500 18px Inter;color:#5b6270">{l["pnote"]}</div><div style="margin-top:4px;font:400 14px Inter;color:#9aa0aa">{l["illu"]}</div></div>
{dot(330, 520, 2.0)}{dot(900, 650, 6.2)}{dot(560, 1190, 9.4)}
{cta_row(l, konto)}{CUR}'''

JS_A = SHARED_JS + '''
let K=null,C=[7.0,7.8,9.7];
const b1=document.getElementById('b1'),b2=document.getElementById('b2');
window.SCENE=t=>{if(!K){const p1=pos(document.getElementById('o1')),p2=pos(document.getElementById('o2')),pc=pos(document.getElementById('cta'));K=[[6.4,1100,1340],[6.9,p1[0],p1[1]],[7.0,p1[0],p1[1]],[7.6,p2[0],p2[1]],[7.8,p2[0],p2[1]],[9.1,400,1260],[9.7,pc[0],pc[1]],[11,pc[0],pc[1]]]}base(t);const a=R(t,7.0,3.0),w=46+18*Math.sin(a*Math.PI*2.5)*Math.exp(-a*1.2);b1.style.width=(t<7?0:w)+'%';b2.style.width=(t<7.8?0:100-w-6)+'%'};'''


# ---------- B: Umzug ----------
def card(l, x, side, t):
    title = "Microsoft 365" if side == "l" else "Google Workspace"
    lab = l["today"] if side == "l" else l["goal"]
    rows = ''.join(f'<div class="row" style="font:500 22px Inter;padding:15px 0;border-color:#eceef1"><span>{n}</span>'
                   f'<span class="{side}s" style="font:600 18px Inter;color:{"#8b919c;text-decoration:line-through" if side == "l" else "#c3c8cf"}">{l["off"] if side == "l" else "—"}</span></div>' for n in l["items"])
    return (f'<div class="abs wcard" data-a="{"left" if side == "l" else "right"}" data-t="{t}" style="left:{x}px;top:470px;width:410px;padding:26px 30px 14px{";border-color:rgba(13,59,139,.35)" if side == "r" else ""}">'
            f'<div style="font:500 18px Inter;color:#0d3b8b">{lab}</div><div style="font:700 32px \'Inter Tight\';letter-spacing:-.03em;margin:4px 0 6px">{title}</div>{rows}</div>')


def body_b(l, konto):
    fly = ''.join('<div class="fly abs" style="width:18px;height:18px;border-radius:50%;background:#0d3b8b;box-shadow:0 0 0 5px rgba(13,59,139,.15),0 0 24px rgba(13,59,139,.6);opacity:0;z-index:9"></div>' for _ in l["items"])
    steps = ''.join(f'<span data-a="pop" data-t="{7.3 + i * .3:.1f}" data-buzz="{7.4 + i * .3:.1f}" style="border:1.5px solid #d9dde3;border-radius:999px;background:#fff;padding:11px 20px;font:600 19px Inter"><b style="color:#0d3b8b">0{i + 1}</b>&nbsp; {s}</span>' for i, s in enumerate(l["steps"]))
    return f'''{head(l)}
<div class="abs" data-a="pop" data-t="1.1" data-buzz="1.25" style="left:80px;top:410px;border:1.5px solid #0a0a0c;border-radius:999px;padding:8px 16px;font:600 17px Inter;background:#fff">● {l["tag"]}</div>
{card(l, 80, "l", 1.5)}{card(l, 590, "r", 2.3)}{fly}
<div class="abs wcard" data-a="rise" data-t="3.0" style="left:80px;right:80px;top:850px;padding:24px 30px">
 <div style="display:flex;justify-content:space-between;font:500 19px Inter"><span style="color:#0d3b8b">{l["mig"]}</span><span id="pct" style="font-weight:700">0 %</span></div>
 <div style="position:relative;height:2px;background:#e3e3e3;margin:18px 0 22px"><div id="bar" style="position:absolute;left:0;top:0;height:2px;width:0;background:#0d3b8b"></div><i id="bhd" style="position:absolute;top:-9px;left:0;width:20px;height:20px;margin-left:-10px;border-radius:50%;background:#0d3b8b;box-shadow:0 0 0 5px #fff,0 0 0 6.5px rgba(13,59,139,.35);display:block"></i></div>
 <div style="display:flex;flex-wrap:wrap;gap:10px">{steps}</div></div>
{lines([("M80 1250 C 300 1300, 520 1260, 560 1190", 8.6, .9)])}
{dot(490, 470, 1.6)}{dot(1000, 470, 6.8)}{dot(560, 1190, 9.4)}
{cta_row(l, konto, " · " + l["fict"])}{CUR}'''

JS_B = SHARED_JS + '''
let K=null,C=[9.7],RY=null;
const fl=[...document.querySelectorAll('.fly')],rs=[...document.querySelectorAll('.rs')],ls=[...document.querySelectorAll('.ls')],bar=document.getElementById('bar'),bhd=document.getElementById('bhd'),pc=document.getElementById('pct');
window.SCENE=t=>{if(!K){const pc=pos(document.getElementById('cta'));K=[[8.8,1100,1340],[9.6,pc[0],pc[1]],[9.7,pc[0],pc[1]],[11,pc[0],pc[1]]];RY=rs.map((r,i)=>[pos(ls[i])[0]+40,pos(r)[0]-30,pos(r)[1]])}
 base(t);fl.forEach((e,i)=>{const t0=3.9+i*.7,p=R(t,t0,.65),q=1-Math.pow(1-p,3),y0=RY[i][2];
  const x=RY[i][0]+(RY[i][1]-RY[i][0])*q,y=y0-Math.sin(q*Math.PI)*100;e.style.left=(x-9)+'px';e.style.top=(y-9)+'px';e.style.opacity=p>0&&p<1?1:0;
  const d=t>=t0+.65;rs[i].textContent=d?'✓ DONE':'—';rs[i].style.color=d?'#0d3b8b':'#c3c8cf';ls[i].style.opacity=t>=t0?'.35':'1'});
 const p=eo(R(t,3.9,2.9));bar.style.width=(p*100)+'%';bhd.style.left=(p*100)+'%';pc.textContent=Math.round(p*100)+' %'};'''

for lang in ("de", "en"):
    l = L[lang]
    jb = JS_B.replace("'✓ DONE'", "'✓ " + l["done"] + "'")
    for konto, suf in (("seite", ""), ("kyrill", "-kyrill")):
        SCENES[f"web-workspace-a{suf}-{lang}"] = dict(theme="theme-web", grid=False, end=11, body=body_a(l, konto), scene=JS_A)
        SCENES[f"web-workspace-b{suf}-{lang}"] = dict(theme="theme-web", grid=False, end=11, body=body_b(l, konto), scene=jb)
