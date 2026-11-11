# LinkedIn-Visuals · Premium-Stil

Standbilder und Videos mit haptischen Bewegungen für LinkedIn-Beiträge,
4:5 (1080 × 1350). Anleitung und Regeln: `.claude/skills/linkedin-agent/modi/li-visual.md`.

- `engine.html` Stil und Bewegungs-Engine (`render(t)`)
- `scenes.py` ein Motiv pro Beitrag (Schlüssel = ID in der Zentrale)
- `build.py` erzeugt `build/<id>.html`
- `render.js <id> still|video` schreibt `out/<id>.png` bzw. `out/<id>.mp4`

Braucht Python 3, Node mit Playwright (Chromium) und ffmpeg.
