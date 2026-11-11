# Vier Motive im digitalONLY-Premium-Stil. build.py setzt sie in engine.html ein.
ICON = {
 "target": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.2"/></svg>',
 "pin": '<svg viewBox="0 0 24 24"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.6"/></svg>',
 "star": '<svg viewBox="0 0 24 24"><path d="M12 3.5l2.6 5.4 5.9.8-4.3 4.1 1 5.8L12 16.8l-5.2 2.8 1-5.8-4.3-4.1 5.9-.8z"/></svg>',
 "qr": '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><path d="M14 14h3v3h-3zM18 18h3v3h-3zM14 20h1M20 14v1"/></svg>',
 "chat": '<svg viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4z"/></svg>',
 "reply": '<svg viewBox="0 0 24 24"><path d="M10 8L5 12l5 4"/><path d="M5 12h9a5 5 0 0 1 5 5v1"/></svg>',
 "check": '<svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
 "door": '<svg viewBox="0 0 24 24"><path d="M6 21V4h12v17M3 21h18"/><circle cx="14.5" cy="12.5" r=".9"/></svg>',
 "desk": '<svg viewBox="0 0 24 24"><path d="M3 10h18v3H3zM5 13v8M19 13v8"/><circle cx="12" cy="5" r="2.5"/></svg>',
 "route": '<svg viewBox="0 0 24 24"><circle cx="6" cy="18" r="2.5"/><circle cx="18" cy="6" r="2.5"/><path d="M8.5 18H15a3 3 0 0 0 0-6H9a3 3 0 0 1 0-6h6.5"/></svg>',
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

# ---------- Seite Mi (neu): Jeder kann Ihr Profil bearbeiten ----------
SCENES["2026-11-18-mi"] = dict(theme="theme-red", grid=False, end=11, body=f'''
<div class="eyebrow" data-a="fade" data-t=".15"><i></i>Google-Profil</div>
<h1 data-words data-t=".35">Ihr Google-Profil kann <span class="red">jeder bearbeiten.</span></h1>
<div class="abs light" data-a="left" data-t="1.5" data-buzz="5.25" style="left:80px;top:470px;width:470px;padding:30px 34px">
 <div style="font:700 32px 'Inter Tight';letter-spacing:-.02em">Ihr Betrieb</div>
 <div style="font:400 19px Inter;color:#777;margin:2px 0 16px">auf Google Maps</div>
 <div style="display:flex;justify-content:space-between;align-items:center;font:500 22px Inter;padding:14px 0;border-top:1px solid #e5e1d9"><span>Samstag</span><b id="hrs" style="font-weight:700">09:00–16:00</b></div>
 <div style="display:flex;justify-content:space-between;font:500 22px Inter;padding:14px 0;border-top:1px solid #e5e1d9"><span>Telefon</span><b style="font-weight:700">041 ··· ·· ··</b></div></div>
<div class="abs card" data-a="rise" data-t="2.6" style="left:80px;top:790px;width:470px;padding:26px 30px">
 <div style="display:flex;gap:14px;align-items:center"><div style="width:46px;height:46px;border-radius:50%;background:linear-gradient(135deg,#4a4a52,#2a2a30);display:grid;place-items:center;font:700 20px Inter">?</div>
  <div><div style="font:600 21px Inter">Jemand mit Google-Konto</div><div style="font:400 17px Inter;color:var(--muted)">schlägt eine Änderung vor</div></div></div>
 <div style="margin:18px 0;padding:14px 18px;border-radius:14px;background:rgba(255,90,74,.08);border:1px solid rgba(255,90,74,.3);font:500 20px Inter">Samstag: <span class="red" style="font-weight:700">geschlossen</span></div>
 <div class="chip" data-tap="4.2" style="background:#f2efe9;color:#141414;font-weight:700">Senden</div></div>
{rings(560, 560, 520, 5.6)}
<div class="abs phone" data-a="up" data-t="3.2" data-d=".9" style="right:80px;top:470px;width:380px;height:610px;padding:84px 30px 28px"><div class="notch"></div>
 <div style="font:400 17px Inter;color:var(--muted)">Samstag, 10:15</div>
 <div style="font:700 28px 'Inter Tight';margin:4px 0 22px">Kundin sucht Sie</div>
 <div class="light" style="padding:20px 22px;border-radius:18px;box-shadow:none"><div style="font:700 24px Inter">Ihr Betrieb</div>
  <div id="st" data-buzz="5.65" style="margin-top:10px;display:inline-block;font:700 19px Inter;padding:6px 14px;border-radius:999px;background:rgba(63,191,106,.15);color:#1f8a46">Geöffnet</div></div>
 <div data-a="rise" data-t="6.4" style="margin-top:26px;padding:16px 18px;border-radius:16px;background:rgba(255,90,74,.10);border:1px solid rgba(255,90,74,.35);font:600 20px/1.35 Inter;color:var(--red)">Sie fährt zur nächsten Praxis.</div>
 <div data-a="fade" data-t="6.8" style="margin-top:14px;font:400 15px Inter;color:var(--dim)">Fiktive Darstellung</div></div>
<div class="abs card" data-a="rise" data-t="7.4" style="left:80px;right:80px;top:1112px;padding:22px 28px;display:flex;flex-wrap:wrap;gap:12px;align-items:center">
 <div class="label" style="color:var(--gold);margin-right:6px">5-Minuten-Check</div>
 <div class="chip" data-a="pop" data-t="7.8" data-buzz="7.95" style="background:rgba(63,191,106,.10);border:1px solid rgba(63,191,106,.4)"><span style="color:var(--green);font-weight:800">✓</span>Hinweise von Google prüfen</div>
 <div class="chip" data-a="pop" data-t="8.15" data-buzz="8.3" style="background:rgba(63,191,106,.10);border:1px solid rgba(63,191,106,.4)"><span style="color:var(--green);font-weight:800">✓</span>Zeiten vergleichen</div>
 <div class="chip" data-a="pop" data-t="8.5" data-buzz="8.65" style="background:rgba(63,191,106,.10);border:1px solid rgba(63,191,106,.4)"><span style="color:var(--green);font-weight:800">✓</span>E-Mail-Hinweise an</div></div>
{FOOT("Fiktives Beispiel", "digital-only.ch", 9)}''',
scene='''
const hrs=document.getElementById('hrs'),st=document.getElementById('st');
window.SCENE=t=>{const c=t>=5.2;hrs.textContent=c?'Geschlossen':'09:00–16:00';hrs.style.color=c?'#e5352a':'#141414';
 const s=t>=5.6;st.textContent=s?'Geschlossen':'Geöffnet';st.style.background=s?'rgba(229,53,42,.14)':'rgba(63,191,106,.15)';st.style.color=s?'#d4291e':'#1f8a46'};''')

# ---------- Kyrill: Ads-Radius ----------
import random as _r
_r.seed(4)
cust = ''.join(f'<i class="abs" data-a="pop" data-t="{2.0 + i * .12:.2f}" style="left:{x}px;top:{y}px;width:16px;height:16px;border-radius:50%;background:var(--green);box-shadow:0 0 14px rgba(63,191,106,.8);display:block"></i>' for i, (x, y) in enumerate([(452 + _r.randint(-95, 95), 262 + _r.randint(-80, 80)) for _ in range(11)]))
far = ''.join(f'<i class="abs far" data-a="pop" data-t="{3.6 + i * .14:.2f}" data-buzz="{3.75 + i * .14:.2f}" style="left:{x}px;top:{y}px;width:16px;height:16px;border-radius:50%;background:var(--red);box-shadow:0 0 14px rgba(255,90,74,.8);display:block"></i>' for i, (x, y) in enumerate([(150, 90), (760, 120), (700, 430), (180, 440), (95, 260), (820, 300), (330, 470), (610, 60)]))
SCENES["2026-11-16-mo-kyrill"] = dict(theme="theme-blue blue-t", grid=True, end=10.5, body=f'''
<div class="eyebrow" data-a="fade" data-t=".15" style="color:var(--blue)"><i></i>Google Ads</div>
<h1 data-words data-t=".35">Wie weit fährt Ihre Kundschaft <span class="blue">wirklich?</span></h1>
<div class="abs card" data-a="rise" data-t="1.2" style="left:80px;right:80px;top:470px;height:560px;overflow:hidden">
 <svg viewBox="0 0 920 560" style="position:absolute;inset:0"><g fill="none" stroke="rgba(142,157,255,.24)" stroke-width="8" stroke-linecap="round">
  <path d="M-20 360 C 200 330, 420 390, 940 300"/><path d="M300 -20 C 330 200, 310 380, 360 580"/><path d="M-20 140 C 260 170, 600 90, 940 160"/><path d="M700 -20 C 660 220, 720 400, 690 580"/></g></svg>
 <div id="rad" class="abs" style="left:460px;top:270px;width:900px;height:900px;border-radius:50%;border:3px dashed rgba(142,157,255,.8);background:radial-gradient(circle,rgba(142,157,255,.16),rgba(142,157,255,.05) 70%);transform:translate(-50%,-50%)"></div>
 <div id="rad0" class="abs" style="left:460px;top:270px;width:900px;height:900px;border-radius:50%;border:2px dashed rgba(255,90,74,.45);transform:translate(-50%,-50%);opacity:0"></div>
 <div id="radl" class="abs chip" style="left:30px;top:26px;background:rgba(10,12,24,.85);border:1px solid rgba(142,157,255,.45);font-weight:700">Radius 30 km</div>
 {cust}{far}
 <svg class="abs" data-a="drop" data-t="1.7" data-buzz="1.95" viewBox="0 0 60 80" style="left:430px;top:200px;width:60px;height:80px;filter:drop-shadow(0 0 22px rgba(142,157,255,.9))"><path d="M30 78C30 78 4 48 4 28a26 26 0 0 1 52 0c0 20-26 50-26 50z" fill="#fff"/><circle cx="30" cy="28" r="9" fill="#5a68d8"/></svg>
 <div class="abs" data-a="fade" data-t="4.9" style="left:30px;bottom:24px;display:flex;gap:22px;font:500 18px Inter;color:var(--muted)"><span><i style="display:inline-block;width:12px;height:12px;border-radius:50%;background:var(--green);margin-right:8px"></i>Ihre Kundschaft</span><span><i style="display:inline-block;width:12px;height:12px;border-radius:50%;background:var(--red);margin-right:8px"></i>bezahlte Klicks, kein Besuch</span></div></div>
<div class="abs card" data-a="rise" data-t="7.6" style="left:80px;right:80px;top:1066px;padding:22px 28px;display:flex;gap:14px;flex-wrap:wrap;align-items:center">
 <div class="chip" data-a="pop" data-t="7.9" data-buzz="8.05" style="background:rgba(142,157,255,.10);border:1px solid rgba(142,157,255,.4)"><b style="color:var(--blue)">1</b>Standortbericht</div>
 <div class="chip" data-a="pop" data-t="8.2" data-buzz="8.35" style="background:rgba(142,157,255,.10);border:1px solid rgba(142,157,255,.4)"><b style="color:var(--blue)">2</b>Kundenkartei</div>
 <div class="chip" data-a="pop" data-t="8.5" data-buzz="8.65" style="background:rgba(142,157,255,.10);border:1px solid rgba(142,157,255,.4)"><b style="color:var(--blue)">3</b>Radius zuschneiden</div></div>
{FOOT("Fiktive Darstellung", "Kyrill Elsensohn · digital-only.ch", 8.9)}''',
scene='''
const rad=document.getElementById('rad'),rl=document.getElementById('radl'),fs=[...document.querySelectorAll('.far')];
window.SCENE=t=>{const p=spring(R(t,5.6,1.3));const d=900-(900-300)*p;rad.style.width=rad.style.height=d+'px';
 rl.textContent=t<5.9?'Radius 30 km':'Radius 8 km';rl.style.color=t<5.9?'':'var(--blue)';
 document.getElementById('rad0').style.opacity=String(R(t,5.6,.6));
 fs.forEach(e=>{if(t>6.1){e.style.opacity=String(Math.max(.5,1-R(t,6.1,.6)));e.style.filter='saturate(.45)'}else e.style.filter=''})};''')

# ---------- Cas: Der Eingang ----------
SCENES["2026-11-20-fr-cas"] = dict(theme="theme-gold", grid=False, end=10.5, body=f'''
<div class="eyebrow" data-a="fade" data-t=".15"><i></i>Google-Profil · Fotos</div>
<h1 data-words data-t=".35">Das wichtigste Foto ist <span class="gold">Ihr Eingang.</span></h1>
<div class="abs" style="left:80px;top:470px;width:470px">
 {item("door", "Der Eingang", "So, wie man ihn von der Strasse aus sieht.", 1.5, "1.95")}
 {item("desk", "Empfang oder Theke", "Bei Tageslicht.", 2.1, "2.55")}
 {item("route", "Der Weg dorthin", "Parkplatz, Haltestelle oder Hinterhof.", 2.7, "3.15")}
</div>
<div class="abs card" data-a="rise" data-t="6.6" data-buzz="7.0" style="left:80px;top:905px;width:470px;padding:22px 26px;display:flex;gap:20px;align-items:center">
 <div style="position:relative;width:110px;height:84px;border-radius:12px;background:linear-gradient(135deg,#6d7b8f,#c9b8a0);flex:none;overflow:hidden"><div style="position:absolute;left:-10px;right:-10px;top:38px;height:7px;background:var(--red);transform:rotate(-32deg);box-shadow:0 0 12px var(--red)"></div></div>
 <div><div class="label" style="color:var(--red)">Stockbild</div><div style="font:600 21px/1.35 Inter;margin-top:6px">Ein ehrliches Handyfoto schlägt ein Stockbild.</div></div></div>
{rings(520, 540, 560, 4.7, "rgba(226,192,122,.30)")}
<div class="abs phone" data-a="up" data-t="3.1" data-d=".9" style="right:80px;top:470px;width:390px;height:650px;padding:74px 22px 24px;overflow:hidden"><div class="notch"></div>
 <div style="position:relative;height:420px;border-radius:24px;overflow:hidden;background:linear-gradient(180deg,#2c3340 0%,#3b3f47 55%,#55504a 56%,#3a3631 100%)">
  <div style="position:absolute;left:40px;right:40px;top:40px;bottom:96px;background:linear-gradient(180deg,#d8cfc2,#b7ab99);border-radius:6px"></div>
  <div style="position:absolute;left:118px;width:110px;top:120px;bottom:96px;background:linear-gradient(180deg,#3b2a1c,#24180f);border:6px solid var(--gold);border-bottom:0;border-radius:8px 8px 0 0"></div>
  <div style="position:absolute;left:206px;top:205px;width:9px;height:9px;border-radius:50%;background:var(--gold)"></div>
  <div style="position:absolute;left:252px;top:132px;width:52px;height:40px;border-radius:6px;background:#1c1c1c;color:var(--gold);font:700 22px Inter;display:grid;place-items:center">12</div>
  <div style="position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.18) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.18) 1px,transparent 1px);background-size:33.33% 33.33%"></div>
  <div id="focus" style="position:absolute;left:105px;top:105px;width:140px;height:140px;border:3px solid var(--gold);border-radius:10px;opacity:0"></div>
  <div id="flash" style="position:absolute;inset:0;background:#fff;opacity:0"></div></div>
 <div style="display:flex;align-items:center;justify-content:space-between;margin-top:30px;padding:0 20px">
  <div data-a="pop" data-t="5.0" data-buzz="5.1" style="width:66px;height:66px;border-radius:14px;border:2px solid var(--gold);background:linear-gradient(180deg,#d8cfc2,#3b2a1c 70%)"></div>
  <div data-tap="4.6" data-buzz="4.62" style="width:86px;height:86px;border-radius:50%;border:5px solid #fff;display:grid;place-items:center"><div style="width:66px;height:66px;border-radius:50%;background:#fff"></div></div>
  <div style="width:66px;font:600 16px Inter;color:var(--gold);text-align:center">FOTO</div></div>
 <div data-a="fade" data-t="5.2" style="text-align:center;font:400 14px Inter;color:var(--dim);margin-top:14px">Fiktive Darstellung</div></div>
<div class="abs" data-a="rise" data-t="7.8" style="left:80px;top:1150px;font:700 40px 'Inter Tight';letter-spacing:-.03em">Zehn Minuten. <span class="gold">Kostet nichts.</span></div>
{FOOT("Beispiel", "Cas · digital-only.ch", 8.4)}''',
scene='''
const fo=document.getElementById('focus'),fl=document.getElementById('flash');
window.SCENE=t=>{const p=R(t,3.9,.5);fo.style.opacity=t>3.9&&t<4.75?1:0;fo.style.transform='scale('+(1.35-.35*eo(p))+')';
 const k=t-4.62;fl.style.opacity=k>0&&k<.45?String(.85*(1-k/.45)):'0'};''')
