#!/usr/bin/env python3
"""
detect.py - fünf Prüfungen, die bewerten, wie maschinell ein Entwurf wirkt.
Deutsche Fassung (Schweiz) von detect.py aus linkedin-agent-skill
(Jake Schincariol, MIT).

Was das ist:  fünf lokale Heuristiken, nachgebaut nach den Signalen, auf die
öffentliche KI-Detektoren achten: Variation der Satzlänge, Konkretheit,
Floskel-Wortschatz, typografischer Fingerabdruck und Stimme. Alles wird auf
diesem Rechner aus dem Text allein berechnet. Nichts wird hochgeladen.

Was das NICHT ist:  GPTZero, Originality, Copyleaks, Winston oder Turnitin.
Es ruft keine dieser Schnittstellen auf und kann deren Urteil nicht
versprechen. Es misst dieselben zugrunde liegenden Dinge, deshalb bewegt das
Beheben dieser Punkte meist auch deren Zahlen. Mehr wird nicht behauptet.

Anpassungen für Deutsch:
  - KONKRETHEIT zählt keine grossgeschriebenen Wörter (im Deutschen sind alle
    Nomen gross), sondern Zahlen, Beträge, Akronyme, Markennamen in
    Binnenmajuskel (digitalONLY, ChatGPT), Schweizer Orte und Marken aus
    slop_de.json, Wochentage, Monate.
  - STIMME misst statt englischer Kurzformen die gesprochene Sprache:
    Modalpartikeln (mal, halt, eben, doch, ja, eigentlich ...) und
    Verschmelzungen (gibt's, geht's, fürs, aufs ...), dazu ich/wir/Sie/du.
  - FINGERABDRUCK zählt zusätzlich „deutsche“ Anführungszeichen,
    Gedankenstriche und das ß (in der Schweiz ungebräuchlich).

Jede Prüfung liefert einen MENSCH-Wert von 0 bis 100. Höher ist besser.

Aufruf
  python3 detect.py entwurf.txt
  python3 detect.py entwurf.txt --json
  python3 detect.py vorher.txt nachher.txt      # zwei Entwürfe vergleichen
"""

import argparse
import json
import os
import re
import statistics
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
LEX = os.path.join(HERE, "slop_de.json")

SENT_RE = re.compile(r"[^.!?\n]+[.!?]*")
WORD_RE = re.compile(r"[A-Za-zÄÖÜäöüßéèàçâêô'’]+")

PARTICLES = re.compile(
    r"\b(?:mal|halt|eben|doch|ja|eigentlich|eh|ziemlich|echt|einfach|schon|wohl|"
    r"übrigens|ehrlich gesagt|sowieso|bisschen|gell)\b|\boder\?", re.IGNORECASE)
VERSCHMELZUNG = re.compile(
    r"\b(?:\w+['’]s|fürs|aufs|ums|durchs|übers|vors|hinters|unters|nen|'nen|hab|"
    r"geht's|gibt's|wie's|hat's|war's|ist's)\b", re.IGNORECASE)
PRON_ANY = re.compile(
    r"\b(?:ich|mich|mir|mein\w*|wir|uns|unser\w*|du|dich|dir|dein\w*|euch|euer\w*)\b",
    re.IGNORECASE)
PRON_SIE = re.compile(r"\b(?:Sie|Ihnen|Ihr|Ihre|Ihrem|Ihren|Ihrer|Ihres)\b")

NUMBERS = re.compile(r"\b\d[\d'’.,]*%?|\bCHF\b|\bFr\.\s?\d|€|\$")
ACRONYM = re.compile(r"\b[A-ZÄÖÜ]{2,6}\b")
CAMEL = re.compile(r"\b[a-z]+[A-Z][A-Za-z]*\b|\b[A-Z][a-z]+[A-Z][A-Za-z]*\b")
MENTION = re.compile(r"@\w+")
TIME_WORDS = re.compile(
    r"\b(?:Montag|Dienstag|Mittwoch|Donnerstag|Freitag|Samstag|Sonntag|Januar|Februar|"
    r"März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|Uhr|"
    r"Minuten|Stunden|Tage|Wochen|Monate|Jahre)\b")

ABBR = ["z.B.", "z. B.", "u.a.", "u. a.", "d.h.", "d. h.", "bzw.", "ca.", "Dr.", "Nr.",
        "inkl.", "exkl.", "evtl.", "ggf.", "usw.", "etc.", "Fr.", "Mio.", "Mrd.", "Std.",
        "Min.", "Tel.", "vgl.", "bspw.", "zzgl.", "St.", "Prof.", "Hr.", "Fa."]


def clamp(n):
    return max(0.0, min(100.0, n))


def scale(value, human, machine):
    """value auf 0-100 abbilden: `human` -> 100, `machine` -> 0."""
    if human == machine:
        return 50.0
    return clamp((value - machine) / (human - machine) * 100)


def _mask_abbr(text):
    for a in ABBR:
        text = text.replace(a, a.replace(".", ""))
    return re.sub(r"(?<=\d)\.(?=\d|[-–])", "", text)


def sentences(text):
    return [s.strip() for s in SENT_RE.findall(_mask_abbr(text)) if len(s.split()) >= 2]


def words(text):
    return WORD_RE.findall(text)


def check_burstiness(text):
    """Menschen variieren die Satzlänge stark. Modelle schreiben gleichmässig."""
    lens = [len(s.split()) for s in sentences(text)]
    if len(lens) < 4:
        return 50.0, "zu kurz zum Beurteilen"
    mean = statistics.mean(lens)
    cv = statistics.pstdev(lens) / mean if mean else 0
    score = scale(cv, human=0.70, machine=0.22)
    return score, f"Variation {cv:.2f} über {len(lens)} Sätze (Ziel 0.55+)"


def check_specificity(text, lex):
    """Zahlen, Namen, Orte, Daten. Floskeln sind abstrakt."""
    w = words(text)
    if len(w) < 25:
        return 50.0, "zu kurz zum Beurteilen"
    orte = [o for o in lex.get("orte", []) + lex.get("marken", [])
            if re.search(r"(?<!\w)" + re.escape(o) + r"(?!\w)", text)]
    named = set(ACRONYM.findall(text)) | set(CAMEL.findall(text)) | set(MENTION.findall(text)) \
        | set(TIME_WORDS.findall(text)) | set(orte)
    hits = len(NUMBERS.findall(text)) + len(named)
    density = hits * 100 / len(w)
    score = scale(density, human=5.0, machine=0.5)
    return score, f"{hits} konkrete Marker, {density:.1f} pro 100 Wörter (Ziel 4+)"


def _lex_pattern(entry):
    core = re.escape(entry["find"]).replace(r"\ ", r"\s+")
    tail = r"(?:e|en|er|es|em)?" if entry.get("flex") else ""
    return re.compile(r"(?<![\w-])" + core + tail + r"(?![\w-])", re.IGNORECASE)


def check_slop(text, lex):
    """Dichte der Floskeln aus dem Lexikon."""
    w = words(text)
    if not w:
        return 50.0, "leer"
    hits, found = 0, []
    for entry in lex["words"] + lex["phrases"]:
        n = len(_lex_pattern(entry).findall(text))
        if n:
            hits += n
            found.append(entry["find"])
    density = hits * 100 / len(w)
    score = scale(density, human=0.0, machine=4.0)
    detail = f"{hits} Floskeln, {density:.1f} pro 100 Wörter"
    if found:
        detail += " (" + ", ".join(sorted(found)[:4]) + (", ..." if len(found) > 4 else "") + ")"
    return score, detail


def check_fingerprint(text):
    """Zeichen, die eine Handy-Tastatur in der Schweiz nicht erzeugt."""
    invisible = sum(1 for c in text if unicodedata.category(c) == "Cf")
    em = text.count("—")
    gedanken = len(re.findall(r"[ \t]–[ \t]", text))
    curly = sum(text.count(c) for c in "‘’“”„‚")
    ellip = text.count("…")
    nbsp = sum(text.count(c) for c in "    ")
    eszett = text.count("ß") + text.count("ẞ")
    total = invisible * 4 + em * 2 + gedanken * 2 + curly + ellip + nbsp + eszett
    per1k = total * 1000 / max(len(text), 1)
    score = scale(per1k, human=0.0, machine=12.0)
    detail = (f"{invisible} unsichtbar, {em} Geviertstrich, {gedanken} Gedankenstrich, "
              f"{curly} typogr. Anführungszeichen, {ellip} …, {nbsp} gesch. Leerzeichen, {eszett} ß")
    return score, detail


def check_voice(text, lex):
    """Gesprochene Sprache, Person, und die Formen, auf die Modelle zurückfallen."""
    w = words(text)
    if len(w) < 25:
        return 50.0, "zu kurz zum Beurteilen"
    per100 = 100 / len(w)
    spoken = (len(PARTICLES.findall(text)) + len(VERSCHMELZUNG.findall(text))) * per100
    person = (len(PRON_ANY.findall(text)) + len(PRON_SIE.findall(text))) * per100
    tells, names = 0, []
    for s in lex["structures"]:
        try:
            n = len(re.compile(s["regex"]).findall(text))
        except re.error:
            continue
        if n:
            tells += n
            names.append(s["id"])
    bullets = [len(b.split()) for b in re.findall(r"(?m)^\s*[-*•]\s+(.+)$", text)]
    uniform = (len(bullets) >= 3 and statistics.pstdev(bullets) < 1.6)
    score = (scale(spoken, human=2.5, machine=0.0) * 0.35
             + scale(person, human=7.0, machine=1.0) * 0.35
             + clamp(100 - tells * 22) * 0.30)
    if uniform:
        score -= 12
        names.append("gleichlange-aufzaehlung")
    detail = (f"{spoken:.1f} Umgangssprache-Marker, {person:.1f} Personalpronomen "
              f"pro 100 Wörter, {tells} Strukturmuster")
    if names:
        detail += " [" + ", ".join(names[:4]) + "]"
    return clamp(score), detail


CHECKS = ["SATZRHYTHMUS", "KONKRETHEIT", "FLOSKELN", "FINGERABDRUCK", "STIMME"]


def run(text, lex):
    results = {
        "SATZRHYTHMUS": check_burstiness(text),
        "KONKRETHEIT": check_specificity(text, lex),
        "FLOSKELN": check_slop(text, lex),
        "FINGERABDRUCK": check_fingerprint(text),
        "STIMME": check_voice(text, lex),
    }
    scores = [results[c][0] for c in CHECKS]
    # Die schwächste Prüfung zieht das Urteil: ein Detektor braucht nur ein Signal.
    overall = statistics.mean(scores) * 0.6 + min(scores) * 0.4
    verdict = "PASS" if overall >= 70 and min(scores) >= 55 else (
        "REVIEW" if overall >= 50 else "FLAGGED")
    return results, overall, verdict


def bar(score, width=24):
    filled = round(score / 100 * width)
    return "#" * filled + "." * (width - filled)


def render(results, overall, verdict, label=None, out=sys.stdout):
    title = "KI-ERKENNUNGS-PANEL" + (f"  -  {label}" if label else "")
    print("\n" + title, file=out)
    print("=" * max(len(title), 62), file=out)
    for name in CHECKS:
        score, detail = results[name]
        print(f"  {name:<14} {bar(score)} {score:5.1f}", file=out)
        print(f"  {'':<14} {detail}", file=out)
    print("-" * 62, file=out)
    print(f"  {'MENSCH-SCORE':<14} {bar(overall)} {overall:5.1f}   {verdict}", file=out)
    if verdict != "PASS":
        weakest = min(CHECKS, key=lambda c: results[c][0])
        print(f"\n  Schwächstes Signal: {weakest}. Das zuerst beheben.", file=out)
    print("", file=out)


def main():
    ap = argparse.ArgumentParser(description="Bewertet, wie maschinell ein Entwurf wirkt.")
    ap.add_argument("input", nargs="?", default="-", help="Datei, oder - für stdin")
    ap.add_argument("compare", nargs="?", help="zweite Datei für vorher/nachher")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--lexicon", default=LEX)
    args = ap.parse_args()

    lex = json.load(open(args.lexicon, encoding="utf-8"))
    read = lambda p: sys.stdin.read() if p == "-" else open(p, encoding="utf-8").read()

    targets = [(args.input, read(args.input))]
    if args.compare:
        targets.append((args.compare, read(args.compare)))

    payload = []
    for name, text in targets:
        results, overall, verdict = run(text, lex)
        payload.append({
            "source": name,
            "checks": {k: {"score": round(v[0], 1), "detail": v[1]} for k, v in results.items()},
            "human_score": round(overall, 1),
            "verdict": verdict,
        })

    if args.json:
        print(json.dumps(payload if args.compare else payload[0], indent=2, ensure_ascii=False))
        return

    for (name, text), p in zip(targets, payload):
        results, overall, verdict = run(text, lex)
        render(results, overall, verdict, label=os.path.basename(name) if args.compare else None)
    if args.compare:
        a, b = payload
        delta = b["human_score"] - a["human_score"]
        print(f"  {a['human_score']:.1f} {a['verdict']}  ->  "
              f"{b['human_score']:.1f} {b['verdict']}   ({delta:+.1f})\n")

    sys.exit(0 if payload[-1]["verdict"] == "PASS" else 1)


if __name__ == "__main__":
    main()
