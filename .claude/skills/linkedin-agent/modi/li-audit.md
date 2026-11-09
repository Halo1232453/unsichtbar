# /li-audit · Was hat wirklich gewirkt

Die einzige ehrliche Quelle dafür, was bei einem Konto funktioniert, ist dieses
Konto. Jede Regel in jedem LinkedIn-Ratgeber, auch in diesem Agenten, ist eine
Annahme. Die letzten 30 eigenen Beiträge sind der Beweis.

## Eingabe

Was vorhanden ist:

- Der Analytics-Export der Seite bzw. des Profils (LinkedIn: Analysen, Inhalte,
  Export). CSV oder XLSX.
- Oder ein Screenshot pro Beitrag mit Impressionen, Reaktionen, Kommentaren,
  Reposts.
- Oder nur die Beiträge mit Reaktionszahlen, reicht für einen ersten Durchgang.

Dazu `log.md` bzw. die Beiträge in der Agent-Zentrale lesen, dort steht, welche
Hook-Formel jeder Beitrag benutzt hat.

## Was wirklich gemessen wird

Reine Impressionen sind die am wenigsten nützliche Zahl, weil sie vor allem
davon abhängen, wie viele schon folgen. Stattdessen das hier, mit Rechenweg:

| Kennzahl | wie | sagt |
| --- | --- | --- |
| **Interaktionsrate** | (Reaktionen + Kommentare + Reposts) / Impressionen | ob der Beitrag seine Reichweite verdient hat |
| **Kommentar-Quote** | Kommentare / Reaktionen | ob er etwas ausgelöst hat oder nur ein Nicken |
| **Reichweiten-Faktor** | Impressionen / Follower | ob er über das bestehende Publikum hinausging |
| **Speichern/Senden** | falls verfügbar | der stärkste Einzelhinweis auf künftige Reichweite |

Nach Interaktionsrate und Reichweiten-Faktor ordnen, nicht nach Impressionen.
Ein Beitrag mit 900 Impressionen und 40 Kommentaren hat den mit 12'000 und 6
geschlagen.

Für die Unternehmensseite zusätzlich: Klicks auf die Seite und auf die Website,
und neue Follower pro Beitrag. Das ist das eigentliche Ziel (Leute aufs Profil
bringen).

## Dann das Muster finden

Die Top 5 und die Flop 5 nebeneinander, und schauen, was sie wirklich trennt.
Bereit sein, etwas zu folgern, das dem Menschen nicht gefällt:

- Hook-Formel. Welche Nummern aus `hooks.json` sind in den Top 5?
- Format. Text, Dokument, Bild, Video.
- Länge.
- Thema (Google Maps, Google Ads, KI-Sichtbarkeit, Branche).
- Tag und Uhrzeit, **zuletzt** prüfen, und nur, wenn die anderen vier nichts
  zeigen. Fast nie die Ursache, und genau dort will man sie haben.
- Kommentare in der ersten Stunde. Beiträge, bei denen innert einer Stunde
  geantwortet wurde, gegen die anderen.

Die Erkenntnis als Behauptung mit Beleg formulieren und sagen, wie sicher sie
ist. Mit 30 Beiträgen sieht man ein Muster. Mit 6 nicht, und dann das sagen,
statt eines zu erfinden.

## Ausgabe

```
AUSWERTUNG  ·  31 Beiträge  ·  12. Juni bis 5. September

TOP 5 NACH INTERAKTIONSRATE
  8.1 %  #3  Fehler      «4 Monate falscher Ads-Radius»        1'940 Impr.
  6.4 %  #20 Rückzug     «Wir haben das Abo gekündigt»         2'210 Impr.
  ...

FLOP 5
  0.4 %  #5  Liste       «7 Tools, die jedes KMU braucht»     11'400 Impr.
  ...

WAS DIE DATEN SAGEN
1. Beiträge, in denen ihr selbst schlecht ausseht: Schnitt 6.2 % gegen 1.1 %
   bei allen anderen. n=6. Stärkstes Signal, und es ist nicht knapp.
2. Tool-Listen bringen Impressionen und sonst nichts. Drei der Flop 5.
3. Wochentag zeigt nichts. Dienstag und Freitag liegen im Rauschen.

AUFHÖREN: Tool-Listen.
MEHR DAVON: Beiträge mit einem Preis, den ihr bezahlt habt, und einer Zahl.
```

(Beispielzahlen oben sind Illustration, nicht echte Daten.)

Dann die Folgerungen an /li-plan geben, damit der nächste Wochenplan auf euren
eigenen Daten steht statt auf Standardwerten.
