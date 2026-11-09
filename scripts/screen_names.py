#!/usr/bin/env python3
"""Quick knockout signals for candidate names (stdlib only). NOT trademark clearance.

Usage:
  screen_names.py Name1 Name2 ... [--descriptor "Find Local Work"] [--no-dns]
  screen_names.py --file names.txt --descriptor "Save With Time Locks"

Per name it reports:
  len        letters in the brand (aim <= ~12)
  title      length of "Name: descriptor" vs the 30-char App Store / Play cap
  syll       rough syllable estimate (2-3 is the sweet spot)
  flags      spelling/pronunciation risks (double letters, consonant clusters,
             ambiguous letters, digits/hyphens, hard-to-hear spellings)
  .com       DNS: 'taken?' if <name>.com resolves (likely registered/in use),
             'maybe free' if it doesn't (confirm with a registrar)
"""
import argparse
import re
import socket
import sys

STORE_CAP = 30
VOWELS = "aeiouy"


def syllables(word: str) -> int:
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups)
    if w.endswith("e") and not w.endswith(("le", "ee")) and n > 1:
        n -= 1
    return max(n, 1)


def flags(name: str) -> list[str]:
    f = []
    low = name.lower()
    if re.search(r"[0-9\-_]", name):
        f.append("digit/hyphen (hard to say/type)")
    if re.search(r"[^aeiouy\s]{4,}", low):
        f.append("consonant cluster")
    if re.search(r"(.)\1", low):
        f.append("double letter (spelling ambiguity)")
    if re.search(r"(ph|ck|gh|qu|x|c[eiy])", low):
        f.append("sound has multiple spellings")
    if re.search(r"[^aeiou](r|l|n|m)$", low) and not re.search(r"[aeiouy]", low[-3:-1]):
        f.append("dropped-vowel ending (Flickr-style, spellability)")
    if len(re.sub(r"[^a-z]", "", low)) > 12:
        f.append("long (>12)")
    return f


def dot_com(name: str) -> str:
    host = re.sub(r"[^a-z0-9-]", "", name.lower()) + ".com"
    try:
        socket.setdefaulttimeout(3)
        socket.getaddrinfo(host, 80)
        return "taken?"
    except socket.gaierror:
        return "maybe free"
    except OSError:
        return "unknown"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("names", nargs="*")
    ap.add_argument("--file")
    ap.add_argument("--descriptor", default="", help="store-title descriptor after 'Name: '")
    ap.add_argument("--no-dns", action="store_true")
    a = ap.parse_args()

    names = list(a.names)
    if a.file:
        with open(a.file) as fh:
            names += [l.strip() for l in fh if l.strip() and not l.startswith("#")]
    if not names:
        ap.error("no names")

    print(f"{'name':<16} {'len':>3} {'title':>7} {'syll':>4}  {'.com':<10} flags")
    for n in names:
        letters = len(re.sub(r"[^A-Za-z]", "", n))
        title = f"{n}: {a.descriptor}" if a.descriptor else n
        tl = f"{len(title)}{'!' if len(title) > STORE_CAP else ''}"
        dns = "-" if a.no_dns else dot_com(n)
        print(f"{n:<16} {letters:>3} {tl:>7} {syllables(n):>4}  {dns:<10} {'; '.join(flags(n))}")
    print(f"\n'!' = store title over {STORE_CAP} chars. Knockout signals only — not clearance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
