# Englische Fassungen der Workspace-Videos (A Ausfall, B Umzug) für Seite und Kyrill.
from scenes import SCENES
import scenes_workspace as W

T = [
 (W.HOOK, 'Outlook went down last night. <span class="red">You could only watch.</span>'),
 ("Stand 13.11.2026 · Quellen: ORF, CNBC, The Register", "As of 13 Nov 2026 · Sources: ORF, CNBC, The Register"),
 ("Fiktive Darstellung", "Illustration"),
 ("Microsoft-365-Ausfall", "Microsoft 365 outage"),
 ("Do 12.11. ab ca. 19 Uhr: Outlook, Teams, SharePoint", "Thu 12 Nov, from ~7 pm CET: Outlook, Teams, SharePoint"),
 ("Fr 13.11.: Störung dauert an", "Fri 13 Nov: still disrupted"),
 ("Januar: schon einmal, fast 10 Stunden", "January: almost 10 hours"),
 ("● Seit Do 12.11., ca. 19 Uhr gestört", "● Disrupted since Thu 12 Nov, ~7 pm CET"),
 ("Würden Sie Microsoft 365 nochmals wählen?", "Switch or stay: what's actually safer?"),
 (">Ja, klar<", ">Stay with Microsoft<"), (">Nein, nie mehr<", ">Switch to Google<"),
 ("Ihre Antwort? In den Kommentaren.", "Your answer? In the comments."),
 ("Illustration, keine echten Umfragewerte", "Illustration, not real poll data"),
 (">Umfrage<", ">Poll<"), (">Posteingang<", ">Inbox<"),
 ("Verbindung wird hergestellt …", "Connecting …"),
 ('Wir holen Sie rüber zu <span class="gold">Google Workspace.</span>', 'We\'ll move you to <span class="gold">Google Workspace.</span>'),
 ("Wechsel-Check · Link im Kommentar", "Switch check · link in comments"),
 (">Wechsel-Check<", ">Switch check<"), (">Erster Montag<", ">First Monday<"),
 (">Heute<", ">Today<"), (">Ziel<", ">Goal<"),
 (">Postfächer<", ">Mailboxes<"), (">Kalender<", ">Calendars<"), (">Kontakte<", ">Contacts<"), (">Dateien<", ">Files<"),
 (">Umzug<", ">Migration<"),
 ("rgba(63,191,106,.18)", "rgba(80,140,255,.24)"), ("rgba(255,90,74,.20)", "rgba(226,192,122,.28)"),
]
JT = [("'Keine Verbindung zum Server'", "'Cannot connect to server'"), ("'Verbindung wird hergestellt …'", "'Connecting …'")]


def tr(s, pairs):
    for a, b in pairs:
        s = s.replace(a, b)
    return s


for konto, suf in (("seite", ""), ("kyrill", "-kyrill")):
    for var, fn, js, theme in (("", W.body_a, W.JS_A, "theme-red"), ("-b", W.body_b, W.JS_B, "theme-gold")):
        body = tr(fn(konto), T)
        # Kalender-Icon «31» und Text dürfen nicht verwechselt werden; Reste prüfen
        for de in ("Posteingang", "Umfrage", "Postfächer", "Kontakte", "Wechsel-Check", "Stand 13.11", "nochmals"):
            assert de not in body, (konto, var, de)
        SCENES[f"2026-11-13-fr-workspace{var}{suf}-en"] = dict(theme=theme, grid=False, end=11, body=body, scene=tr(js, JT))
