# LinkedIn-Videos · digitalONLY

`2026-11-10-verzeichnis-abo-test.mp4`: Testvideo zu Kyrills Beitrag über
Verzeichnis-Abos. Hochformat 1080 × 1920 (9:16), 30 fps, 45 s, H.264/AAC,
Untertitel eingebrannt (die meisten schauen ohne Ton).

## Wie es entsteht (`quelle/`)

1. **Sprechtext** in `segs.json`, ein Eintrag pro Satz.
2. **Stimme:** `synth.py` vertont jeden Satz mit Piper (Open Source, offline).
   Testsstimme: «Thorsten» (deutsch, low), Download:
   https://github.com/rhasspy/piper/releases/download/v0.0.2/voice-de-thorsten-low.tar.gz
   `pip install piper-tts`, dann `python3 synth.py de-thorsten-low.onnx segs.json`.
   Danach Sätze mit Pausen zu `voice.wav` zusammensetzen (`timeline.json` enthält
   die Start- und Endzeiten jedes Satzes) und mit ffmpeg normalisieren.
3. **Animation:** `anim.html` ist ein Template. `__TL__` wird durch den Inhalt
   von `timeline.json` (plus Feld `cap` für die Untertitel) ersetzt;
   `render(t)` zeichnet das Bild zum Zeitpunkt t. `logo.png` aus
   `.claude/skills/linkedin-agent/assets/logo-digitalonly.png` daneben legen.
4. **Rendern:** `node render.js full 30 <dauer>` schreibt Einzelbilder nach
   `frames/`, dann:
   `ffmpeg -framerate 30 -i frames/f%05d.jpg -i voice48.wav -c:v libx264 -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -shortest -movflags +faststart video.mp4`

Die Teststimme ist synthetisch. Für echte Beiträge Kyrills eigene Stimme
aufnehmen oder einen lizenzierten Sprachdienst verwenden; die Taktung kommt
dann aus den gemessenen Satzlängen der Aufnahme.
