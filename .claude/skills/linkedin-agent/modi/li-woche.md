# /li-woche · Wochen-Autopilot

Plant die Woche und schreibt alle Beiträge in einem Durchgang, fertig
humanisiert, und legt sie in der Agent-Zentrale ab. Läuft von Hand («/li-woche»)
oder als geplante Aufgabe jeden Freitag für die folgende Woche. Veröffentlicht
wird nichts: Bertan prüft, ersetzt Platzhalter und plant die Beiträge in
LinkedIn selbst (Uhr-Symbol im Editor).

## 1. Vorbereiten

1. Stimme lesen, wie in SKILL.md beschrieben (zuerst `config/stimme` in der
   Zentrale): Rhythmus, Positionen, Tabus, Belege, Themen-Pfeiler. Stellen mit
   «[bitte prüfen]» sind unbestätigt: als Richtung verwenden, aber keine Aussage
   daraus als Fakt formulieren.
2. `daten/hooks.json` lesen.
3. **Zielwoche bestimmen.** Standard: die Kalenderwoche ab dem nächsten Montag.
   Ausnahme: Läuft es am Montag vor 10 Uhr, ist es die laufende Woche. Die
   Slots kommen aus voice.md «Rhythmus» (Standard Di 08:15, Mi 12:15, Do 08:00).
4. **Zentrale lesen** (URL in SKILL.md), wenn das Werkzeug
   `ArtifactData` verfügbar ist (sonst überspringen):
   - `list` auf `posts`: alle Beiträge. Daraus: was ist in der Zielwoche schon da
     (diese Slots nicht neu schreiben), welche Themen und Hook-Nummern liefen in
     den letzten drei Wochen (nicht wiederholen).
   - `list` auf `ideen`: alle mit `status: "neu"`. Das sind echte Erlebnisse von
     Bertan und haben Vorrang vor allen eigenen Themen.
   - Ist die Zielwoche schon komplett, nichts schreiben. Nur kurz melden.

## 2. Planen

Pro offenem Slot: Typ, Themen-Pfeiler, konkreter Winkel, Hook-Nummer.

- Typen mischen (WISSEN, MEINUNG, dazu GESCHICHTE, BELEG oder ANGEBOT im
  Wechsel), nie zwei gleiche hintereinander, drei verschiedene Hook-Formeln.
- Ideen aus der Zentrale zuerst verwenden. Eine Idee pro Beitrag.
- Ohne Ideen: Themen-Pfeiler rotieren. WISSEN-Beiträge erklären allgemein
  gültiges, überprüfbares Wissen (z.B. wie Google-Profile funktionieren). Nur
  schreiben, was sicher stimmt. Im Zweifel weglassen.
- **Aktueller Anlass (optional):** Eine Websuche nach Änderungen bei Google
  Maps, Google-Unternehmensprofil, Google Ads oder KI-Suche aus den letzten 30
  Tagen. Nur verwenden, wenn eine offizielle Quelle (Google-Blog, Google-Hilfe,
  Anbieter selbst) es bestätigt. Quelle in die Notiz des Beitrags, nicht in den
  Text. Kein Gerücht, keine Spekulation.
- **Nie erfinden:** Keine Kundenergebnisse, Zahlen, Szenen oder Zitate, die
  nicht aus voice.md «Belege» oder einer Idee stammen. Eine GESCHICHTE ohne echte
  Idee wird nicht geschrieben, dann lieber WISSEN oder MEINUNG. Ein BELEG ohne
  echte Zahl bekommt `{Zahl}` und eine Markierung.

## 3. Schreiben

Jeden Beitrag nach `modi/li-post.md` (Form, Länge 900 bis 1300 Zeichen, eine
Idee, Schlussfrage oder Aufforderung, höchstens drei Hashtags, Link nur im ersten
Kommentar). Dann jeden durch `modi/li-human.md`:

```bash
python3 werkzeuge/humanize.py di.txt -o di_sauber.txt --report
python3 werkzeuge/detect.py di.txt di_sauber.txt
```

Gemeldete Strukturmuster von Hand umschreiben und erneut messen, bis PASS
(höchstens drei Runden, sonst neuer Entwurf). Platzhalter wie `{Zahl}` bleiben
stehen, auch wenn sie den Score drücken.

Die drei Beiträge nebeneinander lesen: Klingen sie gleich (gleicher Einstieg,
gleiche Länge, gleiche Schlussfrage), einen umschreiben.

## 4. In der Zentrale ablegen

Mit `ArtifactData` (`batch`, ein Aufruf) auf die Zentrale-URL schreiben. Pro
Beitrag ein Dokument `posts/<JJJJ-MM-TT>-<tag>` (tag klein: mo, di, mi, do, fr):

```json
{
  "datum": "2026-10-20",
  "tag": "Di",
  "zeit": "08:15",
  "woche": "2026-W43",
  "typ": "WISSEN",
  "hook": "#5 Listen-Versprechen",
  "titel": "3 Felder, die Praxen im Google-Profil leer lassen",
  "text": "<der humanisierte Beitrag, genau so, wie er gepostet wird>",
  "erster_kommentar": "<optional, z.B. Link mit einem Satz, sonst leer>",
  "platzhalter": ["{Zahl} in Absatz 3"],
  "score": 82.4,
  "urteil": "PASS",
  "notiz": "<optional: Quelle, Hinweis an Bertan>",
  "status": "entwurf",
  "quelle": "autopilot",
  "idee_id": "<ID der verwendeten Idee oder leer>",
  "erstellt": "<ISO-Zeitstempel>"
}
```

Verwendete Ideen im selben `batch` mit `update` auf `{"status": "verwendet",
"verwendet_in": "<post-id>"}` setzen. Dazu `meta/autopilot` mit `set`:
`{"letzter_lauf": "<ISO>", "zielwoche": "2026-W43", "anzahl": 3,
"hinweis": "<ein Satz>"}`.

Nie bestehende Beiträge überschreiben, deren Status nicht `entwurf` ist.

## 5. Zustellen

Kurze Nachricht an Bertan:

```
3 Entwürfe für die Woche vom 20. Oktober liegen in der Zentrale.

DI 08:15  WISSEN   #5   3 Felder, die Praxen im Google-Profil leer lassen   PASS 84
MI 12:15  MEINUNG  #1   Warum die neue Website oft das Falsche ist          PASS 79
DO 08:00  WISSEN   #15  Feiertage im Google-Profil                          PASS 81

Platzhalter: Di hat {Zahl} in Absatz 3.
Ablauf: prüfen, Platzhalter ersetzen, in LinkedIn einfügen und mit dem
Uhr-Symbol planen, in der Zentrale auf «Geplant» setzen.
```

Darunter jeden Beitrag als Codeblock, damit er auch ohne Zentrale kopiert werden
kann. Ohne Zentrale (kein `ArtifactData`, keine URL): nur so ausgeben.
