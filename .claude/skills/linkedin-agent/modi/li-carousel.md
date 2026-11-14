# /li-carousel · Dokument-Beiträge (Karussell)

Dokument-Beiträge haben auf LinkedIn die längste Lesezeit, weil jedes Wischen
zählt. Das Format belohnt eine Idee in Schritten. Es bestraft einen Textbeitrag,
der in Stücke geschnitten wurde.

## Wann statt eines Textbeitrags

Ein Karussell, wenn die Idee eine **Abfolge** hat: Schritte, Countdown,
Vorher/Nachher, ein Modell mit Teilen (z.B. «Die 7 Felder im Google-Profil, in
Reihenfolge ihrer Wirkung»). Ein Textbeitrag, wenn die Idee eine Behauptung ist.
Eine Behauptung auf acht Folien zu verteilen ist der häufigste Grund, warum
Karussells scheitern. Wenn das vorliegt, sagen und an /li-post übergeben.

## Aufbau

8 bis 12 Folien. Unter 8 ist es ein Textbeitrag. Über 12 fällt die
Abschlussrate stark ab.

```
1        TITEL       der Hook, höchstens 6 Wörter, plus eine Zeile Versprechen
2        EINSATZ     warum es zählt, in einem Satz
3-N      EINE IDEE PRO FOLIE. Überschrift 3-7 Wörter, darunter höchstens 25 Wörter.
                     Braucht eine Folie einen Absatz, sind es zwei Folien.
N+1      ÜBERSICHT   alles als Liste, damit der Screenshot nützlich ist
LETZTE   AUFRUF      eine Handlung. Folgen, ein Stichwort kommentieren, oder der Link. Eine.
```

## Regeln für den Folientext

- **Folie 1 ist 80 % des Ergebnisses.** Sechs Wörter. Gross. Der Rest kann einen
  Titel nicht retten, bei dem niemand wischt.
- **Jede Folie nummerieren** (3/10). Die Abschlussrate steigt, wenn man das Ende
  sieht.
- **Keine Folie ist ein Absatz.** Nicht in 25 Wörtern sagbar: teilen.
- **Die Übersichtsfolie wird gescreenshottet.** Sie muss allein stehen.
- **Absender auf jeder Folie**, klein, unten in der Ecke (digitalONLY AG bzw.
  Website). Screenshots reisen ohne euch.

## Das PDF bauen

LinkedIn will ein PDF, 1080×1350 (4:5) für die grösste Fläche im Feed, unter
100 MB, unter 300 Seiten. Als HTML bauen und als PDF drucken:

- Eine `<section>` pro Folie, `width:1080px; height:1350px;
  page-break-after:always`, keine Ränder.
- Eine Akzentfarbe. Schrift nicht kleiner als 28px, gelesen wird auf dem Handy
  in Daumennagel-Grösse.
- Markenfarben und Schrift aus `voice.md` (Abschnitt «Marke»). Fehlen sie: einmal
  fragen, keine Palette erfinden.
- Umwandeln mit dem, was da ist: Chrome/Chromium headless (`--print-to-pdf`),
  Playwright oder WeasyPrint. Danach eine Seite als Bild prüfen.

## Ausgabe

Erst den Folientext als nummerierte Liste, in zehn Sekunden lesbar. Dann den
**Begleittext**: Auch ein Karussell braucht 2 bis 3 Zeilen darüber, das ist der
eigentliche Hook im Feed. Beides durch `modi/li-human.md`. Das PDF erst bauen,
wenn der Mensch den Text freigibt.

Nichts wird bei LinkedIn hochgeladen. Der Mensch postet das PDF selbst.
