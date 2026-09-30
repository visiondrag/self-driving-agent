#!/usr/bin/env python3
"""Find new arXiv papers on self-driving that are not yet in data/*.yaml.

Prints a markdown checklist of candidates for triage (never edits data).
Usage: python scripts/discover.py [--max 100] > candidates.md
"""
from __future__ import annotations

import sys

import arxiv
from common import iter_papers, load_topics

QUERIES = [
    'abs:"autonomous driving" AND (abs:"vision-language-action" OR abs:VLA)',
    'abs:"autonomous driving" AND (abs:"vision-language model" OR abs:"large language model")',
    'abs:"end-to-end" AND abs:"autonomous driving"',
    'abs:"driving" AND abs:"world model"',
    'abs:"autonomous driving" AND abs:"reinforcement learning" AND abs:planning',
    'abs:"autonomous driving" AND (abs:benchmark OR abs:dataset)',
    'abs:"autonomous driving" AND (abs:simulation OR abs:"scenario generation")',
    'abs:"autonomous driving" AND abs:"Gaussian splatting"',
]


def main() -> int:
    limit = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 100
    known = {str(p["id"]) for t in load_topics() for _, p in iter_papers(t) if p.get("id")}
    seen = set()
    print("# Candidate papers\n")
    for q in QUERIES:
        print(f"## `{q}`\n")
        for e in arxiv.search(q, limit):
            if e["id"] in known or e["id"] in seen:
                continue
            seen.add(e["id"])
            print(f"- [ ] {e['published']} [{e['title']}](https://arxiv.org/abs/{e['id']}) `{e['id']}`")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
