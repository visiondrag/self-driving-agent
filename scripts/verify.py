#!/usr/bin/env python3
"""Check every arXiv id in data/*.yaml resolves and its title matches.

Needs network access to export.arxiv.org. Exit code 1 on any mismatch/missing id.
Usage: python scripts/verify.py [--threshold 0.6]
"""
from __future__ import annotations

import difflib
import re
import sys
from collections import Counter

import arxiv
from common import NEW_ID, iter_papers, load_topics


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9 ]", "", s.lower().replace("-", " "))


def similar(a: str, b: str) -> float:
    a, b = norm(a), norm(b)
    if a in b or b in a:  # allow short-name titles like "UniAD" vs full title
        return 1.0
    return difflib.SequenceMatcher(None, a, b).ratio()


def main() -> int:
    threshold = 0.6
    if "--threshold" in sys.argv:
        threshold = float(sys.argv[sys.argv.index("--threshold") + 1])
    entries = [(t["slug"], p) for t in load_topics() for _, p in iter_papers(t) if p.get("id")]
    problems = []
    for slug, p in entries:
        if not NEW_ID.match(str(p["id"])):
            problems.append(f"{slug}: bad id format {p['id']!r} ({p['title']})")
    dupes = [k for k, v in Counter(str(p["id"]) for _, p in entries).items() if v > 1]
    ids = sorted({str(p["id"]) for _, p in entries if NEW_ID.match(str(p["id"]))})
    meta = arxiv.lookup(ids)
    for slug, p in entries:
        m = meta.get(str(p["id"]))
        if not m:
            problems.append(f"{slug}: {p['id']} not found on arXiv ({p['title']})")
            continue
        score = similar(p["title"], m["title"])
        if score < threshold:
            problems.append(f"{slug}: {p['id']} title mismatch ({score:.2f})\n    ours:  {p['title']}\n    arxiv: {m['title']}")
    if dupes:
        print("Note: ids listed in several topics (fine if intentional):", ", ".join(dupes))
    print(f"checked {len(ids)} ids")
    for line in problems:
        print("PROBLEM", line)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
