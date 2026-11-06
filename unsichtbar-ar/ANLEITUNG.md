# Unsichtbar · AR-Ausstellung

Fertiges WebAR-Projekt mit drei Stationen. Besucher scannen am Eingang einen QR-Code, tippen auf «Kamera starten» und halten das Handy auf ein Plakat. Dann läuft das passende Faktenvideo direkt auf dem Plakat. Keine App nötig.

## Was drin ist

| Ordner / Datei | Inhalt |
|---|---|
| `index.html` | Die AR-Seite. Oben im Script stehen alle Texte und Einstellungen |
| `ar.js` | Die Effekte (Scan, Karten, 3D-Objekte, Partikel, Quiz). Muss man normalerweise nicht anfassen |
| `vorschau.html` | Alle Videos ohne Kamera (Backup, falls AR nicht klappt) |
| `quellen.html` | Alle Quellen mit Links |
| `eingang.html` | Eingangsschild A4 mit QR-Code, wird automatisch erzeugt |
| `plakate/` | Die drei Plakate als PNG und als Druck-PDF (A3). `plakate/web/` sind kleine Versionen für den Scan-Effekt |
| `videos/` | Die drei Faktenvideos (stumm, ca. 45 Sekunden) |
| `targets/targets.mind` | Erkennungsdaten der drei Plakate |
| `lib/` | A-Frame 1.5.0, MindAR 1.2.5, QR-Code (alles lokal, läuft ohne CDN) |
| `karten/` | Die alten Karten-Bilder. Werden nicht mehr gebraucht, die Karten werden jetzt live gezeichnet |

## Online stellen (GitHub Pages, ca. 10 Minuten)

1. Auf github.com ein neues öffentliches Repository erstellen, z. B. `unsichtbar`.
2. «uploading an existing file» wählen und den **Inhalt** dieses Ordners hineinziehen (nicht den Ordner selbst).
3. Settings > Pages > Branch `main`, Ordner `/ (root)` > Save.
4. Nach 1 bis 2 Minuten ist die Seite unter `https://DEINNAME.github.io/unsichtbar/` erreichbar.

Die Kamera funktioniert nur über https. Deshalb nicht die Datei direkt doppelklicken.

## Lokal testen in VS Code

Extension «Live Server» installieren, `index.html` rechtsklicken > «Open with Live Server». Auf dem Laptop kannst du die Plakate auf einem zweiten Bildschirm oder dem Handy anzeigen und die Webcam darauf halten.

## Drucken

- `plakate/plakate-A3-druck.pdf` auf A3 oder grösser drucken, **matt**, damit nichts spiegelt.
- Die Plakate genau so drucken, wie sie sind. Wenn du am Plakat etwas änderst, erkennt die Kamera es nicht mehr (siehe unten).
- `eingang.html` über die **Online-Adresse** öffnen und drucken. Der QR-Code zeigt dann automatisch auf eure Seite.

## Eigene Videos einsetzen

Einfach die Dateien in `videos/` ersetzen, gleicher Name. Am besten Hochformat 720 × 1018 Pixel (Seitenverhältnis wie das Plakat), MP4, unter 10 MB. Videos mit Ton starten auf dem Handy erst nach einem Tippen, deshalb sind diese hier stumm.

## Plakate ändern

Wenn ihr ein Plakat neu gestaltet, muss `targets/targets.mind` neu erzeugt werden:

1. MindAR Compiler öffnen: https://hiukim.github.io/mind-ar-js-doc/tools/compile
2. Die drei Plakate **in der Reihenfolge 01, 02, 03** hochladen, «Start» klicken.
3. Die Datei herunterladen und als `targets/targets.mind` speichern.

Gute Plakate für die Erkennung haben viele Details, harte Kanten und keine sich wiederholenden Muster.

## Tipps für den Ausstellungstag

- Gutes, gleichmässiges Licht auf die Plakate, keine Spots, die blenden.
- Plakate auf Augenhöhe, ca. 1 bis 2 Meter Abstand zum Betrachter.
- WLAN oder Handyempfang vor Ort prüfen. Die Seite lädt ca. 4 MB.
- Ein Tablet mit `vorschau.html` bereitlegen, falls jemand kein passendes Handy hat.
- Getestet mit Chrome. Auf dem iPhone in Safari öffnen.

## Was passiert, wenn ein Plakat erkannt wird

1. **Scan:** Eine rote Linie fährt über das Plakat, die Höhenlinien leuchten auf («Unsichtbares wird sichtbar»).
2. **3D-Objekt:** Aus der Mitte wächst ein Objekt und öffnet sich: ein Akku mit Lithium und Kobalt (01), ein T-Shirt, das sich mit 2'700 l Wasser füllt (02), eine Kakaoschote, die aufklappt (03). Danach schwebt es rechts unten weiter.
3. **Karten:** Titel und Fakten-Karten fliegen aus dem Plakat und klappen auf, rote Linien verbinden sie mit dem Plakat. Die Zahlen zählen von 0 hoch.
4. **Partikel:** Salzkristalle steigen auf (01), Textilfasern ziehen vorbei (02), Kakaobohnen fallen (03).
5. **Video:** Das Video hebt sich mit einem Schatten aus dem Plakat.
6. **Frage:** Unten erscheint die Frage.

Antippen kann man:
- **Fakten-Karten:** drehen sich um und zeigen auf der Rückseite einen weiteren Fakt (alles aus `quellen.html`).
- **Frage:** klappt ein Quiz mit drei Antworten auf.
- **3D-Objekt:** fliegt nochmals in die Mitte und spielt die Animation erneut ab.

## Texte und Einstellungen ändern

Alles steht in `index.html` ganz oben im Script:

- `STATIONS`: alle Texte pro Station, also Fakten (`big` = grosse Zahl, `text`, `src` = Quelle), Rückseite (`more`, `moreSrc`), Frage und Quiz (`right` = Nummer der richtigen Antwort, gezählt ab 0).
- `LAYOUT`: Positionen der Karten und wann sie erscheinen.
- `TIMING`: Ablauf in Millisekunden.
- `MODEL_REST`: wo das 3D-Objekt nach seinem Auftritt schwebt.

Tipp: Einen Schritt zurück gehen, damit man alle Karten sieht.

## Testen ohne Kamera und Plakat

`index.html?demo` öffnen (auf der Startseite der Link «Effekte testen»). Dann läuft alles mit einem virtuellen Plakat. Oben links wechselst du die Station (oder Tasten 1, 2, 3). Bewegst du die Maus, kippt das Plakat leicht, damit man die Tiefe sieht.

## Videos mit durchsichtigem Hintergrund

Wenn du ein Video mit Greenscreen hast (z. B. eine Person, die aus dem Plakat tritt), trage bei der Station `chroma: '#00ff00'` ein. Dann wird das Grün durchsichtig.

## Plakat kurz verloren

Wenn die Kamera das Plakat verliert (Wackeln, jemand läuft durchs Bild), bleibt alles stehen und das Video läuft weiter. Erst wenn das Plakat 6 Sekunden lang nicht mehr im Bild ist, wird es zurückgesetzt. Die Zeit stellst du in `index.html` bei `GRACE_MS` ein (6000 = 6 Sekunden).
