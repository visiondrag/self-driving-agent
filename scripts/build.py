#!/usr/bin/env python3
"""Generate docs/*.md and the README topic index from data/*.yaml.

Usage: python scripts/build.py [--check]
  --check  exit non-zero if generated files are out of date (for CI)
"""
from __future__ import annotations

import sys

from common import DOCS, ROOT, iter_papers, load_topics, paper_link, paper_year

START, END = "<!-- TOPICS:START -->", "<!-- TOPICS:END -->"


def esc(text: str) -> str:
    return str(text).replace("|", "\\|")


def render_topic(topic) -> str:
    out = [f"# {topic['title']}", "", "<!-- generated from data/%s.yaml; do not edit by hand -->" % topic["slug"], ""]
    if topic.get("intro"):
        out += [topic["intro"].strip(), ""]
    n = sum(1 for _ in iter_papers(topic))
    out += [f"**{n} entries.** Add papers by editing `data/{topic['slug']}.yaml` (see [CONTRIBUTING](../CONTRIBUTING.md)).", ""]
    for section in topic.get("sections", []):
        out += [f"## {section['name']}", ""]
        if section.get("desc"):
            out += [section["desc"].strip(), ""]
        out += ["| Paper | Year | Venue | Code | Note |", "|---|---|---|---|---|"]
        papers = sorted(section["papers"], key=lambda p: (-(paper_year(p) or 0), p["title"].lower()))
        for p in papers:
            link = paper_link(p)
            title = f"[{esc(p['title'])}]({link})" if link else esc(p["title"])
            code = f"[code]({p['code']})" if p.get("code") else ""
            note = " - ".join(x for x in (p.get("org"), p.get("note")) if x)
            out.append(
                f"| {title} | {paper_year(p) or ''} | {esc(p.get('venue', ''))} | {code} | {esc(note)} |"
            )
        out.append("")
    return "\n".join(out)


def render_index(topics) -> str:
    lines = ["| Topic | Entries | What is inside |", "|---|---|---|"]
    for t in topics:
        n = sum(1 for _ in iter_papers(t))
        lines.append(f"| [{t['title']}](docs/{t['slug']}.md) | {n} | {esc(t.get('summary', ''))} |")
    total = sum(sum(1 for _ in iter_papers(t)) for t in topics)
    lines += ["", f"**Total: {total} entries across {len(topics)} topics.**"]
    return "\n".join(lines)


def main() -> int:
    check = "--check" in sys.argv
    topics = load_topics()
    stale = []
    DOCS.mkdir(exist_ok=True)
    for t in topics:
        path = DOCS / f"{t['slug']}.md"
        text = render_topic(t) + "\n"
        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                stale.append(str(path))
        else:
            path.write_text(text, encoding="utf-8")
    readme = ROOT / "README.md"
    body = readme.read_text(encoding="utf-8")
    if START in body and END in body:
        head, rest = body.split(START, 1)
        _, tail = rest.split(END, 1)
        new = f"{head}{START}\n{render_index(topics)}\n{END}{tail}"
        if check:
            if new != body:
                stale.append("README.md")
        else:
            readme.write_text(new, encoding="utf-8")
    if check and stale:
        print("Out of date (run `python scripts/build.py`):", *stale, sep="\n  ")
        return 1
    print("ok" if check else f"built {len(topics)} topics")
    return 0


if __name__ == "__main__":
    sys.exit(main())
