# Stummes Kino-Video im Website-Stil für die Unternehmensseite: Schnitte im Takt, Kamerafahrt,
# Fokuswechsel, Raster im Hintergrund, Untertitel Wort für Wort als Erzähler.
from scenes import SCENES
import scenes_workspace_web as Wb

SUBS = [(2.4, 4.0, "Outlook weg."), (4.0, 5.0, "Teams auch."), (5.0, 6.5, "SharePoint auch."),
        (6.7, 9.1, "Zum zweiten Mal in diesem Jahr."), (9.3, 11.3, "Die einen: Wechseln bringt nur Aufwand."),
        (11.3, 13.3, "Die anderen: Wer nichts ändert, hat nichts gelernt."), (13.5, 15.4, "Wechseln oder bleiben?"),
        (15.4, 19.0, "Was ist für Ihr KMU sicherer? Ab in die Kommentare.")]
END = 18.6

ROWS = [("Outlook", "Offline", 3.2), ("Teams", "Gestört", 4.1), ("SharePoint", "Offline", 5.0)]
rows = ''.join(f'<div class="row" style="font:500 34px Inter;padding:24px 0;border-color:#eceef1"><span style="display:flex;align-items:center;gap:18px"><i style="width:16px;height:16px;border-radius:50%;border:2.5px solid #0a0a0c;display:block"></i>{n}</span>'
               f'<span class="st" data-k="{t}" data-a="fade" data-t="0" data-buzz="{t + .02}" style="font:600 28px Inter;color:#0a0a0c">Online</span></div>' for n, s, t in ROWS)

BODY = f'''
<div class="grid" style="background-image:linear-gradient(rgba(10,10,12,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(10,10,12,.05) 1px,transparent 1px);background-size:54px 54px" id="grid"></div>
<canvas id="sph" class="abs" style="left:420px;top:330px;width:720px;height:720px"></canvas>
<div class="abs pill" id="toppill" style="right:80px;top:54px;font-size:18px;padding:13px 22px">Wechsel-Check buchen</div>

<div class="shot abs" id="s1" style="inset:0">
 <div class="eyebrow" style="top:180px">Microsoft-365-Ausfall · 12./13. November 2026</div>
 <div class="abs wcard cam" style="left:120px;top:330px;width:840px;padding:40px 46px">
  <div style="font:500 24px Inter;color:#0d3b8b">Dienststatus</div>
  <div style="font:800 52px 'Inter Tight';letter-spacing:-.04em;margin:6px 0 14px">outlook.office365.com</div>{rows}</div>
</div>

<div class="shot abs" id="s2" style="inset:0">
 <div class="abs cam" style="left:80px;right:80px;top:300px;text-align:center">
  <div style="font:800 340px/0.9 'Inter Tight';letter-spacing:-.07em;color:#0d3b8b">2×</div>
  <div style="font:800 64px/1 'Inter Tight';letter-spacing:-.045em;margin-top:26px">in diesem Jahr.</div>
  <div style="display:inline-block;margin-top:34px;border:1.5px solid #0a0a0c;border-radius:999px;padding:12px 24px;font:600 24px Inter;background:#fff">Januar 2026: fast 10 Stunden</div></div>
</div>

<div class="shot abs" id="s3" style="inset:0">
 <div class="eyebrow" style="top:180px">Zwei Lager</div>
 <div class="abs wcard cam" id="camp1" style="left:80px;top:300px;width:440px;padding:36px 34px;min-height:330px">
  <div style="font:500 22px Inter;color:#5b6270">Die einen</div>
  <div style="font:800 46px/1.05 'Inter Tight';letter-spacing:-.04em;margin-top:14px">«Wechseln bringt nur Aufwand.»</div></div>
 <div class="abs wcard cam" id="camp2" style="right:80px;top:300px;width:440px;padding:36px 34px;min-height:330px;border-color:#0d3b8b">
  <div style="font:500 22px Inter;color:#0d3b8b">Die anderen</div>
  <div style="font:800 46px/1.05 'Inter Tight';letter-spacing:-.04em;margin-top:14px">«Wer nichts ändert, hat nichts gelernt.»</div></div>
 <div class="abs" style="left:490px;top:430px;width:100px;height:100px;border-radius:50%;background:#0a0a0c;color:#fff;display:grid;place-items:center;font:800 32px 'Inter Tight';z-index:3" id="vs">VS</div>
 <div class="abs" style="left:80px;right:80px;top:720px;display:flex;gap:18px;justify-content:center">
  <div class="opt" id="o1" style="padding:20px 34px;font-size:26px">Bleiben</div>
  <div class="opt" id="o2" style="padding:20px 34px;font-size:26px;border-color:#0d3b8b;color:#0d3b8b">Wechseln</div></div>
</div>

<div class="shot abs" id="s4" style="inset:0">
 <div class="eyebrow" style="top:180px">Die Frage zum Wochenende</div>
 <h1 class="cam" style="top:240px;font-size:118px;line-height:.92">Wechseln<br>oder bleiben?</h1>
 <div class="abs cam" style="left:80px;top:560px;width:520px;font:400 30px/1.4 Inter">Sicher heisst nicht, dass nie etwas ausfällt. Sicher heisst: das passende Werkzeug und ein Plan B.</div>
 <div class="abs" style="left:80px;top:860px;display:flex;align-items:center;gap:28px">
  <div class="pill" id="cta" style="font-size:26px;padding:22px 36px">Wechsel-Check buchen {Wb.ARROW}</div>
  <span style="font:500 24px Inter;text-decoration:underline;text-underline-offset:6px">Link im ersten Kommentar</span></div>
</div>

<div class="abs" id="intro" style="inset:0;background:#0a0a0c;z-index:30;display:grid;place-content:center;text-align:center">
 <div style="font:500 30px 'JetBrains Mono';color:#8b919c;letter-spacing:.06em"><span id="ty"></span><span id="blk" style="display:inline-block;width:16px;height:32px;background:#f4f2ee;vertical-align:-5px;margin-left:4px"></span></div>
 <div id="nc" style="margin-top:28px;font:800 64px 'Inter Tight';letter-spacing:-.04em;color:#f4f2ee;opacity:0">Keine Verbindung.</div>
</div>

<div class="abs" id="sub" style="left:80px;right:80px;top:1150px;min-height:120px;display:flex;align-items:center;justify-content:center;text-align:center;z-index:25"><div id="subt" style="font:800 46px/1.15 'Inter Tight';letter-spacing:-.03em"></div></div>
<div class="foot" id="ft" style="z-index:26"><span>Stand 13.11.2026 · Quellen: ORF, CNBC, The Register · Illustration</span><span>digital-only.ch</span></div>
{Wb.CUR}'''

SUBS_JS = repr([[a, b, s] for a, b, s in SUBS]).replace("'", '"')
SCENE = Wb.SHARED_JS + f'''
const SUB={SUBS_JS};let K=null,C=[11.6,12.4,16.6];
const SH=[['s1',2.2,6.6],['s2',6.6,9.2],['s3',9.2,13.4],['s4',13.4,99]];
const ty=document.getElementById('ty'),blk=document.getElementById('blk'),nc=document.getElementById('nc'),intro=document.getElementById('intro'),subt=document.getElementById('subt');
const TY="Donnerstag, 12. November · 19:00";let lastSub=-1;
window.SCENE=t=>{{
 if(!K){{const a=pos(document.getElementById('o1')),b=pos(document.getElementById('o2')),c=pos(document.getElementById('cta'));
  K=[[10.4,1100,1340],[11.4,b[0],b[1]],[11.6,b[0],b[1]],[12.2,a[0],a[1]],[12.4,a[0],a[1]],[12.8,(a[0]+b[0])/2,a[1]+60],[13.3,(a[0]+b[0])/2,a[1]+60],[15.8,500,1100],[16.6,c[0],c[1]],[20,c[0],c[1]]]}}
 base(t);
 // Intro: Schwarzbild, Tipptext, harter Schnitt
 ty.textContent=TY.slice(0,Math.round(TY.length*R(t,.2,1.0)));blk.style.opacity=(Math.floor(t*3)%2)?'0':'1';
 nc.style.opacity=t>=1.45?'1':'0';nc.style.transform='translateX('+(t>=1.45&&t<1.9?Math.sin((t-1.45)*95)*10*Math.exp(-(t-1.45)*8):0)+'px)';
 intro.style.opacity=t<2.2?'1':'0';
 // Shots mit Kamerafahrt und Fokus
 SH.forEach(([id,a,b])=>{{const e=document.getElementById(id),on=t>=a&&t<b;e.style.opacity=on?'1':'0';
  e.querySelectorAll('.cam').forEach((c,i)=>{{const p=R(t,a,1.6),s=1.07-.07*eo(p),bl=Math.max(0,7*(1-R(t,a+.05*i,.45)));
   c.style.transform='scale('+s+')';c.style.filter=bl>.1?'blur('+bl.toFixed(1)+'px)':'none';c.style.transformOrigin='50% 40%'}})}});
 document.getElementById('grid').style.transform='translateY('+(-t*6)+'px) scale('+(1.02+.02*Math.sin(t*.4))+')';
 sph.style.transform='scale('+(t<13.4?1:1+.25*eo(R(t,13.4,2)))+')';sph.style.opacity=t<13.4?'.65':'1';
 // Status-Zeilen kippen
 document.querySelectorAll('.st').forEach(e=>{{const k=+e.dataset.k,off=t>=k;e.textContent=off?(e.parentNode.textContent.includes('Teams')?'Gestört':'Offline'):'Online';
  e.style.color=off?'#8b919c':'#0a0a0c';e.style.textDecoration=off?'line-through':'none'}});
 // Lager-Karten
 [['camp1',9.4],['camp2',11.0]].forEach(([id,k])=>{{const e=document.getElementById(id),p=spring(R(t,k,.6));e.style.opacity=String(cl(R(t,k,.25)));e.style.translate=(id==='camp1'?-1:1)*(1-p)*120+'px 0'}});
 const vs=document.getElementById('vs'),vp=spring(R(t,12.6,.5));vs.style.transform='scale('+(.3+.7*vp)+')';vs.style.opacity=String(cl(R(t,12.6,.2)));
 // Untertitel Wort für Wort
 const i=SUB.findIndex(s=>t>=s[0]&&t<s[1]);if(i<0){{subt.innerHTML='';lastSub=-1}}else{{const s=SUB[i],w=s[2].split(' ');
  if(i!==lastSub){{subt.innerHTML=w.map(x=>'<span style="padding:0 6px;border-radius:8px">'+x+'</span>').join(' ');lastSub=i}}
  const sp=[...subt.children],n=Math.min(w.length,Math.floor((t-s[0])/((s[1]-s[0]-.35)/w.length))+1);
  sp.forEach((e,j)=>{{e.style.opacity=j<n?'1':'0';e.style.background=j===n-1?'#0d3b8b':'transparent';e.style.color=j===n-1?'#fff':'#0a0a0c'}})}}
 document.getElementById('sub').style.opacity=t<2.2?'0':'1';
}};'''

SCENES["cine-workspace-seite-de"] = dict(theme="theme-web", grid=False, end=END - 2.5, body=BODY, scene=SCENE)
