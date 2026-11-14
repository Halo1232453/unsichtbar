# Motive für die Beiträge KW 46 (Mi 11. bis Fr 13. November 2026), alle vier Konten.
from scenes import SCENES, ICON, item, rings, FOOT

ICON.update({
 "lock": '<svg viewBox="0 0 24 24"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>',
 "clock": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 "phone": '<svg viewBox="0 0 24 24"><path d="M6 3h4l2 5-3 2a11 11 0 0 0 5 5l2-3 5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 4 5a2 2 0 0 1 2-2z"/></svg>',
 "search": '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>',
 "x": '<svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></svg>',
 "list": '<svg viewBox="0 0 24 24"><path d="M9 6h11M9 12h11M9 18h11"/><circle cx="4.5" cy="6" r="1"/><circle cx="4.5" cy="12" r="1"/><circle cx="4.5" cy="18" r="1"/></svg>',
 "pen": '<svg viewBox="0 0 24 24"><path d="M4 20h4L19 9l-4-4L4 16z"/></svg>',
 "access": '<svg viewBox="0 0 24 24"><circle cx="12" cy="4.5" r="1.8"/><path d="M8 9h8M12 9v5l4 5M12 14l-4 5"/></svg>',
})
FT = {"seite": "digital-only.ch", "bertan": "Bertan Findik · digital-only.ch", "kyrill": "Kyrill Elsensohn · digital-only.ch", "cas": "Cas · digital-only.ch"}
OK = 'background:rgba(63,191,106,.10);border:1px solid rgba(63,191,106,.4)'
BAD = 'background:rgba(255,90,74,.10);border:1px solid rgba(255,90,74,.42);color:var(--red)'


def std(pid, theme, eyebrow, h1, items, right, bottom, foot_l, konto, end=10.5, grid=False, scene="", h1size=None, eye=None, left_top=470):
    hs = f' style="font-size:{h1size}px"' if h1size else ''
    ec = f' style="color:{eye}"' if eye else ''
    lst = ''.join(item(ic, ti, tx, 1.5 + i * .6, f"{1.95 + i * .6:.2f}") for i, (ic, ti, tx) in enumerate(items))
    left = f'<div class="abs" style="left:80px;top:{left_top}px;width:480px">{lst}</div>' if items else ''
    bot = f'<div class="abs" data-a="rise" data-t="{end - 2.4}" style="left:80px;right:80px;top:1150px;font:700 38px \'Inter Tight\';letter-spacing:-.03em">{bottom}</div>' if bottom else ''
    SCENES[pid] = dict(theme=theme, grid=grid, end=end, scene=scene, body=f'''
<div class="eyebrow" data-a="fade" data-t=".15"{ec}><i></i>{eyebrow}</div>
<h1 data-words data-t=".35"{hs}>{h1}</h1>
{left}{right}{bot}{FOOT(foot_l, FT[konto], end - 1.8)}''')


def phone(inner, t=3.2, top=470, h=640, w=390, pad="80px 30px 26px"):
    return f'<div class="abs phone" data-a="up" data-t="{t}" data-d=".9" style="right:80px;top:{top}px;width:{w}px;height:{h}px;padding:{pad};overflow:hidden"><div class="notch"></div>{inner}</div>'


# ---------- Seite Mi 11.11.: Konkurrenz ----------
def pin(n, x, y, t):
    return (f'<div class="abs" data-rings="{t + .3}" style="left:{x - 110}px;top:{y - 70}px;width:220px;height:220px">' + ''.join('<div class="ring" style="inset:0;border-color:rgba(142,157,255,.55)"></div>' for _ in range(3)) + '</div>'
            f'<svg class="abs" data-a="drop" data-t="{t}" data-buzz="{t + .25}" viewBox="0 0 60 80" style="left:{x - 30}px;top:{y - 40}px;width:60px;height:80px;filter:drop-shadow(0 0 20px rgba(142,157,255,.9))"><path d="M30 78C30 78 4 48 4 28a26 26 0 0 1 52 0c0 20-26 50-26 50z" fill="#fff"/><text x="30" y="36" text-anchor="middle" font-family="Inter" font-weight="700" font-size="24" fill="#141414">{n}</text></svg>')


def lab(x, y, name, sub, t):
    return f'<div class="abs card" data-a="pop" data-t="{t}" style="left:{x}px;top:{y}px;padding:14px 20px;border-radius:16px"><div style="font:600 24px Inter">{name}</div>' + (f'<div style="font:500 19px Inter;color:var(--muted)"><span class="gold">★ {sub[0]}</span> · {sub[1]}</div>' if sub else '') + '</div>'


SCENES_MAP = f'''
<svg class="abs" viewBox="0 0 1080 760" style="left:0;top:500px;width:1080px;height:760px"><g fill="none" stroke="rgba(142,157,255,.28)" stroke-width="7" stroke-linecap="round">
 <path d="M-20 380 C 250 350, 560 430, 1100 300"/><path d="M300 -20 C 330 240, 300 520, 360 780"/><path d="M-20 700 C 300 680, 700 720, 1100 650"/><path d="M780 -20 C 740 260, 800 520, 760 780"/></g>
 <g stroke="rgba(142,157,255,.12)" stroke-width="2"><path d="M60 120 L1020 520M80 600 L1000 140"/></g></svg>
{pin(1, 300, 820, 2.0)}{pin(2, 640, 920, 2.5)}{pin(3, 820, 640, 3.0)}
{lab(390, 640, "Mitbewerber A", ("4,8", "Fotos · offen"), 2.3)}{lab(690, 990, "Mitbewerber B", ("4,6", "offen"), 2.8)}{lab(700, 520, "Mitbewerber C", None, 3.3)}
<div class="abs" data-a="pop" data-t="1.6" data-buzz="4.0,4.6,5.2" style="left:110px;top:560px;width:84px;height:84px;border-radius:50%;background:#1f8f3f;display:grid;place-items:center;box-shadow:0 0 30px rgba(63,191,106,.6)"><svg viewBox="0 0 24 24" style="width:40px;height:40px;fill:#fff"><path d="M6 3h4l2 5-3 2a11 11 0 0 0 5 5l2-3 5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 4 5a2 2 0 0 1 2-2z"/></svg></div>
<div class="abs" data-a="fade" data-t="5.6" style="left:420px;top:1080px;width:60px;height:80px;border:3px dashed rgba(255,255,255,.35);border-radius:30px 30px 30px 30px / 30px 30px 50px 50px;display:grid;place-items:center;color:var(--muted);font:600 26px Inter">?</div>
<div class="abs card" data-a="rise" data-t="5.9" data-buzz="6.3" style="left:500px;top:1070px;padding:16px 22px;opacity:.9"><div style="font:600 24px Inter;color:var(--muted)">Ihr Betrieb</div><div style="font:500 20px Inter;color:var(--dim)">nicht unter den ersten drei</div></div>'''
std("2026-11-11-mi", "theme-blue", "Jetzt gerade", 'Während Sie das lesen, ruft jemand <span class="blue">Ihre Konkurrenz</span> an.', [], SCENES_MAP, "", "Fiktive Darstellung · Suche «Elektriker Zug»", "seite", grid=True, end=9.5, eye="var(--red)")

# ---------- Seite Do 12.11.: Feiertage ----------
def cal():
    hl = {8: "reg", 24: "kurz", 25: "fei", 26: "reg", 31: "kurz"}
    cells = '<div></div>'
    for d in range(1, 32):
        k = hl.get(d)
        st = {"fei": "background:linear-gradient(180deg,#f0d394,#c39d5f);color:#1a1408;box-shadow:0 0 22px rgba(226,192,122,.6)",
              "reg": "border:2px solid var(--gold);color:var(--gold)", "kurz": "border:2px dashed var(--gold);color:var(--gold)"}.get(k, "background:rgba(255,255,255,.05)")
        a = f' data-a="pop" data-t="{4.2 + list(hl).index(d) * .35:.2f}" data-buzz="{4.3 + list(hl).index(d) * .35:.2f}"' if k else f' data-a="fade" data-t="{2.6 + d * .03:.2f}"'
        cells += f'<div{a} style="height:44px;border-radius:10px;display:grid;place-items:center;font:600 18px Inter;{st}">{d}</div>'
    head = ''.join(f'<div style="text-align:center;font:500 15px Inter;color:var(--muted)">{x}</div>' for x in ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"])
    return (f'<div class="abs card" data-a="right" data-t="2.2" style="right:80px;top:500px;width:420px;padding:26px 24px">'
            f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:14px"><span style="font:700 30px \'Inter Tight\'">Dezember</span><span style="color:var(--muted);font:500 18px Inter">2026</span></div>'
            f'<div style="display:grid;grid-template-columns:repeat(7,1fr);gap:7px">{head}{cells}</div>'
            f'<div style="display:flex;gap:16px;margin-top:16px;font:500 15px Inter;color:var(--muted)"><span>■ Feiertag</span><span>□ regional</span><span>⬚ oft verkürzt</span></div></div>')
std("2026-11-12-do", "theme-gold", "Google-Profil · Feiertage", '3 Dinge, bevor im Dezember <span class="gold">die Feiertage kommen.</span>',
    [("check", "Feiertage bestätigen", "Auch an Tagen, an denen Sie normal offen haben."), ("pin", "8. und 26. Dezember", "Regional, je nach Kanton."), ("lock", "Länger zu?", "«Vorübergehend geschlossen» prüfen.")],
    cal() + '<div class="abs card" data-a="rise" data-t="6.2" data-buzz="6.6" style="left:80px;right:80px;top:1010px;padding:24px 30px;display:flex;gap:26px;align-items:center"><div style="font:700 56px \'Inter Tight\';color:var(--gold);letter-spacing:-.04em">26.12.</div><div><div style="font:600 25px Inter">Offen, zu oder Notfalldienst?</div><div style="font:400 20px Inter;color:var(--muted)">Im Profil unter «Besondere Öffnungszeiten»</div></div></div>',
    'Dauert etwa <span class="gold">eine Viertelstunde.</span>', "Beispiel-Kalender", "seite", end=10)

# ---------- Seite Fr 13.11.: Der Anruf ----------
std("2026-11-13-fr", "theme-red", "Start ins Wochenende", 'Der Anruf, den Sie nie bekommen haben, war vielleicht <span class="red">Ihr bester Kunde.</span>', [],
    f'''<div class="abs light" data-a="left" data-t="1.8" style="left:80px;top:640px;width:430px;padding:30px 32px">
 <div style="font:700 32px 'Inter Tight'">Ihr Betrieb</div><div style="font:400 19px Inter;color:#777;margin-bottom:12px">auf Google Maps</div>
 <div style="font:600 21px Inter;margin-bottom:18px"><span style="color:#c9971f">★ 4,7</span> · Geöffnet</div>
 <div class="chip" data-tap="3.3" style="background:#141414;color:#fff;font-weight:700">☎ Anrufen</div></div>
<div class="abs" data-a="fade" data-t="6.6" style="left:80px;top:960px;width:430px"><div style="font:500 25px Inter;color:var(--muted)">Was danach passiert, sehen Sie nie.</div><div style="font:700 27px Inter;color:var(--gold);margin-top:6px">Testen Sie es diese Woche selbst.</div></div>
{rings(560, 560, 520, 4.6)}
{phone('<div style="text-align:center;margin-top:30px"><div style="width:110px;height:110px;border-radius:50%;margin:0 auto;border:1px solid rgba(226,192,122,.45);background:rgba(226,192,122,.08);display:grid;place-items:center"><svg viewBox="0 0 24 24" style="width:48px;height:48px;stroke:var(--gold);fill:none;stroke-width:1.8"><path d="M3 11l9-7 9 7v9H3z"/><path d="M9 20v-6h6v6"/></svg></div><div style="font:700 30px \'Inter Tight\';margin-top:26px">Ihr Betrieb</div><div id="cs" style="font:500 21px Inter;color:var(--muted);margin-top:6px">Wird angerufen …</div><div data-a="pop" data-t="5.2" data-buzz="5.3" style="margin:28px 6px 0;padding:18px;border-radius:16px;background:rgba(255,90,74,.10);border:1px solid rgba(255,90,74,.4);font:500 21px/1.35 Inter;color:#f3b0a8">«Kein Anschluss unter dieser Nummer.»</div><div data-tap="7.2" data-buzz="7.25" style="width:96px;height:96px;border-radius:50%;margin:46px auto 0;background:#e5352a;display:grid;place-items:center;box-shadow:0 0 40px rgba(229,53,42,.6)"><svg viewBox="0 0 24 24" style="width:42px;height:42px;fill:#fff;transform:rotate(135deg)"><path d="M6 3h4l2 5-3 2a11 11 0 0 0 5 5l2-3 5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 4 5a2 2 0 0 1 2-2z"/></svg></div></div>', t=3.6, top=500, h=680)}''',
    "", "Fiktives Beispiel", "seite", end=10,
    scene='''const cs=document.getElementById('cs');window.SCENE=t=>{const f=t>=5.1;cs.textContent=f?'Anruf fehlgeschlagen':'Wird angerufen'+'.'.repeat(1+Math.floor(t*3)%3);cs.style.color=f?'var(--red)':''};''')

# ---------- Bertan Do 12.11.: 3 Fragen ----------
qs = [("1", "«Wie viele Anrufe hat das 2025 Betrieben wie meinem gebracht?»"), ("2", "«Welche Zahlen sehe ich selbst, ohne Sie anzurufen?»"), ("3", "«Wie und wann kann ich kündigen?»")]
qhtml = ''.join(f'<div class="abs card" data-a="left" data-t="{1.6 + i * .8}" data-buzz="{2.0 + i * .8}" style="left:80px;top:{480 + i * 150}px;width:520px;padding:22px 26px;display:flex;gap:18px;align-items:flex-start"><div style="flex:none;width:44px;height:44px;border-radius:12px;background:rgba(226,192,122,.12);border:1px solid rgba(226,192,122,.45);color:var(--gold);font:700 22px Inter;display:grid;place-items:center">{n}</div><div style="font:600 23px/1.35 Inter">{q}</div></div>' for i, (n, q) in enumerate(qs))
offer = f'''<div class="abs card" data-a="right" data-t="4.2" style="right:80px;top:480px;width:330px;padding:26px 26px">
 <div class="label mono" style="color:var(--gold)">Angebot</div><div style="font:700 28px 'Inter Tight';margin:8px 0 6px">Werbepaket</div>
 <div class="row" style="font-size:19px"><span style="color:var(--muted)">Laufzeit</span><b>12 Monate</b></div>
 <div class="row" style="font-size:19px"><span style="color:var(--muted)">Anrufe 2025</span><span class="q">?</span></div>
 <div class="row" style="font-size:19px"><span style="color:var(--muted)">Eigene Zahlen</span><span class="q">?</span></div>
 <div class="row" style="font-size:19px"><span style="color:var(--muted)">Kündigung</span><span class="q">?</span></div></div>
<div class="abs" data-a="slam" data-t="5.8" data-d=".35" style="right:110px;top:830px;transform:rotate(-8deg);border:4px solid var(--gold);color:var(--gold);font:700 28px 'JetBrains Mono';letter-spacing:.1em;padding:8px 18px;border-radius:10px;background:rgba(9,9,11,.85)">ERST FRAGEN</div>
<div class="abs" data-a="rise" data-t="6.8" style="left:80px;right:80px;top:960px;font:500 26px/1.4 Inter;color:var(--muted)">Ein guter Verkäufer hat auf alle drei eine Antwort. <span style="color:var(--ink);font-weight:600">Wird es still, wissen Sie auch etwas.</span></div>'''
std("2026-11-12-do-bertan", "theme-gold", "Aus dem Aussendienst", '3 Fragen an jeden <span class="gold">Werbeverkäufer.</span>', [], qhtml + offer, "", "Beispiel", "bertan", end=10)

# ---------- Bertan Fr 13.11.: Gut gegen sehr gut ----------
gut = '''<div class="abs card" data-a="left" data-t="1.6" style="left:80px;top:480px;width:450px;padding:28px 30px;opacity:.85">
 <div class="label">Gut</div><div style="font:700 30px 'Inter Tight';margin:8px 0 14px">Präsentiert</div>
 <div class="row" style="font-size:20px"><span style="color:var(--muted)">Folien</span><b>10</b></div>
 <div class="row" style="font-size:20px"><span style="color:var(--muted)">Pakete</span><b>3</b></div>
 <div class="row" style="font-size:20px"><span style="color:var(--muted)">Rabatt gilt bis</span><b class="red">Freitag</b></div></div>'''
sgut = ''.join(f'<div data-a="pop" data-t="{3.4 + i * .5}" data-buzz="{3.5 + i * .5}" style="display:flex;gap:12px;align-items:flex-start;padding:12px 0;border-bottom:1px solid var(--line);font:500 20px/1.35 Inter"><span style="color:var(--gold);font-weight:800">?</span>{q}</div>' for i, q in enumerate(["Woher kommen Ihre Kunden heute?", "Was hat funktioniert, was nicht?", "Was soll in einem Jahr anders sein?"]))
sehr = f'''<div class="abs card" data-a="right" data-t="2.6" style="right:80px;top:480px;width:430px;padding:28px 30px;border-color:rgba(226,192,122,.45);box-shadow:0 0 50px rgba(226,192,122,.15)">
 <div class="label" style="color:var(--gold)">Sehr gut</div><div style="font:700 30px 'Inter Tight';margin:8px 0 6px">Fragt zuerst</div>{sgut}</div>
<div class="abs light" data-a="pop" data-t="5.6" data-buzz="5.75" style="right:80px;top:880px;width:430px;padding:20px 24px;font:600 22px/1.35 Inter">«Sie brauchen gerade nichts von mir.»</div>'''
std("2026-11-13-fr-bertan", "theme-red", "Aus dem Aussendienst", 'Gute Verkäufer präsentieren. <span class="gold">Sehr gute fragen.</span>', [], gut + sehr,
    'Nur die zweite Sorte <span class="gold">verdient Ihre Zeit.</span>', "Beispiel", "bertan", end=9.5)

# ---------- Kyrill Mi 11.11.: 3 Uhr nachts ----------
seg = ''.join(f'<div class="hseg" data-h="{h}" style="flex:1;height:34px;border-radius:4px;background:{"rgba(63,191,106,.75)" if 7 <= h < 19 else "rgba(255,90,74,.55)"}"></div>' for h in range(24))
std("2026-11-11-mi-kyrill", "theme-blue blue-t", "Google Ads", 'Ihre Anzeige läuft um 3 Uhr nachts. <span class="blue">Ihr Telefon nicht.</span>',
    [("clock", "Werbezeitplan", "An Ihre Öffnungszeiten anpassen."), ("phone", "Anruf-Assets", "Nummer nur, wenn jemand abnimmt."), ("search", "Nachts", "Website oder Online-Termin statt Telefon.")],
    phone('<div id="clk" style="text-align:center;font:200 92px \'Inter Tight\';letter-spacing:-.04em;margin-top:8px">22:00</div><div style="text-align:center;font:500 18px Inter;color:var(--muted)">Donnerstag</div>'
          '<div class="light" data-a="pop" data-t="4.6" style="margin-top:34px;padding:18px 20px;border-radius:18px;box-shadow:none"><div style="font:600 14px Inter;color:#777">Anzeige</div><div style="font:700 22px Inter;margin:4px 0 12px">Ihr Betrieb · Zug</div><div class="chip" data-tap="5.4" style="background:#141414;color:#fff;font-weight:700;padding:9px 16px">☎ Jetzt anrufen</div></div>'
          '<div data-a="pop" data-t="6.1" data-buzz="6.2" style="margin-top:22px;padding:16px;border-radius:16px;background:rgba(255,90,74,.10);border:1px solid rgba(255,90,74,.4);color:var(--red);font:600 20px Inter;text-align:center">Niemand nimmt ab</div>', t=3.0, top=470, h=600)
    + f'<div class="abs card" data-a="rise" data-t="6.8" style="left:80px;right:80px;top:1100px;padding:20px 26px"><div style="display:flex;justify-content:space-between;font:600 17px Inter;color:var(--muted);margin-bottom:10px"><span>Werbezeitplan</span><span>0 Uhr · 12 Uhr · 24 Uhr</span></div><div style="display:flex;gap:3px">{seg}</div></div>',
    "", "Fiktive Darstellung", "kyrill", end=10.5, h1size=66,
    scene='''const ck=document.getElementById('clk'),hs=[...document.querySelectorAll('.hseg')];
window.SCENE=t=>{const m=Math.round(22*60+300*R(t,3.6,1.6));const h=Math.floor(m/60)%24,mm=m%60;ck.textContent=String(h).padStart(2,'0')+':'+String(mm).padStart(2,'0');
 hs.forEach(e=>{const h=+e.dataset.h,night=h<7||h>=19;e.style.opacity=night?String(1-.82*R(t,7.6,.7)):'1'})};''')

# ---------- Kyrill Do 12.11.: Suchbegriffe ----------
terms = [("physiotherapie zug", 1), ("physio zug termin", 1), ("physiotherapie ausbildung", 0), ("physiotherapeut lohn", 0), ("physio job zug", 0)]
rows = ''
for i, (s, good) in enumerate(terms):
    t0 = 2.6 + i * .3
    if good:
        r = f'<span class="chip" style="{OK};padding:5px 12px;font-size:15px"><span style="color:var(--green)">✓</span>Kunde</span>'
    else:
        k = 4.6 + (i - 2) * .55
        r = f'<span class="chip" data-a="pop" data-t="{k:.2f}" data-buzz="{k + .1:.2f}" style="{BAD};padding:5px 12px;font-size:15px">ausgeschlossen</span>'
    rows += f'<div class="row" data-a="fade" data-t="{t0:.2f}" style="font:500 16px \'JetBrains Mono\'"><span class="term" data-bad="{0 if good else 1}">{s}</span>{r}</div>'
std("2026-11-12-do-kyrill", "theme-red", "Google Ads", 'Wofür haben Sie letzte Woche <span class="red">wirklich bezahlt?</span>',
    [("list", "Suchbegriffe öffnen", "Letzte 30 Tage."), ("search", "Markieren", "Alles, was nie zu Kundschaft führt."), ("x", "Ausschliessen", "«Ausbildung», «Lohn», «Job».")],
    f'<div class="abs card" data-a="right" data-t="2.2" style="right:60px;top:470px;width:460px;padding:26px 24px"><div class="label">Suchbegriffe · 30 Tage</div><div style="margin-top:10px">{rows}</div></div>',
    'Danach reicht <span class="red">ein Blick pro Monat.</span>', "Fiktive Darstellung", "kyrill", end=10,
    scene='''const tm=[...document.querySelectorAll('.term')];window.SCENE=t=>{tm.forEach((e,i)=>{if(e.dataset.bad==='1'){const k=4.6+(i-2)*.55;e.style.textDecoration=t>=k?'line-through':'none';e.style.color=t>=k?'var(--dim)':''}})};''')

# ---------- Kyrill Fr 13.11.: Klicks oder Anrufe ----------
def tog(lbl, on_t, idn):
    return (f'<div class="row" style="font:600 22px Inter;padding:20px 0"><span>{lbl}</span><div id="{idn}" data-tap="{on_t}" data-buzz="{on_t + .05}" data-on="{on_t}" '
            f'style="width:70px;height:40px;border-radius:20px;background:#3a3a40;position:relative"><i style="position:absolute;top:4px;left:4px;width:32px;height:32px;border-radius:50%;background:#fff;display:block;transition:none"></i></div></div>')
std("2026-11-13-fr-kyrill", "theme-blue blue-t", "Google Ads", 'Zählen Sie Klicks <span class="blue">oder Anrufe?</span>',
    [("phone", "Anrufe als Conversions?", "Direkt über die Anzeige und über die Website."), ("list", "Formulare und Termine?", "Auch das sind Ergebnisse."), ("clock", "Wer schaut monatlich?", "Ohne Blick bleibt alles geraten.")],
    phone(f'<div style="font:700 28px \'Inter Tight\'">Conversions</div><div style="font:400 17px Inter;color:var(--muted);margin:4px 0 16px">Was zählt Ihr Konto?</div>'
          f'<div class="row" style="font:600 22px Inter;padding:20px 0"><span>Klicks</span><span class="chip" style="{OK};padding:6px 14px;font-size:16px">gezählt</span></div>'
          + tog("Anrufe", 5.0, "t1") + tog("Formulare", 5.6, "t2") + tog("Termine", 6.2, "t3") +
          '<div data-a="pop" data-t="7.0" style="margin-top:22px;padding:16px;border-radius:16px;background:rgba(142,157,255,.10);border:1px solid rgba(142,157,255,.4);font:600 20px Inter;text-align:center;color:var(--blue)">Jetzt sieht man, was es bringt.</div>', t=3.0, h=640),
    'Ein Klick ist kein Kunde. <span class="blue">Ein Anruf schon eher.</span>', "Fiktive Darstellung", "kyrill", end=10.5,
    scene='''const tg=[...document.querySelectorAll('[data-on]')].filter(e=>e.id&&e.id[0]==='t');window.SCENE=t=>{tg.forEach(e=>{const p=spring(R(t,+e.dataset.on,.4));e.style.background=t>=+e.dataset.on?'#3f8f5a':'#3a3a40';e.firstChild.style.left=(4+30*p)+'px'})};''')

# ---------- Cas Mi 11.11.: ChatGPT fragen ----------
chk = [("Adresse", "✓", OK, 5.6), ("Telefon", "?", 'background:rgba(226,192,122,.10);border:1px solid rgba(226,192,122,.45);color:var(--gold)', 6.0), ("Leistungen", "✓", OK, 6.4), ("Empfohlen?", "✕", BAD, 6.8)]
chkh = ''.join(f'<div class="row" style="font:500 20px Inter;padding:13px 0"><span style="color:var(--muted)">{a}</span><span class="chip" data-a="pop" data-t="{t}" data-buzz="{t + .1}" style="{st};padding:5px 14px;font-size:17px;font-weight:700">{m}</span></div>' for a, m, st, t in chk)
std("2026-11-11-mi-cas", "theme-blue blue-t", "KI-Sichtbarkeit", 'Fragen Sie ChatGPT, was es <span class="blue">über Sie weiss.</span>',
    [("search", "Zwei Fragen stellen", "«Was weisst du über …?» und «Wen empfiehlst du?»"), ("list", "Genau hinschauen", "Adresse, Telefon, Leistungen."), ("pen", "Falsch? Bei sich suchen", "Google-Profil, Website, alte Verzeichnisse.")],
    f'''<div class="abs card" data-a="right" data-t="2.6" style="right:80px;top:470px;width:400px;padding:24px 24px">
 <div style="display:flex;align-items:center;gap:10px;font:600 19px Inter"><i style="width:10px;height:10px;border-radius:50%;background:var(--blue);box-shadow:0 0 12px var(--blue);display:block"></i>KI-Chat</div>
 <div data-a="pop" data-t="3.2" style="margin:18px 0 0 auto;width:fit-content;max-width:300px;background:#f2efe9;color:#141414;border-radius:18px 18px 4px 18px;padding:13px 17px;font:500 18px/1.35 Inter">Was weisst du über [Ihr Betrieb] in Zug?</div>
 <div data-a="pop" data-t="3.9" style="margin-top:14px;background:rgba(255,255,255,.06);border:1px solid var(--line);border-radius:18px 18px 18px 4px;padding:14px 17px"><div id="ty" class="mono" style="letter-spacing:.2em">···</div>
  <div id="sk" style="display:none"><div style="height:12px;border-radius:6px;background:rgba(255,255,255,.18);width:92%;margin:6px 0"></div><div style="height:12px;border-radius:6px;background:rgba(255,255,255,.18);width:78%;margin:8px 0"></div><div style="height:12px;border-radius:6px;background:rgba(255,255,255,.18);width:60%;margin:8px 0"></div></div></div>
 <div class="label" style="margin-top:18px">Ihr Check</div>{chkh}</div>''',
    'Fünf Minuten. <span class="blue">Heute noch.</span>', "Fiktive Darstellung", "cas", end=10,
    scene='''const ty=document.getElementById('ty'),sk=document.getElementById('sk');window.SCENE=t=>{const d=t<4.9;ty.style.display=d?'block':'none';sk.style.display=d?'none':'block';ty.textContent=['·  ','·· ','···'][Math.floor(t*4)%3]};''')

# ---------- Cas Do 12.11.: 750 Zeichen ----------
desc = "Physiotherapie in Zug für Rücken, Knie und Sport. Termine auch am Abend, 3 Minuten vom Bahnhof. Wir nehmen uns Zeit für die erste Abklärung."
std("2026-11-12-do-cas", "theme-gold", "Google-Profil", '750 Zeichen, die Sie <span class="gold">ganz selbst schreiben.</span>',
    [("pen", "Was Sie anbieten", "In den Worten Ihrer Kundschaft."), ("pin", "Für wen, wo", "Zielgruppe und Region."), ("star", "Was Sie unterscheidet", "Mit einem konkreten Beispiel.")],
    phone(f'<div style="font:700 28px \'Inter Tight\'">Beschreibung</div><div style="font:400 17px Inter;color:var(--muted);margin:4px 0 16px">Ihr Google-Profil</div>'
          f'<div style="min-height:250px;padding:18px;border-radius:16px;background:rgba(255,255,255,.05);border:1px solid rgba(226,192,122,.4);font:500 20px/1.45 Inter"><span id="tx"></span><span id="cur" style="display:inline-block;width:2px;height:22px;background:var(--gold);vertical-align:-3px"></span></div>'
          f'<div style="display:flex;justify-content:flex-end;margin-top:10px;font:600 17px \'JetBrains Mono\';color:var(--gold)"><span id="cn">0</span>&nbsp;/ 750</div>'
          f'<div data-a="pop" data-t="7.4" data-buzz="7.5" style="margin-top:22px;padding:14px 16px;border-radius:14px;{BAD};font:600 18px Inter">Keine Links, keine Rabattaktionen</div>', t=3.0, h=640),
    'Wann haben Sie <span class="gold">Ihre Beschreibung</span> zuletzt gelesen?', "Fiktives Beispiel", "cas", end=10.5,
    scene=f'''const D={desc!r},tx=document.getElementById('tx'),cn=document.getElementById('cn'),cu=document.getElementById('cur');
window.SCENE=t=>{{const n=Math.round(D.length*R(t,4.0,3.0));tx.textContent=D.slice(0,n);cn.textContent=n;cu.style.opacity=(Math.floor(t*2.5)%2||n<D.length)?1:0}};''')

# ---------- Cas Fr 13.11.: Barrierefreiheit ----------
def sw(lbl, t, idn):
    return (f'<div class="row" style="font:600 20px/1.3 Inter;padding:18px 0"><span style="max-width:220px">{lbl}</span><div id="{idn}" class="sw" data-tap="{t}" data-buzz="{t + .05}" data-on="{t}" '
            f'style="flex:none;width:70px;height:40px;border-radius:20px;background:#3a3a40;position:relative"><i style="position:absolute;top:4px;left:4px;width:32px;height:32px;border-radius:50%;background:#fff;display:block"></i></div></div>')
std("2026-11-13-fr-cas", "theme-gold", "Google-Profil · Barrierefreiheit", 'Ist Ihr Eingang rollstuhlgerecht? <span class="gold">Sagen Sie es Google.</span>',
    [("access", "Merkmale öffnen", "Bereich Barrierefreiheit im Profil."), ("check", "Nur was stimmt", "Lieber ehrlich: «Eingang mit 2 Stufen»."), ("door", "Foto vom Eingang", "Damit man es vorher sieht.")],
    rings(520, 540, 560, 4.4, "rgba(226,192,122,.30)") +
    phone('<div style="text-align:center"><div style="width:90px;height:90px;border-radius:50%;margin:0 auto 12px;border:1px solid rgba(226,192,122,.5);background:rgba(226,192,122,.08);display:grid;place-items:center"><svg viewBox="0 0 24 24" style="width:46px;height:46px;stroke:var(--gold);fill:none;stroke-width:1.9;stroke-linecap:round"><circle cx="12" cy="4.5" r="1.8"/><path d="M8 9h8M12 9v5l4 5M12 14l-4 5"/></svg></div>'
          '<div style="font:700 26px \'Inter Tight\'">Barrierefreiheit</div><div style="font:400 16px Inter;color:var(--muted);margin-bottom:8px">Merkmale im Google-Profil</div></div>'
          + sw("Rollstuhlgerechter Eingang", 5.0, "s1") + sw("Rollstuhlgerechte Toilette", 5.7, "s2") + sw("Rollstuhlgerechte Parkplätze", 99, "s3") +
          '<div data-a="pop" data-t="6.6" style="margin-top:18px;padding:14px;border-radius:14px;background:rgba(63,191,106,.10);border:1px solid rgba(63,191,106,.4);font:600 18px Inter;text-align:center;color:var(--green)">Erscheint direkt im Eintrag</div>', t=3.0, h=660),
    'Nicht erst <span class="gold">vor der Treppe.</span>', "Fiktives Beispiel", "cas", end=10, h1size=62, left_top=500,
    scene='''const sw=[...document.querySelectorAll('.sw')];window.SCENE=t=>{sw.forEach(e=>{const on=+e.dataset.on,p=spring(R(t,on,.4));e.style.background=t>=on?'#3f8f5a':'#3a3a40';e.firstChild.style.left=(4+30*p)+'px'})};''')
