# /li-human · Der Humanizer

Entfernt den Maschinen-Fingerabdruck aus jedem Entwurf (Gedankenstriche,
Floskeln, unsichtbare Zeichen, ß) und bewertet das Ergebnis mit fünf Prüfungen,
bevor es rausgeht. Zwei Werkzeuge, beide laufen wirklich. Benutz sie. Nicht von
Auge schätzen.

```bash
python3 werkzeuge/humanize.py entwurf.txt -o sauber.txt --report   # reinigen, Änderungen zeigen
python3 werkzeuge/detect.py sauber.txt                              # bewerten, fünf Prüfungen
python3 werkzeuge/detect.py entwurf.txt sauber.txt                  # vorher/nachher
```

(Pfade relativ zum Skill-Ordner. Der Entwurf kommt vorher in eine Textdatei im
Arbeitsordner.)

Beide lesen `werkzeuge/slop_de.json`: das deutsche Floskel-Lexikon, 17 Klassen
unsichtbarer Zeichen, die typografischen Ersetzungen und 19 Strukturmuster. Es
ist zum Bearbeiten gedacht. Benutzt digitalONLY ein Wort wirklich, das das
Lexikon entfernt, Zeile löschen.

## Was automatisch behoben wird

**1. Unsichtbare Zeichen.** Zero-Width-Spaces und -Joiner, Word-Joiner,
bedingte Trennstriche, BOMs, Unicode-Tag-Zeichen, geschützte und schmale
Leerzeichen. Keine Tastatur erzeugt sie, sie überleben Kopieren und Einfügen und
sind in jedem Editor unsichtbar.

**2. Typografie.** Geviertstrich wird Komma. Gedankenstrich ( – ) wird Komma,
zwischen Zahlen Bindestrich, als Aufzählungszeichen «- ». „Deutsche“ und
“englische” Anführungszeichen werden gerade. … wird drei Punkte. ß wird ss.
«Schweizer Guillemets» bleiben, die sind in der Schweiz normal.

**3. Floskel-Lexikon.** «in der heutigen digitalen Welt», «von entscheidender
Bedeutung», «nahtlos», «massgeschneidert», «ganzheitlich», «Game-Changer»,
«darüber hinaus», «der Schlüssel zum Erfolg» und der Rest. Ersetzt wird nur, wo
der Satz grammatikalisch hält (gleiches Genus, Endungen bleiben: «nahtlosen» wird
«reibungslosen»). Gross/klein bleibt, URLs bleiben unberührt.

## Was NICHT automatisch behoben wird

Strukturmuster werden **markiert, nicht umgeschrieben**, weil Satzbau Urteil
braucht. Im Deutschen erst recht: Wer ein Satzglied löscht, zerstört schnell die
Verbstellung.

- «Es geht nicht um X, sondern um Y» und «nicht nur X, sondern auch Y»
- «Das ist kein X. Das ist Y.»
- Dreierreihen («schnell, einfach und günstig.»)
- Enthüllungsfrage als eigene Zeile: «Das Ergebnis?»
- «Es ist wichtig zu beachten, dass», «Tauchen wir ein», «Stellen Sie sich vor»
- «aufs nächste Level», «das volle Potenzial», «Genau hier setzen wir an»
- «Wir freuen uns, mitteilen zu dürfen», «Wussten Sie, dass»
- «Fazit:», «Zusammenfassend», «Unterm Strich»
- Raketen-, Feuer-, Glühbirnen-Emoji, ✅-Listen, Hashtag-Wände
- Köder: «Was denkt ihr?», «Wer kennt's?», «Sehen Sie das auch so?»
- Gleich lange Sätze und gleich lange Aufzählungspunkte

Diese Liste ist deine Arbeit. Jede markierte Stelle von Hand umschreiben, Sinn
behalten, dann `detect.py` erneut laufen lassen. Das bringt den Score von REVIEW
auf PASS, und das kann kein Skript.

## Die fünf Prüfungen

`detect.py` bewertet fünf Signale von 0 bis 100, höher ist menschlicher:

| Prüfung | misst | so sieht Maschine aus |
| --- | --- | --- |
| SATZRHYTHMUS | Variation der Satzlänge | jeder Satz gleich lang |
| KONKRETHEIT | Zahlen, Beträge, Orte, Daten, Namen pro 100 Wörter | abstrakte Nomen, keine Zahlen |
| FLOSKELN | Lexikon-Treffer pro 100 Wörter | Standard-Wortschatz |
| FINGERABDRUCK | unsichtbare Zeichen, Striche, „“, ß pro 1000 Zeichen | typografisch perfekt |
| STIMME | Umgangssprache (mal, halt, eben, gibt's ...), ich/wir/Sie, Strukturmuster | steif, keine Person, inszenierte Enthüllungen |

Das Urteil gewichtet den Durchschnitt mit 60 % und die **schwächste einzelne
Prüfung** mit 40 %, weil ein Detektor nur ein Signal braucht. PASS braucht
gesamt 70+ und keine Prüfung unter 55.

Hinweise zum Deutschen: KONKRETHEIT zählt keine grossgeschriebenen Wörter (die
sind im Deutschen alle Nomen), sondern Zahlen, CHF, Akronyme (SEO, KMU), Marken
in Binnenmajuskel (digitalONLY, ChatGPT), Schweizer Orte, Wochentage und Monate.
STIMME misst statt englischer Kurzformen die Modalpartikeln und Verschmelzungen
der gesprochenen Sprache. Ein Satz wie «Das macht halt kaum jemand» ist
menschlicher als «Dies wird selten umgesetzt».

## Ehrlich sagen

Das sind fünf lokale Heuristiken nach den Signalen, auf die öffentliche
Detektoren achten. Sie laufen nur auf diesem Rechner, nichts wird hochgeladen.
Sie sind **nicht** GPTZero, Originality, Copyleaks, Winston oder Turnitin, rufen
diese nicht auf und können deren Urteil nicht versprechen. Das Beheben dieser
Punkte bewegt meist auch deren Zahlen, weil dieselben Dinge gemessen werden. Das
ist die ganze Behauptung. Nie sagen, ein Text sei «unerkennbar».

Der Unsichtbar-Durchgang ist echt und eng: Er entfernt Format-Zeichen, die in
generiertem Text landen. Er ist keine Behauptung über das Umgehen
kryptografischer Wasserzeichen.

## Reihenfolge

1. Entwurf in `entwurf.txt` schreiben.
2. `humanize.py entwurf.txt -o sauber.txt --report`
3. Die Strukturmuster lesen. Diese Zeilen selbst umschreiben, in `sauber.txt`.
4. `detect.py entwurf.txt sauber.txt` für vorher/nachher.
5. Kein PASS: die im Output genannte schwächste Prüfung beheben und nochmals.
   Zwei Runden sind normal. Fünf heisst, der Entwurf ist nach Schema
   geschrieben, dann hilft ein neuer Entwurf, nicht mehr Durchgänge.
6. Dem Menschen den bereinigten Text und den Score zeigen. Nie nur den Score.

**Ohne Python** (z.B. in einer Umgebung ohne Code-Ausführung): Regeln oben von
Hand anwenden, Score weglassen und sagen, dass er nicht gemessen wurde.
