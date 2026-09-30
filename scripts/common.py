"""Shared helpers: load the YAML paper database."""
from __future__ import annotations

import pathlib
import re

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"

NEW_ID = re.compile(r"^\d{4}\.\d{4,5}$")


def load_topics():
    """Return topic dicts sorted by their `order` field."""
    topics = []
    for path in sorted(DATA.glob("*.yaml")):
        topic = yaml.safe_load(path.read_text(encoding="utf-8"))
        topic["slug"] = path.stem
        topics.append(topic)
    topics.sort(key=lambda t: t.get("order", 99))
    return topics


def iter_papers(topic):
    for section in topic.get("sections", []):
        for paper in section.get("papers", []):
            yield section, paper


def paper_year(paper):
    if paper.get("year"):
        return int(paper["year"])
    pid = str(paper.get("id", ""))
    if NEW_ID.match(pid):
        yy = int(pid[:2])
        return 2000 + yy
    return None


def paper_link(paper):
    if paper.get("id"):
        return f"https://arxiv.org/abs/{paper['id']}"
    return paper.get("url")
