# Motiv zum Microsoft-365-Ausfall vom 12./13. November 2026: Seite und Kyrill.
from scenes import SCENES, rings, FOOT
from scenes_kw46 import FT

def body(konto):
    rows = ''.join(f'<div style="display:flex;gap:14px;align-items:center;padding:14px 0;border-bottom:1px solid var(--line)"><i style="width:38px;height:38px;border-radius:50%;background:rgba(255,255,255,.08);display:block;flex:none"></i><div style="flex:1"><div style="height:11px;width:{w1}%;border-radius:6px;background:rgba(255,255,255,.16)"></div><div style="height:10px;width:{w2}%;border-radius:6px;background:rgba(255,255,255,.09);margin-top:8px"></div></div></div>' for w1, w2 in [(62, 88), (48, 74), (70, 60)])
    tl = ''.join(f'<div class="chip" data-a="pop" data-t="{t}" data-buzz="{t + .1}" style="{st};padding:8px 14px;font-size:17px">{x}</div>' for x, st, t in [
        ("Do 12.11. ab ca. 19 Uhr: Outlook, Teams, SharePoint", 'background:rgba(255,90,74,.10);border:1px solid rgba(255,90,74,.42);color:var(--red)', 4.6),
        ("Fr 13.11.: Störung dauert an", 'background:rgba(255,90,74,.10);border:1px solid rgba(255,90,74,.42);color:var(--red)', 5.0),
        ("Januar: schon einmal, fast 10 Stunden", 'background:rgba(255,255,255,.06);border:1px solid var(--line);color:var(--muted)', 5.4)])
    mail = f'''<div class="abs card" data-a="left" data-t="1.5" data-buzz="3.6" style="left:80px;top:470px;width:500px;padding:26px 28px">
 <div style="display:flex;align-items:center;justify-content:space-between"><span style="font:700 26px 'Inter Tight'">Posteingang</span>
  <span id="spin" style="width:30px;height:30px;border-radius:50%;border:3px solid rgba(255,255,255,.15);border-top-color:var(--ink);display:block"></span></span></div>
 <div id="mst" style="margin-top:12px;font:500 18px Inter;color:var(--muted)">Verbindung wird hergestellt …</div>{rows}</div>
<div class="abs" style="left:80px;top:850px;width:520px;display:flex;flex-direction:column;gap:10px;align-items:flex-start">{tl}</div>'''
    poll = f'''{rings(520, 520, 560, 6.2)}
<div class="abs phone" data-a="up" data-t="5.8" data-d=".9" style="right:80px;top:470px;width:380px;height:620px;padding:84px 28px 26px"><div class="notch"></div>
 <div class="label" style="color:var(--gold)">Umfrage</div>
 <div style="font:700 28px/1.2 'Inter Tight';margin:10px 0 24px">Würden Sie Microsoft 365 nochmals wählen?</div>
 <div data-tap="7.0" style="padding:16px 18px;border-radius:16px;border:1px solid var(--line);margin-bottom:14px;position:relative;overflow:hidden"><div id="b1" style="position:absolute;inset:0 auto 0 0;width:0;background:rgba(63,191,106,.18)"></div><div style="position:relative;font:600 21px Inter">Ja, klar</div></div>
 <div data-tap="7.6" style="padding:16px 18px;border-radius:16px;border:1px solid var(--line);position:relative;overflow:hidden"><div id="b2" style="position:absolute;inset:0 auto 0 0;width:0;background:rgba(255,90,74,.20)"></div><div style="position:relative;font:600 21px Inter">Nein, nie mehr</div></div>
 <div data-a="fade" data-t="8.6" style="margin-top:26px;font:500 18px/1.4 Inter;color:var(--muted)">Ihre Antwort? In den Kommentaren.</div>
 <div data-a="fade" data-t="8.6" style="margin-top:10px;font:400 14px Inter;color:var(--dim)">Illustration, keine echten Umfragewerte</div></div>'''
    bottom = f'<div class="abs" data-a="rise" data-t="9.2" style="left:80px;right:80px;top:1150px;font:700 36px \'Inter Tight\';letter-spacing:-.03em">Auch Google fällt mal aus. <span class="gold">Aber passt Ihr Werkzeug noch?</span></div>'
    return f'''
<div class="eyebrow" data-a="fade" data-t=".15"><i></i>Microsoft-365-Ausfall</div>
<h1 data-words data-t=".35">Würden Sie Microsoft 365 <span class="red">heute nochmals wählen?</span></h1>
{mail}{poll}{bottom}{FOOT("Stand 13.11.2026 · Quellen: ORF, CNBC, The Register", FT[konto], 9.6)}'''

SCENE_JS = '''const sp=document.getElementById('spin'),ms=document.getElementById('mst'),b1=document.getElementById('b1'),b2=document.getElementById('b2');
window.SCENE=t=>{const off=t>=3.5;sp.style.transform='rotate('+(t*380)+'deg)';sp.style.borderTopColor=off?'var(--red)':'var(--ink)';sp.style.opacity=off?(.5+.5*Math.abs(Math.sin(t*4))):1;
 ms.textContent=off?'Keine Verbindung zum Server':'Verbindung wird hergestellt …';ms.style.color=off?'var(--red)':'';
 const a=R(t,7.0,3.0),w=t<7?0:46+18*Math.sin(a*Math.PI*2.5)*Math.exp(-a*1.2);b1.style.width=(t<7?0:w)+'%';b2.style.width=(t<7.6?0:100-w-8)+'%'};'''

for pid, konto in (("2026-11-13-fr-workspace", "seite"), ("2026-11-13-fr-workspace-kyrill", "kyrill")):
    SCENES[pid] = dict(theme="theme-red", grid=False, end=11, body=body(konto), scene=SCENE_JS)
