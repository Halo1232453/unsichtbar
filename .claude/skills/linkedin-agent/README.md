# LinkedIn-Agent · digitalONLY AG

Projektlokal installierter Claude-Skill (`.claude/skills/linkedin-agent/`).
Claude Code lädt ihn automatisch, sobald eine Session in diesem Repo startet.
Einstieg: `SKILL.md`. Befehle: `/li-post`, `/li-comment`, `/li-reply`,
`/li-profile`, `/li-plan`, `/li-human`, `/li-carousel`, `/li-repurpose`,
`/li-dm`, `/li-inbox`, `/li-audit`, `/li-woche`.

## Zuerst

`voice.md` prüfen und alle Stellen mit **[bitte prüfen]** bestätigen oder
streichen. Ohne Belege kommt jeder Entwurf mit `{Zahl}` zurück.
Global nutzen: Ordner nach `~/.claude/skills/` kopieren und `voice.md` nach
`~/.claude/linkedin/voice.md`.

## Humanizer (Python 3, keine Abhängigkeiten)

```bash
python3 werkzeuge/humanize.py entwurf.txt -o sauber.txt --report
python3 werkzeuge/detect.py sauber.txt
python3 werkzeuge/detect.py entwurf.txt sauber.txt   # vorher/nachher
```

`detect.py` endet mit Exit-Code 1, solange das Urteil nicht PASS ist.

## Agent-Zentrale

`zentrale.html` ist die Seite der Agent-Zentrale (Wochenplan, Ideen, Stimme),
gedacht als Claude-Artifact mit Datenbank (`ArtifactData`). Die in `SKILL.md`
hinterlegte Zentrale-URL muss für das jeweilige Claude-Konto erreichbar sein,
sonst nutzt der Agent `voice.md` und `~/.claude/linkedin/log.md`.

Der Agent veröffentlicht nie selbst. Jeder Modus endet mit einem
kopierfertigen Block, der Mensch postet.

Adaptiert von «linkedin-agent-skill» (Jake Schincariol, MIT).
