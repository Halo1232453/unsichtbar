# /li-visual · Bild und Video im Premium-Stil

Macht zu einem Beitrag ein Standbild und ein Video mit haptischen Bewegungen
im dunklen digitalONLY-Stil und hängt beides in der Zentrale an. Aufruf aus
der Zentrale: `/li-visual <post-id>` (Auftrag unter «Details» kopieren).

## Der Stil

- **Format:** 4:5, 1080 × 1350. Standbild als PNG in doppelter Auflösung,
  Video als MP4, 30 fps, 10 bis 13 Sekunden, ohne Ton (Feed spielt stumm).
- **Fläche:** fast Schwarz mit Lichtschein. Drei Themen: `theme-red`
  (Warnung, Fehler, Verlust), `theme-gold` (Geld, Bewertungen, Fragen an
  den Leser), `theme-blue` (Google Maps, Karten, KI), optional Raster.
- **Aufbau von oben:** Logo weiss · Eyebrow mit rotem Punkt und gesperrter
  Schrift · Überschrift in Inter Tight, 2 bis 3 Zeilen, die Pointe in der
  Akzentfarbe · ein Motiv (Glas-Karten, Handy, Karte, Rechnung, Liste mit
  Icon-Kacheln) · eine Schlusszeile aus dem Beitrag · Fusszeile.
- **Fusszeile rechts je Konto:** Seite `digital-only.ch` · Bertan
  `Bertan Findik · digital-only.ch` · Kyrill `Kyrill Elsensohn · digital-only.ch`
  · Cas `Cas · digital-only.ch`. Links: «Fiktives Beispiel» oder «Fiktive
  Darstellung», sobald Zahlen, Namen, Bildschirme oder Antworten nur zur
  Illustration sind.
- **Bewegung (haptisch):** Wörter federn einzeln ein, Karten gleiten mit
  Feder-Überschwingen herein, wichtige Momente vibrieren kurz (`data-buzz`),
  Tipps zeigen eine Welle und ein Einfedern (`data-tap`), Puls-Ringe hinter dem
  Hauptmotiv (`data-rings`), Stempel knallen (`slam`), Balken und Sterne
  füllen sich nacheinander. Eine Bewegung pro Aussage, im Takt des Texts.

## Regeln

- Nur Inhalte aus dem Beitrag. Keine Zahl, kein Kunde, kein Zitat, das nicht im
  Text oder in voice.md «Belege» steht. Platzhalter wie `{Betrag}` kommen nie
  ins Bild: die Stelle weglassen.
- Kein Google-Logo und keine nachgebauten Original-Oberflächen. Schlichte
  Mockups mit «Fiktive Darstellung».
- Bereits gepostete Beiträge nicht neu gestalten.

## Ablauf

1. Beitrag aus der Zentrale lesen (`ArtifactData` `get`, `posts/<id>`).
2. Motiv in `linkedin-visuals/scenes.py` als neuen Eintrag `SCENES["<id>"]`
   anlegen (Vorlagen: die vier bestehenden Motive), dann im Ordner
   `linkedin-visuals`: `python3 build.py`, `node render.js <id> still`,
   Standbild ansehen, `node render.js <id> video`.
3. Beide Dateien mit dem Artifact-Werkzeug hochladen (`asset: true`,
   `url` = Zentrale) und per `ArtifactData` `update` mit `if_version` in
   `medien` eintragen: Video zuerst, dann Bild. Feld `visual: "premium"` setzen.
4. Kurz melden, was im Bild steht und was fiktiv ist.
