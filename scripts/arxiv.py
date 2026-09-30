"""Minimal arXiv API client (stdlib only)."""
from __future__ import annotations

import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

API = "https://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom"}


def _get(params: dict) -> str:
    url = f"{API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "self-driving-agent-bot"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")


def parse(xml_text: str) -> list[dict]:
    root = ET.fromstring(xml_text)
    entries = []
    for e in root.findall("a:entry", NS):
        raw_id = e.findtext("a:id", "", NS).rsplit("/abs/", 1)[-1]
        title = " ".join(e.findtext("a:title", "", NS).split())
        entries.append(
            {
                "id": raw_id.split("v")[0] if "v" in raw_id else raw_id,
                "title": title,
                "published": e.findtext("a:published", "", NS)[:10],
                "summary": " ".join(e.findtext("a:summary", "", NS).split()),
            }
        )
    return entries


def lookup(ids: list[str]) -> dict[str, dict]:
    """Fetch metadata for arXiv ids in batches; returns {id: entry}."""
    found = {}
    for i in range(0, len(ids), 50):
        batch = ids[i : i + 50]
        xml_text = _get({"id_list": ",".join(batch), "max_results": len(batch)})
        for entry in parse(xml_text):
            found[entry["id"]] = entry
        time.sleep(3)  # be polite to the API
    return found


def search(query: str, max_results: int = 50) -> list[dict]:
    xml_text = _get(
        {
            "search_query": query,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "max_results": max_results,
        }
    )
    return parse(xml_text)
