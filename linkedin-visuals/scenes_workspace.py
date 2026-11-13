# Microsoft-365-Ausfall vom 12./13. November 2026: je zwei Videos (A «Ausfall», B «Umzug»)
# für die Seite und für Kyrill, gleicher Hook, gleiche Botschaft.
from scenes import SCENES, rings, FOOT
from scenes_kw46 import FT

HOOK = 'Gestern war Outlook weg. <span class="red">Sie konnten nur zuschauen.</span>'
SRC = "Stand 13.11.2026 · Quellen: ORF, CNBC, The Register"
RED = 'background:rgba(255,90,74,.10);border:1px solid rgba(255,90,74,.42);color:var(--red)'
CTA = ('<div class="abs" data-a="rise" data-t="{t}" style="left:80px;right:80px;top:1140px;display:flex;flex-wrap:wrap;gap:18px;align-items:center;justify-content:space-between">'
       '<div style="font:700 36px \'Inter Tight\';letter-spacing:-.03em">Wir holen Sie rüber zu <span class="gold">Google Workspace.</span></div>'
       '<div class="chip" data-a="pop" data-t="{t2}" data-buzz="{t3}" data-tap="{t3}" style="background:linear-gradient(180deg,#f0d394,#c39d5f);color:#1a1408;font-weight:700;padding:13px 22px">Wechsel-Check · Link im Kommentar</div></div>')


def head():
    return f'<div class="eyebrow" data-a="fade" data-t=".15"><i></i>Microsoft-365-Ausfall</div>\n<h1 data-words data-t=".35">{HOOK}</h1>'


# ---------- Video A: Ausfall ----------
def body_a(konto):
    rows = ''.join(f'<div style="display:flex;gap:14px;align-items:center;padding:14px 0;border-bottom:1px solid var(--line)"><i style="width:38px;height:38px;border-radius:50%;background:rgba(255,255,255,.08);display:block;flex:none"></i><div style="flex:1"><div style="height:11px;width:{w1}%;border-radius:6px;background:rgba(255,255,255,.16)"></div><div style="height:10px;width:{w2}%;border-radius:6px;background:rgba(255,255,255,.09);margin-top:8px"></div></div></div>' for w1, w2 in [(62, 88), (48, 74), (70, 60)])
    tl = ''.join(f'<div class="chip" data-a="pop" data-t="{t}" data-buzz="{t + .1}" style="{st};padding:8px 14px;font-size:17px">{x}</div>' for x, st, t in [
        ("Do 12.11. ab ca. 19 Uhr: Outlook, Teams, SharePoint", RED, 4.4),
        ("Fr 13.11.: Störung dauert an", RED, 4.8),
        ("Januar: schon einmal, fast 10 Stunden", 'background:rgba(255,255,255,.06);border:1px solid var(--line);color:var(--muted)', 5.2)])
    return f'''{head()}
<div class="abs card" data-a="left" data-t="1.5" data-buzz="3.6" style="left:80px;top:470px;width:500px;padding:26px 28px">
 <div style="display:flex;align-items:center;justify-content:space-between"><span style="font:700 26px 'Inter Tight'">Posteingang</span>
  <span id="spin" style="width:30px;height:30px;border-radius:50%;border:3px solid rgba(255,255,255,.15);border-top-color:var(--ink);display:block"></span></div>
 <div id="mst" style="margin-top:12px;font:500 18px Inter;color:var(--muted)">Verbindung wird hergestellt …</div>{rows}</div>
<div class="abs" style="left:80px;top:850px;width:520px;display:flex;flex-direction:column;gap:10px;align-items:flex-start">{tl}</div>
{rings(520, 500, 560, 6.0)}
<div class="abs phone" data-a="up" data-t="5.6" data-d=".9" style="right:80px;top:460px;width:380px;height:600px;padding:84px 28px 26px"><div class="notch"></div>
 <div class="label" style="color:var(--gold)">Umfrage</div>
 <div style="font:700 28px/1.2 'Inter Tight';margin:10px 0 24px">Würden Sie Microsoft 365 nochmals wählen?</div>
 <div data-tap="6.8" style="padding:16px 18px;border-radius:16px;border:1px solid var(--line);margin-bottom:14px;position:relative;overflow:hidden"><div id="b1" style="position:absolute;inset:0 auto 0 0;width:0;background:rgba(63,191,106,.18)"></div><div style="position:relative;font:600 21px Inter">Ja, klar</div></div>
 <div data-tap="7.4" style="padding:16px 18px;border-radius:16px;border:1px solid var(--line);position:relative;overflow:hidden"><div id="b2" style="position:absolute;inset:0 auto 0 0;width:0;background:rgba(255,90,74,.20)"></div><div style="position:relative;font:600 21px Inter">Nein, nie mehr</div></div>
 <div data-a="fade" data-t="8.2" style="margin-top:24px;font:500 18px/1.4 Inter;color:var(--muted)">Ihre Antwort? In den Kommentaren.</div>
 <div data-a="fade" data-t="8.2" style="margin-top:10px;font:400 14px Inter;color:var(--dim)">Illustration, keine echten Umfragewerte</div></div>
{CTA.format(t=8.8, t2=9.4, t3=9.6)}{FOOT(SRC, FT[konto], 9.8)}'''

JS_A = '''const sp=document.getElementById('spin'),ms=document.getElementById('mst'),b1=document.getElementById('b1'),b2=document.getElementById('b2');
window.SCENE=t=>{const off=t>=3.5;sp.style.transform='rotate('+(t*380)+'deg)';sp.style.borderTopColor=off?'var(--red)':'var(--ink)';sp.style.opacity=off?(.5+.5*Math.abs(Math.sin(t*4))):1;
 ms.textContent=off?'Keine Verbindung zum Server':'Verbindung wird hergestellt …';ms.style.color=off?'var(--red)':'';
 const a=R(t,6.8,3.0),w=46+18*Math.sin(a*Math.PI*2.5)*Math.exp(-a*1.2);b1.style.width=(t<6.8?0:w)+'%';b2.style.width=(t<7.4?0:100-w-8)+'%'};'''


# ---------- Video B: Umzug ----------
ITEMS = [("Postfächer", "@"), ("Kalender", "31"), ("Kontakte", "☺"), ("Dateien", "▤")]


def box(side, title, sub, t, extra=""):
    pos = "left:80px" if side == "l" else "right:80px"
    items = ''.join(f'<div class="row" style="font:600 21px Inter;padding:15px 0"><span style="display:flex;gap:12px;align-items:center"><span style="width:36px;height:36px;border-radius:10px;display:grid;place-items:center;background:rgba(255,255,255,.06);font-size:16px">{ic}</span>{n}</span>'
                    + (f'<span class="{side}st" data-i="{i}" style="font:700 18px Inter;color:var(--dim)">–</span>' if side == "r" else f'<span class="lst" data-i="{i}" style="font:700 16px Inter;color:var(--red)">offline</span>') + '</div>'
                    for i, (n, ic) in enumerate(ITEMS))
    return (f'<div class="abs card" data-a="{"left" if side == "l" else "right"}" data-t="{t}" {extra} style="{pos};top:480px;width:420px;padding:24px 26px{";border-color:rgba(226,192,122,.5);box-shadow:0 0 60px rgba(226,192,122,.16)" if side == "r" else ""}">'
            f'<div class="label" style="color:{"var(--gold)" if side == "r" else "var(--red)"}">{sub}</div><div style="font:700 30px \'Inter Tight\';margin:6px 0 8px">{title}</div>{items}</div>')


def body_b(konto):
    fly = ''.join(f'<div class="fly abs" data-i="{i}" style="left:0;top:0;width:58px;height:58px;border-radius:16px;display:grid;place-items:center;background:linear-gradient(180deg,#f0d394,#c39d5f);color:#1a1408;font:700 20px Inter;box-shadow:0 0 30px rgba(226,192,122,.7);opacity:0">{ic}</div>' for i, (n, ic) in enumerate(ITEMS))
    steps = ''.join(f'<div class="chip" data-a="pop" data-t="{7.6 + i * .3:.1f}" data-buzz="{7.7 + i * .3:.1f}" style="background:rgba(226,192,122,.10);border:1px solid rgba(226,192,122,.45)"><b style="color:var(--gold)">{i + 1}</b>{s}</div>' for i, s in enumerate(["Wechsel-Check", "Plan", "Umzug", "Erster Montag"]))
    return f'''{head()}
<div class="abs chip" data-a="pop" data-t="1.3" data-buzz="1.5,2.6" style="left:80px;top:420px;{RED};padding:6px 14px;font-size:16px">● Seit Do 12.11., ca. 19 Uhr gestört</div>
{box("l", "Microsoft 365", "Heute", 1.6, 'data-buzz="2.2"')}
{box("r", "Google Workspace", "Ziel", 2.6)}
{fly}
<div class="abs card" data-a="rise" data-t="3.2" style="left:80px;right:80px;top:880px;padding:22px 26px">
 <div style="display:flex;justify-content:space-between;font:600 18px Inter;color:var(--muted)"><span>Umzug</span><span id="pct" class="mono" style="color:var(--gold)">0 %</span></div>
 <div style="height:12px;border-radius:6px;background:rgba(255,255,255,.08);margin-top:12px;overflow:hidden"><div id="bar" style="height:100%;width:0;background:linear-gradient(90deg,#c39d5f,#f0d394);box-shadow:0 0 20px rgba(226,192,122,.6)"></div></div>
 <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:18px">{steps}</div></div>
{CTA.format(t=8.9, t2=9.4, t3=9.6)}{FOOT(SRC + " · Fiktive Darstellung", FT[konto], 9.8)}'''

JS_B = '''const fl=[...document.querySelectorAll('.fly')],rs=[...document.querySelectorAll('.rst')],ls=[...document.querySelectorAll('.lst')],bar=document.getElementById('bar'),pc=document.getElementById('pct');
const L=[[372,600],[372,668],[372,736],[372,804]],Rr=[[650,600],[650,668],[650,736],[650,804]];
window.SCENE=t=>{fl.forEach((e,i)=>{const t0=3.8+i*.75,p=R(t,t0,.7),q=1-Math.pow(1-p,3);const x=L[i][0]+(Rr[i][0]-L[i][0])*q,y=L[i][1]+(Rr[i][1]-L[i][1])*q-Math.sin(q*Math.PI)*120;
  e.style.left=x+'px';e.style.top=y+'px';e.style.opacity=p>0&&p<1?1:0;e.style.transform='scale('+(.7+.5*Math.sin(q*Math.PI))+') rotate('+(q*20-10)+'deg)';
  const done=t>=t0+.7;rs[i].textContent=done?'✓':'–';rs[i].style.color=done?'var(--green)':'var(--dim)';rs[i].style.fontSize=done?'24px':'18px';
  ls[i].style.opacity=t>=t0?'.35':'1'});
 const p=R(t,3.8,3.0);bar.style.width=(eo(p)*100)+'%';pc.textContent=Math.round(eo(p)*100)+' %'};'''

for konto, suf in (("seite", ""), ("kyrill", "-kyrill")):
    SCENES[f"2026-11-13-fr-workspace{suf}"] = dict(theme="theme-red", grid=False, end=11, body=body_a(konto), scene=JS_A)
    SCENES[f"2026-11-13-fr-workspace-b{suf}"] = dict(theme="theme-gold", grid=False, end=11, body=body_b(konto), scene=JS_B)
