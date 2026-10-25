#!/usr/bin/env python3
"""Look up English terms in a TBX term base (for example the Microsoft Terminology
Collection, VIETNAMESE.tbx) and print the Vietnamese forms.

Usage: python3 -I tbx_lookup.py <file.tbx> <term> [<term> ...]
       python3 -I tbx_lookup.py <file.tbx> --file terms.txt      (one English term per line)

Output, one block per term: each Vietnamese form, how many entries use it, and the
first English definition. Exact match, case ignored. Pick one form per term and write
it to a term pack (terms/*.md) with source mark M (Microsoft) or your own mark.
The term base is not part of this skill: download it from its owner.
"""
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict

XML_LANG = "{http://www.w3.org/XML/1998/namespace}lang"


def load(path, wanted):
    forms = defaultdict(Counter)
    defs = {}
    for _, el in ET.iterparse(path, events=("end",)):
        if el.tag != "termEntry":
            continue
        en, vi, d = [], [], None
        for ls in el.iter("langSet"):
            lang = ls.get(XML_LANG, "")
            terms = [t.text or "" for t in ls.iter("term")]
            if lang.startswith("en"):
                en += terms
                de = ls.find(".//descrip[@type='definition']")
                if de is not None and de.text:
                    d = de.text
            elif lang.startswith("vi"):
                vi += terms
        for e in en:
            k = e.strip().lower()
            if k in wanted:
                for v in vi:
                    forms[k][v.strip()] += 1
                if d and k not in defs:
                    defs[k] = d
        el.clear()
    return forms, defs


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    path, rest = sys.argv[1], sys.argv[2:]
    if rest[0] == "--file":
        rest = [l.strip() for l in open(rest[1], encoding="utf-8") if l.strip()]
    wanted = {t.lower(): t for t in rest}
    forms, defs = load(path, set(wanted))
    for k, t in wanted.items():
        print(f"## {t}")
        if not forms[k]:
            print("  (not found)")
        for v, n in forms[k].most_common(6):
            print(f"  {v}  [{n}]")
        if k in defs:
            print(f"  def: {defs[k][:140]}")


if __name__ == "__main__":
    main()
