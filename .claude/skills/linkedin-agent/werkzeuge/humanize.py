#!/usr/bin/env python3
"""
humanize.py - entfernt den Maschinen-Fingerabdruck aus einem Entwurf.
Deutsche Fassung (Schweiz) von humanize.py aus linkedin-agent-skill
(Jake Schincariol, MIT).

Drei Durchgänge, in dieser Reihenfolge:

  1. UNSICHTBAR    löscht oder normalisiert Zeichen, die keine Tastatur
                   erzeugt: Zero-Width-Joiner, Word-Joiner, bedingte
                   Trennstriche, BOMs, Unicode-Tag-Zeichen, geschützte und
                   schmale Leerzeichen.
  2. TYPOGRAFIE    Geviertstrich -> Komma, Gedankenstrich -> Bindestrich oder
                   Komma, „deutsche“ und “englische” Anführungszeichen ->
                   gerade, … -> drei Punkte, ß -> ss (Schweizer Schreibweise).
                   «Schweizer Guillemets» bleiben unangetastet.
  3. LEXIKON       ersetzt die Floskeln aus slop_de.json durch einfache Wörter,
                   erhält Gross-/Kleinschreibung und Endungen, lässt URLs in
                   Ruhe.

Strukturelle Muster («Es geht nicht um X, sondern um Y», Dreierreihen,
Hashtag-Wände) werden GEMELDET, nie automatisch umgeschrieben. Die Satzform
zu ändern braucht Urteilsvermögen, das ist die Arbeit des Modells oder des
Menschen, nicht die einer Regex.

Aufruf
  python3 humanize.py entwurf.txt
  python3 humanize.py entwurf.txt --report
  python3 humanize.py entwurf.txt -o sauber.txt --report
  python3 humanize.py entwurf.txt --json
  cat entwurf.txt | python3 humanize.py - --report
"""

import argparse
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
LEX = os.path.join(HERE, "slop_de.json")

URL_RE = re.compile(r"https?://\S+|www\.\S+|\S+@\S+\.\S+"
                    r"|\b[\w-]+\.(?:ch|li|com|de|at|net|org|io|ai)\b(?:/\S*)?")
SENT_RE = re.compile(r"[^.!?\n]+[.!?]*")
FLEX_ENDINGS = r"(?P<end>e|en|er|es|em)?"


def load_lexicon(path=LEX):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _cp(spec):
    """'U+200B' -> 0x200B;  'U+E0000-U+E007F' -> (start, end)."""
    if "-" in spec:
        a, b = spec.split("-")
        return (int(a[2:], 16), int(b[2:], 16))
    return int(spec[2:], 16)


def protect_urls(text):
    """URLs durch Platzhalter ersetzen, damit kein Durchgang in Links schreibt."""
    found = []

    def stash(m):
        found.append(m.group(0))
        return f"\x00URL{len(found) - 1}\x00"

    return URL_RE.sub(stash, text), found


def restore_urls(text, found):
    for i, url in enumerate(found):
        text = text.replace(f"\x00URL{i}\x00", url)
    return text


def pass_invisible(text, lex):
    hits = []
    for entry in lex["invisible"]:
        cp = _cp(entry["cp"])
        if isinstance(cp, tuple):
            pattern = "[" + re.escape(chr(cp[0])) + "-" + re.escape(chr(cp[1])) + "]"
        else:
            pattern = re.escape(chr(cp))
        n = len(re.findall(pattern, text))
        if n:
            hits.append({"name": entry["cp"] + " " + entry["name"], "count": n,
                         "action": "gelöscht" if entry["action"] == "delete" else "-> Leerzeichen"})
            text = re.sub(pattern, "" if entry["action"] == "delete" else " ", text)
    # Jedes verbleibende Cf-Zeichen (Format) ist per Definition unsichtbar.
    stray = [c for c in text if unicodedata.category(c) == "Cf" and c != "\x00"]
    if stray:
        hits.append({"name": "weitere unsichtbare Formatzeichen", "count": len(stray),
                     "action": "gelöscht"})
        text = "".join(c for c in text if unicodedata.category(c) != "Cf" or c == "\x00")
    return text, hits


def pass_typographic(text, lex):
    hits = []
    # Striche am Zeilenanfang sind Aufzählungen, keine Gedankenstriche.
    text, n_bullets = re.subn(r"(?m)^([ \t]*)[–—][ \t]+", r"\1- ", text)
    if n_bullets:
        hits.append({"name": "– / — als Aufzählungszeichen", "count": n_bullets, "to": "-"})
    for entry in lex["typographic"]:
        ch = entry["from"]
        n = text.count(ch)
        if not n:
            continue
        hits.append({"name": f"{ch}  {entry['name']}", "count": n,
                     "to": entry["to"].strip() or "(Leerzeichen)"})
        if ch == "—":
            text = re.sub(r"[ \t]*—[ \t]*", ", ", text)
        elif ch == "–":
            text = re.sub(r"(?<=\d)[ \t]*–[ \t]*(?=\d)", "-", text)   # 8–10 -> 8-10
            text = re.sub(r"[ \t]+–[ \t]+", ", ", text)               # als Gedankenstrich
            text = text.replace("–", "-")                               # 50.– -> 50.-
        else:
            text = text.replace(ch, entry["to"])
    # Ein eingefügtes Komma vor bestehender Satzzeichen liest sich falsch.
    text = re.sub(r",[ \t]*([,.;:!?])", r"\1", text)
    text = re.sub(r",[ \t]*\n", "\n", text)
    return text, hits


def _match_case(src, repl):
    if not repl:
        return repl
    if src.isupper() and len(src) > 1:
        return repl.upper()
    if src[0].isupper():
        return repl[0].upper() + repl[1:]
    if src[0].islower() and repl[0].isupper() and " " not in repl:
        # Nomen bleiben gross, auch wenn die Fundstelle klein war.
        return repl
    return repl


def _pattern(entry):
    core = re.escape(entry["find"]).replace(r"\ ", r"\s+")
    tail = FLEX_ENDINGS if entry.get("flex") else ""
    return re.compile(r"(?<![\w-])" + core + tail + r"(?![\w-])", re.IGNORECASE)


def pass_lexical(text, lex):
    """Floskeln ersetzen. Längste zuerst, damit Wendungen vor Einzelwörtern greifen."""
    hits = []
    entries = sorted(lex["phrases"] + lex["words"],
                     key=lambda e: len(e["find"]), reverse=True)
    for entry in entries:
        pattern = _pattern(entry)
        found = pattern.findall(text)
        if not found:
            continue
        hits.append({"find": entry["find"], "replace": entry["replace"] or "(gelöscht)",
                     "count": len(found), "family": entry["family"]})

        def sub(m, entry=entry):
            whole = m.group(0)
            end = m.groupdict().get("end") or ""
            core = whole[: len(whole) - len(end)] if end else whole
            repl = _match_case(core, entry["replace"])
            return repl + (end if repl else "")

        text = pattern.sub(sub, text)
    # Aufräumen nach Löschungen.
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r"(?m)^[ \t]*([,.;:])[ \t]*", "", text)
    text = re.sub(r"[ \t]+([,.;:!?])", r"\1", text)
    text = re.sub(r"(?<!\.)\.\.(?!\.)", ".", text)
    text = re.sub(r"(?m)^[ \t]+", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Satzanfang nach Löschung wieder gross schreiben (nicht nach z.B., ca., ...).
    text = _recapitalize(text)
    # Aus Gedankenstrich gewordenes Komma vor Konnektor -> neuer Satz.
    text = re.sub(r",\s*(also|deshalb|trotzdem|darum)\s*,\s*",
                  lambda m: ". " + m.group(1)[0].upper() + m.group(1)[1:] + ", ", text)
    return text, hits


def scan_structures(text, lex):
    flags = []
    for s in lex["structures"]:
        try:
            pattern = re.compile(s["regex"])
        except re.error:
            continue
        found = pattern.findall(text)
        if found:
            flags.append({"name": s["name"], "count": len(found), "fix": s["fix"]})
    lens = [len(s.split()) for s in SENT_RE.findall(_mask_abbr(text)) if len(s.split()) >= 2]
    if len(lens) >= 4:
        mean = sum(lens) / len(lens)
        var = sum((n - mean) ** 2 for n in lens) / len(lens)
        cv = (var ** 0.5) / mean if mean else 0
        if cv < 0.35:
            flags.append({
                "name": f"Gleichförmige Satzlänge (Variation {cv:.2f})",
                "count": len(lens),
                "fix": "Einen Satz halbieren. Einen anderen lang laufen lassen. Maschinen schreiben gleichmässig.",
            })
    return flags


ABBR = ["z.B.", "z. B.", "u.a.", "u. a.", "d.h.", "d. h.", "bzw.", "ca.", "Dr.", "Nr.",
        "inkl.", "exkl.", "evtl.", "ggf.", "usw.", "etc.", "Fr.", "Mio.", "Mrd.", "Std.",
        "Min.", "Tel.", "vgl.", "bspw.", "zzgl.", "St.", "Prof.", "Hr.", "Fa."]


_ABBR_KEYS = {a.replace(" ", "").lower() for a in ABBR}


def _recapitalize(text):
    def fix(m):
        before = text[: m.start()]
        if m.group(1) == "." and before.endswith(".."):
            return m.group(0)                      # ... bewusste Fortsetzung
        token = re.search(r"(\S+)$", before + m.group(1))
        word = token.group(1).lower() if token else ""
        if word in _ABBR_KEYS or any(word.endswith(k) for k in _ABBR_KEYS if "." in k[:-1]):
            return m.group(0)
        if re.fullmatch(r"[\d'.,]+\.", word):
            return m.group(0)                      # 1. Januar, 3. Punkt
        return m.group(1) + m.group(2) + m.group(3).upper()

    # Nur rein klein geschriebene Wörter anfassen: digitalONLY, iPhone, eBay bleiben.
    lower_word = r"(?=[a-zäöüß]*(?![\w.]))"
    text = re.sub(r"([.!?])([ \t]+)([a-zäöü])" + lower_word, fix, text)
    return re.sub(r"(?m)^([ \t]*)([a-zäöü])" + lower_word,
                  lambda m: m.group(1) + m.group(2).upper(), text)


def _mask_abbr(text):
    """Abkürzungen und Dezimalpunkte maskieren, damit sie keine Sätze beenden."""
    for a in ABBR:
        text = text.replace(a, a.replace(".", ""))
    return re.sub(r"(?<=\d)\.(?=\d|[-–])", "", text)


def humanize(text, lex):
    text, urls = protect_urls(text)
    text, inv = pass_invisible(text, lex)
    text, typo = pass_typographic(text, lex)
    text, lexi = pass_lexical(text, lex)
    text = restore_urls(text, urls)
    return text.strip() + "\n", {
        "invisible": inv,
        "typographic": typo,
        "lexical": lexi,
        "structures": scan_structures(text, lex),
    }


def render_report(report, out=sys.stderr):
    def head(title):
        print(f"\n{title}\n" + "-" * len(title), file=out)

    total = sum(h["count"] for h in report["invisible"]) \
        + sum(h["count"] for h in report["typographic"]) \
        + sum(h["count"] for h in report["lexical"])

    head("HUMANIZER-BERICHT")
    print(f"{total} Maschinen-Spuren entfernt, "
          f"{len(report['structures'])} Strukturmuster zum Umschreiben markiert", file=out)

    if report["invisible"]:
        head("1. UNSICHTBARE ZEICHEN")
        for h in report["invisible"]:
            print(f"  {h['count']:>3}x  {h['name']}  {h['action']}", file=out)
    if report["typographic"]:
        head("2. TYPOGRAFIE")
        for h in report["typographic"]:
            print(f"  {h['count']:>3}x  {h['name']}  -> {h['to']}", file=out)
    if report["lexical"]:
        head("3. FLOSKEL-LEXIKON")
        for h in report["lexical"]:
            print(f"  {h['count']:>3}x  {h['find']}  -> {h['replace']}   [{h['family']}]", file=out)
    if report["structures"]:
        head("4. STRUKTURMUSTER  (nicht automatisch behoben - selbst umschreiben)")
        for h in report["structures"]:
            print(f"  {h['count']:>3}x  {h['name']}\n        {h['fix']}", file=out)
    if not any(report.values()):
        head("SAUBER")
        print("  Nichts zu entfernen.", file=out)
    print("", file=out)


def main():
    ap = argparse.ArgumentParser(description="Entfernt den Maschinen-Fingerabdruck aus einem Entwurf.")
    ap.add_argument("input", nargs="?", default="-", help="Datei, oder - für stdin")
    ap.add_argument("-o", "--out", help="bereinigten Text hierhin schreiben statt auf stdout")
    ap.add_argument("--report", action="store_true", help="Änderungen auf stderr ausgeben")
    ap.add_argument("--json", action="store_true", help="{text, report} als JSON ausgeben")
    ap.add_argument("--lexicon", default=LEX, help="Pfad zu slop_de.json")
    args = ap.parse_args()

    raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    lex = load_lexicon(args.lexicon)
    clean, report = humanize(raw, lex)

    if args.json:
        print(json.dumps({"text": clean, "report": report}, indent=2, ensure_ascii=False))
        return
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(clean)
        print(f"geschrieben: {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(clean)
    if args.report:
        render_report(report)


if __name__ == "__main__":
    main()
