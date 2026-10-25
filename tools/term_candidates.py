#!/usr/bin/env python3
"""List English term candidates in a source text that no term pack covers.

Usage: python3 -I term_candidates.py <source.md|.txt|.html> [--min 2]

Candidates (a simple, known extraction method: patterns plus frequency):
- abbreviations (API, SSO, CI/CD) and CamelCase or dotted names;
- hyphenated words (sign-in, opt-out);
- two- and three-word phrases without stop words that occur at least --min times.
Words that a pack (../terms/*.md) already has are left out. Review the list,
then look each term up (tools/tbx_lookup.py, the vendor's Vietnamese interface)
and add a row to a pack. Names of products and companies go to the org pack.
"""
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
TERMS_DIR = os.path.join(HERE, "..", "terms")
STOP = set("""a an the and or but if then else of to in on at by for with from as is are was were be been being
this that these those it its into over under than so such not no can may must should will would could
you your we our they their he she his her them us i me my do does did done has have had any all each
every more most other some only also very just about after before when where which who what how why
up out off new use used using get set run per via until now first last longer need needs make sure
add adds above below old create creates there here own same both while during""".split())


def load_known():
    known = set()
    try:
        files = [f for f in os.listdir(TERMS_DIR) if f.endswith(".md")]
    except OSError:
        files = []
    for f in files:
        for line in open(os.path.join(TERMS_DIR, f), encoding="utf-8"):
            if line.startswith("|"):
                cell = line.split("|")[1]
                for part in re.split(r"[,/;]| and ", cell):
                    p = part.strip().lower()
                    if p:
                        known.add(p)
    return known


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    mn = int(sys.argv[sys.argv.index("--min") + 1]) if "--min" in sys.argv else 2
    text = open(sys.argv[1], encoding="utf-8").read()
    text = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>|<[^>]+>|`[^`]*`", " ", text)
    known = load_known()
    found = Counter()
    for m in re.finditer(r"\b[A-Z][A-Z0-9]{1,}(?:/[A-Z0-9]+)?s?\b|\b[a-z]+[A-Z]\w+\b|\b[A-Z][a-z]+[A-Z]\w+\b|\b\w+(?:-\w+)+\b", text):
        found[m.group(0)] += mn
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", text)
    for n in (2, 3):
        for i in range(len(words) - n + 1):
            gram = words[i:i + n]
            if any(w.lower() in STOP for w in gram):
                continue
            found[" ".join(w.lower() for w in gram)] += 1
    def is_known(t):
        t = t.lower()
        return t in known or t.rstrip("s") in known or all(w in known or w.rstrip("s") in known for w in t.split())
    rows = [(t, c) for t, c in found.items() if c >= mn and not is_known(t)]
    for t, c in sorted(rows, key=lambda x: (-x[1], x[0].lower())):
        print(f"{c:3d}  {t}")


if __name__ == "__main__":
    main()
