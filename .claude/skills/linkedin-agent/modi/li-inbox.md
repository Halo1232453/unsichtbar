# /li-inbox · Triage im Posteingang

Die meisten LinkedIn-Posteingänge sind zu 80 % Rauschen, und dieses Rauschen
kostet, dass die wichtigen 20 % eine Woche liegen bleiben. Dieser Modus trennt
sie und schreibt nur, was sich lohnt.

Gilt für Bertans persönlichen Posteingang und für Nachrichten an die
Unternehmensseite.

## Eingabe

Der Mensch fügt die Nachrichten ein. Screenshots gehen. Sich nicht ins Konto
einloggen und den Posteingang nicht per Browser lesen.

## In fünf Töpfe

| Topf | Signal | Handlung |
| --- | --- | --- |
| **LEAD** | beschreibt ein Problem, das digitalONLY löst, oder fragt nach Zusammenarbeit | heute antworten, vollständig |
| **RECRUITER** | eine Stelle, eine Firma, ein Lohnband | antworten, wenn die Stelle echt ist, sonst eine Zeile |
| **KOLLEGE** | jemand aus dem Feld mit etwas zu sagen | diese Woche antworten, menschlich |
| **BITTE** | will Rat, Zeit, eine Vorstellung, einen Gefallen | antworten, wenn es günstig und konkret ist, sonst sauber absagen |
| **SPAM** | Agentur-Pitch, Leadgen-Serie, Krypto, «kurze Frage» ohne Frage | archivieren, keine Antwort |

Zuerst die Anzahl ausgeben. «3 Leads, 2 Recruiter, 41 Spam» zu sehen ist schon
der grösste Teil des Nutzens.

## Automatische Serien erkennen

Automatisierte Akquise hat eine Form: Vernetzungsnotiz ohne Bezug, eine
Nachricht Minuten nach dem Annehmen, «kurze Frage», «Ich habe gesehen, dass Sie
in der {Branche} tätig sind», ein Kalenderlink in Nachricht eins, dann genau vier
Tage später ein Nachfassen. Wenn erkannt: SPAM und sagen, welches Merkmal es
verraten hat. Einem Skript schuldet man keine Antwort.

## Antworten

- **LEAD**: die Frage in der Nachricht vollständig beantworten, gratis. Passt
  es, ist das Angebot ein Satz am Ende. Passt es nicht, das sagen und weiterhelfen.
  Beides ist ein gutes Ergebnis.
- **RECRUITER**: ist die Stelle interessant, nach dem fragen, was fehlt
  (Lohnband, Stufe, Pensum, vor Ort oder nicht). Sonst eine Zeile: kein Interesse,
  empfehle gern jemanden, und das ernst meinen.
- **BITTE**: kostet es unter zehn Minuten und ist konkret, machen. Ist es «Kann
  ich Sie mal kurz anzapfen», mit einem warmen Satz absagen und die eine Antwort
  geben, die man im Gespräch gegeben hätte. Höflicher und nützlicher.
- **ABSAGEN** sind kurz, warm und endgültig. Kein «Kommen wir im Q3 darauf
  zurück», wenn es kein Q3 gibt.

## Ausgabe

Nach Töpfen gruppiert, Anzahl zuerst, Entwürfe nur für die Töpfe, die eine
Antwort bekommen, jeder humanisiert (`modi/li-human.md`). Dann das Tor: Der Mensch
schickt sie.

```
POSTEINGANG  ·  52 Nachrichten  ·  3 LEAD, 2 RECRUITER, 4 KOLLEGE, 2 BITTE, 41 SPAM

SPAM  (41) - archivieren. 38 davon dieselbe Serie: Notiz ohne Bezug,
«kurze Frage» 4 Minuten nach dem Annehmen, Kalenderlink in Nachricht eins.
```
