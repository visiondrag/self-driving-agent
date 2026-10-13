#!/usr/bin/env python3
"""Build the static site from the repo's Markdown into ./_site.

Usage: python website/build.py [--out _site]
Requires: markdown (pip install markdown). Optional: pillow (resizes the banner).
Fails (exit 1) on any broken internal link or anchor.

Resource lists in the Markdown ("- Title: [Link](url)") are parsed into structured
entries and rendered as cards; the same entries power the home-page topic hub and
the filterable "Explore all" page.
"""
import html, json, re, shutil, sys, posixpath
from pathlib import Path
from urllib.parse import urlparse
import markdown

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / (sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else "_site")
REPO = "https://github.com/visiondrag/self-driving-agent"
SITE_NAME = "Self-Driving Agent"
TAGLINE = "A curated map of autonomous-driving research: end-to-end, VLA, reasoning, world models, simulation, datasets and benchmarks."

# ---------------------------------------------------------------- structure
PAPER_PAGES = [
    "docs/surveys.md", "docs/end-to-end.md", "docs/perception-mapping.md", "docs/prediction-planning.md",
    "docs/llm-vlm.md", "docs/vla.md", "docs/reasoning-rl.md", "docs/world-models.md", "docs/simulation.md",
    "docs/safety-robustness.md", "docs/cooperative-v2x.md", "docs/industry.md"]
NAV = [
    ("Home", "README.md"),
    ("Explore all", "@explore"),
    ("Recent (2025-26)", "docs/recent.md"),
    ("Learning", "docs/learning.md"),
    ("Papers", PAPER_PAGES),
    ("Data & evaluation", ["docs/datasets.md", "docs/benchmarks.md"]),
    ("Tools", "docs/tools.md"),
    ("Competitions", "docs/competitions.md"),
    ("Organizations", "docs/organizations.md"),
    ("Contribute", "CONTRIBUTING.md"),
]
SHORT = {
    "README.md": "Home", "docs/recent.md": "Recent (2025-26)", "docs/surveys.md": "Surveys & roadmaps",
    "docs/end-to-end.md": "End-to-end driving", "docs/perception-mapping.md": "Perception & maps",
    "docs/prediction-planning.md": "Prediction & planning", "docs/llm-vlm.md": "LLM / VLM", "docs/vla.md": "Vision-Language-Action",
    "docs/reasoning-rl.md": "Reasoning & RL", "docs/world-models.md": "World models", "docs/simulation.md": "Simulation & scenarios",
    "docs/safety-robustness.md": "Safety & robustness", "docs/cooperative-v2x.md": "Cooperative & V2X", "docs/industry.md": "Industry systems",
    "docs/datasets.md": "Datasets", "docs/benchmarks.md": "Benchmarks",
}
# which pages render resource bullets as cards, and what kind/area they are
KIND = {  # path prefix -> (type, area)
    "docs/surveys.md": ("paper", "general"),
    "docs/end-to-end.md": ("paper", "e2e"),
    "docs/perception-mapping.md": ("paper", "e2e"),
    "docs/prediction-planning.md": ("paper", "e2e"),
    "docs/llm-vlm.md": ("paper", "language"),
    "docs/vla.md": ("paper", "language"),
    "docs/reasoning-rl.md": ("paper", "language"),
    "docs/world-models.md": ("paper", "world"),
    "docs/simulation.md": ("paper", "world"),
    "docs/safety-robustness.md": ("paper", "safety"),
    "docs/cooperative-v2x.md": ("paper", "safety"),
    "docs/industry.md": ("paper", "safety"),
    "docs/recent.md": ("paper", "general"),
    "docs/datasets.md": ("dataset", "eval"),
    "docs/benchmarks.md": ("benchmark", "eval"),
    "docs/tools.md": ("tool", "general"),
    "docs/learning.md": ("learning", "general"),
    "docs/competitions.md": ("competition", "general"),
    "docs/organizations.md": ("org", "general"),
}
NO_ENTRIES = {"README.md", "CONTRIBUTING.md"}
AREAS = {
    "e2e": ("End-to-end & modular stack", "Sensors-to-plan models, BEV and occupancy perception, forecasting and planners.", ["docs/end-to-end.md", "docs/perception-mapping.md", "docs/prediction-planning.md"]),
    "language": ("LLM, VLM, VLA & reasoning", "Language and vision-language drivers, action models, chain-of-thought and RL post-training.", ["docs/vla.md", "docs/llm-vlm.md", "docs/reasoning-rl.md"]),
    "world": ("World models & simulation", "Generative world models, world-action models, 3DGS reconstruction, simulators and scenario generation.", ["docs/world-models.md", "docs/simulation.md"]),
    "eval": ("Data & evaluation", "Driving datasets and open-loop, closed-loop and VLM benchmarks.", ["docs/datasets.md", "docs/benchmarks.md"]),
    "safety": ("Safety, V2X & industry", "Attacks and robustness, cooperative driving, and industry system reports.", ["docs/safety-robustness.md", "docs/cooperative-v2x.md", "docs/industry.md"]),
}
AREA_SHORT = {"e2e": "end-to-end", "language": "language & VLA", "world": "world-model & simulation", "eval": "data & evaluation", "safety": "safety & industry"}
SKIP_TILES = set()
TYPES = {"paper": "Papers", "dataset": "Datasets", "benchmark": "Benchmarks", "tool": "Tools", "learning": "Learning",
         "competition": "Competitions", "org": "Organizations"}
SOURCES = {
    "arxiv.org": "arXiv", "ieeexplore.ieee.org": "IEEE", "link.springer.com": "Springer", "sciencedirect.com": "ScienceDirect",
    "nature.com": "Nature", "science.org": "Science", "spj.science.org": "Science", "arc.aiaa.org": "AIAA", "ncbi.nlm.nih.gov": "PMC",
    "pmc.ncbi.nlm.nih.gov": "PMC", "github.com": "GitHub", "huggingface.co": "Hugging Face", "ntrs.nasa.gov": "NASA NTRS",
    "nasa.gov": "NASA", "esa.int": "ESA", "researchgate.net": "ResearchGate", "semanticscholar.org": "Semantic Scholar",
    "academia.edu": "Academia", "doi.org": "DOI", "youtube.com": "YouTube", "youtu.be": "YouTube", "zenodo.org": "Zenodo",
    "frontiersin.org": "Frontiers", "dl.acm.org": "ACM", "aclanthology.org": "ACL", "wiley.com": "Wiley", "onlinelibrary.wiley.com": "Wiley",
    "agupubs.onlinelibrary.wiley.com": "AGU", "openaccess.thecvf.com": "CVF", "kelvins.esa.int": "ESA Kelvins", "slab.stanford.edu": "Stanford SLAB",
    "purl.stanford.edu": "Stanford", "pith.science": "Pith", "mdpi.com": "MDPI", "ieee-dataport.org": "IEEE DataPort", "hou.usra.edu": "USRA",
}
errors = []

# ---------------------------------------------------------------- helpers
def slugify(value, sep="-"):
    v = re.sub(r"[^\w\- ]", "", value.strip().lower())
    return re.sub(r" ", sep, v)

def page_url(md_path):
    return md_path[: -len("README.md")] + "index.html" if md_path.endswith("README.md") else md_path[:-3] + ".html"

def rel(from_url, to_url):
    return posixpath.relpath(to_url, posixpath.dirname(from_url) or ".")

def md_files():
    out = []
    for p in sorted(ROOT.rglob("*.md")):
        r = p.relative_to(ROOT).as_posix()
        if r.startswith((".git/", ".github/", "_site/", "website/", "scripts/", "data/")):
            continue
        out.append(r)
    return out

def autolink_bare_urls(text):
    def fix(line):
        if "](" in line or "<http" in line:
            return line
        return re.sub(r"(?<![\(<\"'])\bhttps?://[^\s)<>\]]+", lambda m: f"<{m.group(0)}>", line)
    return "\n".join(fix(l) for l in text.split("\n"))

def strip_md(s):
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"[*_`]", "", s)
    return re.sub(r"\s+", " ", s).strip()

def kind_of(path):
    best = None
    for pre, v in KIND.items():
        if path == pre or (pre.endswith("/") and path.startswith(pre)):
            if best is None or len(pre) > len(best[0]):
                best = (pre, v)
    return best[1] if best else ("report", "general")

def source_of(url):
    host = urlparse(url).netloc.lower().removeprefix("www.")
    for k, v in SOURCES.items():
        if host == k or host.endswith("." + k):
            return v
    return host

def year_of(url, text):
    m = re.search(r"arxiv\.org/(?:abs|pdf|html)/(\d{2})(\d{2})\.\d{4,5}", url)
    if m and 7 <= int(m.group(1)) <= 40:
        return 2000 + int(m.group(1))
    m = re.findall(r"(?<![\w.])((?:19[89]|20[0-3])\d)(?![\w.])", text)
    return int(m[-1]) if m else 0

def year_from(venue, url, text):
    """Venue year first (published year), then arXiv id, then a year in the title (ignoring 'Mars 2020')."""
    m = re.search(r"(?<!\d)((?:19|20)\d{2})(?!\d)", venue)
    if m:
        return int(m.group(1))
    return year_of(url, re.sub(r"Mars 2020", "", text))

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")

def parse_bullet(line):
    """'- Title (note): [Link](url) - [File](path)' -> dict(title, desc, links)."""
    body = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", line.rstrip())
    venue = ""
    mv = re.search(r"\s+·\s+\*([^*]+)\*\s*$", body)       # trailing "· *Venue Year*"
    if mv:
        venue, body = mv.group(1).strip(), body[: mv.start()]
    links = [(m.group(1).strip(), m.group(2)) for m in LINK_RE.finditer(body)]
    text = LINK_RE.sub("", body)
    text = re.sub(r"<(https?://[^>]+)>", "", text)
    text = re.sub(r"\s+([·\-—|]\s*)+$", "", text.strip())
    text = re.sub(r"[\s:·\-—|]+$", "", text)
    desc = ""
    m = re.match(r"^\*\*(.+?)\*\*\s*[:—-]?\s*(.*)$", text)
    if m:
        title, desc = m.group(1), m.group(2)
    else:
        title = text
        m = re.match(r"^(.*\S)\s+\(([^()]{12,})\)$", title)
        if m and len(m.group(1)) >= 15:
            title, desc = m.group(1), m.group(2)
    title = re.sub(r"[*_`]", "", title).strip()
    desc = re.sub(r"[*_`]", "", desc).strip(" :·-—")
    m = re.match(r"^\(([^)]*)\)\s*:?\s*(.+)$", desc)          # "(from X): text" -> "text (from X)"
    if m:
        desc = f"{m.group(2)} ({m.group(1)})"
    desc = re.sub(r"\s+[Ss]ee\s*\.?$", "", desc)               # dangling "See" left by a removed link
    desc = (desc[:1].upper() + desc[1:]) if desc else desc
    return {"title": title, "desc": desc, "links": links, "venue": venue}

def parse_row(line, header):
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if not cells or not any(cells):
        return None
    links = [(m.group(1).strip(), m.group(2)) for c in cells for m in LINK_RE.finditer(c)]
    first = strip_md(cells[0])
    rest = " · ".join(strip_md(c) for c in cells[1:] if strip_md(c))
    return {"title": first, "desc": rest, "links": links}

# ---------------------------------------------------------------- pages
class Page:
    def __init__(self, path):
        self.path = path
        self.url = page_url(path)
        self.type, self.area = kind_of(path)
        text = (ROOT / path).read_text(encoding="utf-8")
        m = re.search(r"^# (.+)$", text, re.M)
        self.title = m.group(1).strip() if m else Path(path).stem
        self.label = SHORT.get(path, self.title)
        self.entries, self.sections = [], []   # sections: (id, name, count)
        self.cards = {}
        self.src = text
        text = self.extract(text)
        md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "sane_lists"],
                               extension_configs={"toc": {"slugify": slugify, "toc_depth": "2-3"}})
        self.html = md.convert(autolink_bare_urls(text))
        self.toc = [t for h1 in md.toc_tokens for t in (h1["children"] if h1["level"] == 1 else [h1])]
        self.ids = set(re.findall(r'id="([^"]+)"', self.html))
        for k, v in self.cards.items():
            self.html = self.html.replace(f"<p>@@CARDS{k}@@</p>", v)

    def area_for_section(self, section):
        return self.area

    def extract(self, text):
        """Collect entries; replace runs of linked bullets with card placeholders."""
        if self.path in NO_ENTRIES:
            return text
        lines, out = text.split("\n"), []
        section, sid, i, n = self.title, "", 0, 0
        header = None
        while i < len(lines):
            line = lines[i]
            h = re.match(r"^(#{2,3}) (.+)$", line)
            if h:
                section, sid = h.group(2).strip(), slugify(h.group(2))
                if h.group(1) == "##":
                    self.sections.append([sid, section, 0])
                out.append(line); i += 1; continue
            if re.match(r"^- ", line):
                run = []
                while i < len(lines) and re.match(r"^- ", lines[i]):
                    run.append(lines[i]); i += 1
                parsed = [parse_bullet(l) for l in run]
                if all(p["links"] for p in parsed) and len(parsed) >= 1:
                    cards = []
                    for p in parsed:
                        e = self.make_entry(p, section, sid)
                        if e: cards.append(e)
                    n += 1
                    self.cards[n] = '<div class="cards">' + "".join(card_html(e) for e in cards) + "</div>"
                    out += ["", f"@@CARDS{n}@@", ""]
                else:
                    for p, l in zip(parsed, run):
                        if p["links"]: self.make_entry(p, section, sid)
                    out += run
                continue
            if line.startswith("|"):
                if re.match(r"^\|[\s\-|:]+\|?$", line):
                    out.append(line); i += 1; continue
                if i + 1 < len(lines) and re.match(r"^\|[\s\-|:]+\|?$", lines[i + 1]):
                    header = [c.strip() for c in line.strip("|").split("|")]
                else:
                    p = parse_row(line, header)
                    if p and p["links"]: self.make_entry(p, section, sid)
            out.append(line); i += 1
        return "\n".join(out)

    def make_entry(self, p, section, sid):
        if len(p["title"]) < 3:
            return None
        ext = [(l, u) for l, u in p["links"] if u.startswith("http")]
        loc = [(l, u) for l, u in p["links"] if not u.startswith("http")]
        primary = next(((l, u) for l, u in ext if l.lower() in ("link", "paper")), ext[0] if ext else (loc[0] if loc else None))
        text = p["title"] + " " + p["desc"]
        e = {"title": p["title"], "desc": p["desc"], "venue": p.get("venue", ""), "page": self, "section": section, "sid": sid,
             "links": p["links"], "primary": primary, "type": self.type,
             "area": self.area_for_section(section), "src": source_of(primary[1]) if primary and primary[1].startswith("http") else "",
             "year": year_from(p.get("venue", ""), primary[1] if primary else "", text),
             "arxiv": bool(primary and "arxiv.org" in primary[1]), "pdf": any(not u.startswith("http") and u.endswith(".pdf") for _, u in p["links"])}
        self.entries.append(e)
        for s in self.sections:
            if s[0] == sid: s[2] += 1
        return e

def pill_label(label, url, taken):
    if not url.startswith("http"):
        return "PDF" if url.endswith(".pdf") else "Page"
    l = label if label.lower() not in ("link",) else source_of(url)
    return l

def card_html(e):
    chips = []
    if e["src"]: chips.append(f'<span class="chip src">{html.escape(e["src"])}</span>')
    if e["year"]: chips.append(f'<span class="chip">{e["year"]}</span>')
    if e["venue"]: chips.append(f'<span class="chip venue">{html.escape(e["venue"])}</span>')
    elif e["arxiv"]: chips.append('<span class="chip pre">preprint</span>')
    if e["pdf"]: chips.append('<span class="chip pdf">PDF in repo</span>')
    pl = e["primary"]
    title = html.escape(e["title"])
    if pl:
        t = f'<a href="{html.escape(pl[1])}">{title}<span class="ext" aria-hidden="true"></span></a>'
    else:
        t = title
    actions = []
    for label, url in e["links"]:
        if pl and url == pl[1] and len(e["links"]) > 1 and url.startswith("http"):
            continue
        if len(e["links"]) == 1:
            continue
        actions.append(f'<a class="pill" href="{html.escape(url)}">{html.escape(pill_label(label, url, None))}</a>')
    desc = f'<p class="card-desc">{html.escape(e["desc"])}</p>' if e["desc"] else ""
    return (f'<article class="card" data-area="{e["area"]}">'
            f'<div class="card-top">{"".join(chips)}</div><h3 class="card-title">{t}</h3>{desc}'
            f'{"<div class=card-actions>" + "".join(actions) + "</div>" if actions else ""}</article>')

def flatten(tokens, acc=None):
    acc = acc if acc is not None else []
    for t in tokens:
        acc.append(t); flatten(t["children"], acc)
    return acc

def target_url(page_path, href, pages, lib_exists):
    """Resolve a relative href to a site-root-relative url, or None."""
    path, _, frag = href.partition("#")
    target = posixpath.normpath(posixpath.join(posixpath.dirname(page_path), path)) if path else page_path
    if target.endswith(".md") and target in pages:
        return pages[target].url + ("#" + frag if frag else "")
    if target.rstrip("/") == "library" and lib_exists:
        return "library/index.html"
    if target.startswith(("library/", "assets/")) and (ROOT / target).exists():
        return target
    return None

def resolve_links(page, pages, lib_exists):
    def sub(m):
        attr, val = m.group(1), m.group(2)
        if val.startswith("http") or val.startswith("mailto:"):
            return m.group(0)
        if val.startswith("#"):
            if val[1:] not in page.ids:
                errors.append(f"{page.path}: missing anchor {val}")
            return m.group(0)
        path, _, frag = val.partition("#")
        target = posixpath.normpath(posixpath.join(posixpath.dirname(page.path), path))
        if target.endswith(".md"):
            if target not in pages:
                errors.append(f"{page.path}: broken link {val}"); return m.group(0)
            if frag and frag not in pages[target].ids:
                errors.append(f"{page.path}: missing anchor #{frag} in {target}")
            return f'{attr}="{rel(page.url, pages[target].url)}{"#" + frag if frag else ""}"'
        if target.rstrip("/") == "library" and lib_exists:
            return f'{attr}="{rel(page.url, "library/index.html")}"'
        if (ROOT / target).is_dir() and (ROOT / target / "README.md").exists():
            return f'{attr}="{rel(page.url, pages[target.rstrip("/") + "/README.md"].url)}"'
        if target.startswith(("library/", "assets/")) and (ROOT / target).exists():
            return f'{attr}="{rel(page.url, target)}"'
        if (ROOT / target).is_dir():
            return f'{attr}="{REPO}/tree/main/{target}" target="_blank" rel="noopener"'
        if (ROOT / target).exists():
            return f'{attr}="{REPO}/blob/main/{target}" target="_blank" rel="noopener"'
        errors.append(f"{page.path}: broken link {val}"); return m.group(0)
    page.html = re.sub(r'(href|src)="([^"]*)"', sub, page.html)
    page.html = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', page.html)
    page.html = page.html.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")

# ---------------------------------------------------------------- navigation bits
def nav_pages(pages):
    seq = []
    for label, t in NAV:
        for p in ([t] if isinstance(t, str) else t):
            if p.endswith(".md") and p in pages: seq.append(p)
            elif p == "@explore": seq.append(p)
            elif p == "library/": seq.append(p)
    return seq

def url_of(path, pages):
    return {"@explore": "explore.html", "library/": "library/index.html"}.get(path) or pages[path].url

def label_of(path, pages):
    return {"@explore": "Explore all", "library/": "Library"}.get(path) or SHORT.get(path, pages[path].title)

def group_of(path):
    for label, t in NAV:
        if isinstance(t, list) and path in t: return label
    return None

def nav_html(pages, current_url, lib_exists):
    out = []
    def link(path, label=None):
        if path == "library/" and not lib_exists: return ""
        url = url_of(path, pages); label = label_of(path, pages) if path in SHORT or path.startswith(("@", "library")) else (label or pages[path].title)
        cur = ' aria-current="page"' if url == current_url else ""
        return f'<a href="{rel(current_url, url)}"{cur}>{html.escape(label)}</a>'
    for label, target in NAV:
        if isinstance(target, str):
            out.append(f'<div class="nav-item">{link(target, label)}</div>')
        else:
            urls = [url_of(t, pages) for t in target]
            op = " open" if current_url in urls else ""
            out.append(f'<details{op}><summary>{html.escape(label)}</summary>' + "".join(link(t) for t in target) + "</details>")
    return "\n".join(out)

def breadcrumbs(pg_path, url, pages):
    parts = [f'<a href="{rel(url, "index.html")}">Home</a>']
    g = group_of(pg_path)
    if g:
        first = next(t for l, t in NAV if l == g)[0]
        parts.append(f'<a href="{rel(url, url_of(first, pages))}">{html.escape(g)}</a>')
    parts.append(f'<span aria-current="page">{html.escape(label_of(pg_path, pages))}</span>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<span class="sep">›</span>'.join(parts) + "</nav>"

def prev_next(pg_path, url, pages, lib_exists):
    seq = [p for p in nav_pages(pages) if p != "README.md" and (p != "library/" or lib_exists)]
    if pg_path not in seq: return ""
    i = seq.index(pg_path)
    def box(p, cls, arrow):
        return (f'<a class="pn {cls}" href="{rel(url, url_of(p, pages))}"><span class="pn-k">{arrow}</span>'
                f'<span class="pn-t">{html.escape(label_of(p, pages))}</span></a>')
    a = box(seq[i - 1], "prev", "← Previous") if i > 0 else "<span></span>"
    b = box(seq[i + 1], "next", "Next →") if i + 1 < len(seq) else "<span></span>"
    return f'<nav class="prevnext" aria-label="Pagination">{a}{b}</nav>'

def jump_chips(pg):
    secs = [s for s in pg.sections if s[2] > 0]
    if len(secs) < 4: return ""
    chips = "".join(f'<a href="#{s[0]}">{html.escape(s[1])} <b>{s[2]}</b></a>' for s in secs)
    return f'<nav class="jump" aria-label="Topics on this page">{chips}</nav>'

# ---------------------------------------------------------------- special pages
def home_body(pages, entries, all_entries):
    def count(types=None, area=None):
        return len([e for e in entries if (not types or e["type"] in types) and (not area or e["area"] == area)])
    recent = len([e for e in entries if e["year"] >= 2025 and e["type"] in ("paper", "benchmark")])
    stats = [(count({"paper"}), "papers"), (recent, "from 2025-26"), (count({"dataset"}), "datasets"),
             (count({"benchmark"}), "benchmarks"), (count({"tool"}), "tools")]
    chips = "".join(f'<li><b>{v}</b><span>{html.escape(l)}</span></li>' for v, l in stats)
    hero = (f'<section class="hero"><div class="hero-inner"><p class="eyebrow">Open research map</p>'
            f'<h1>{SITE_NAME}</h1><p class="lead">{html.escape(TAGLINE)}</p>'
            f'<div class="cta"><a class="btn primary" href="docs/recent.html">What is new in 2025-26</a>'
            f'<a class="btn" href="explore.html">Explore all {len(entries)} resources</a>'
            f'<button class="btn" id="hero-search" type="button">Search <kbd>/</kbd></button></div>'
            f'<ul class="stats">{chips}</ul></div></section>')
    area_cards = ""
    for key, (name, desc, paths) in AREAS.items():
        pgs = [pages[p] for p in paths]
        n = len([e for e in entries if e["area"] == key and e["type"] in ("paper", "benchmark")])
        d = len([e for e in entries if e["area"] == key and e["type"] == "dataset"])
        secs = [(q, s_) for q in pgs for s_ in q.sections if s_[2] > 0][:5]
        links = "".join(f'<a href="{q.url}#{s_[0]}">{html.escape(s_[1])}</a>' for q, s_ in secs)
        meta = (f'<b>{n}</b> papers' if n else "") + (f' · <b>{d}</b> datasets' if d else "")
        area_cards += (f'<article class="area" data-area="{key}"><h3><a href="{pgs[0].url}">{html.escape(name)}</a></h3>'
                       f'<p>{html.escape(desc)}</p><p class="area-meta">{meta}</p>'
                       f'<div class="area-links">{links}</div>'
                       f'<a class="area-go" href="explore.html?area={key}">Browse all {html.escape(AREA_SHORT[key])} →</a></article>')
    tiles = ""
    for key, (name, _, paths) in AREAS.items():
        t = ""
        for p in paths:
            pg = pages[p]
            t += "".join(f'<a class="tile" data-area="{key}" href="{pg.url}#{s_[0]}"><span class="tile-n">{s_[2]}</span>'
                         f'<span class="tile-t">{html.escape(s_[1])}</span></a>' for s_ in pg.sections if s_[2] > 0 and s_[1].lower() not in SKIP_TILES)
        tiles += f'<h3 class="tile-h" data-area="{key}">{html.escape(name)}</h3><div class="tiles">{t}</div>'
    steps = [("1", "Orient", "Surveys and roadmaps", "docs/surveys.html"),
             ("2", "Catch up", "What changed in 2025-26", "docs/recent.html"),
             ("3", "Methods", "End-to-end, VLA, world models", "docs/end-to-end.html"),
             ("4", "Data", "Datasets to train on", "docs/datasets.html"),
             ("5", "Evaluate", "Open and closed-loop benchmarks", "docs/benchmarks.html"),
             ("6", "Build", "Simulators and devkits", "docs/tools.html")]
    stepper = '<ol class="steps">' + "".join(
        f'<li><a href="{u}"><span class="step-n">{n}</span><b>{t}</b><span>{html.escape(d)}</span></a></li>' for n, t, d, u in steps) + "</ol>"
    quick = [("Datasets", "nuScenes, Waymo, WOD-E2E and language/VQA driving data.", "docs/datasets.html", f'{count({"dataset"})} entries'),
             ("Benchmarks", "NAVSIM, Bench2Drive, DriveBench and world-model evaluation.", "docs/benchmarks.html", f'{count({"benchmark"})} entries'),
             ("Tools", "CARLA, Waymax, MetaDrive, Autoware and devkits.", "docs/tools.html", f'{count({"tool"})} entries'),
             ("Competitions", "Waymo, CARLA Leaderboard, CVPR Grand Challenge.", "docs/competitions.html", f'{count({"competition"})} entries'),
             ("Organizations", "Industry and academic groups to follow.", "docs/organizations.html", f'{count({"org"})} entries'),
             ("Contribute", "Suggest a paper or fix an entry.", f"{REPO}/blob/main/CONTRIBUTING.md", "GitHub")]
    qc = "".join(f'<a class="quick" href="{u}"><b>{html.escape(t)}</b><span>{html.escape(d)}</span><em>{m}</em></a>' for t, d, u, m in quick)
    return (hero + '<div class="home-wrap">'
            '<h2 class="sec" id="areas">Explore by area</h2><div class="areas">' + area_cards + "</div>"
            '<h2 class="sec" id="path">A suggested path</h2>' + stepper +
            '<h2 class="sec" id="topics">Browse by topic</h2><p class="muted">Every topic section across the paper pages. The number is how many entries it holds.</p>' + tiles +
            '<h2 class="sec" id="more">More resources</h2><div class="quicks">' + qc + "</div></div>")

def explore_body():
    return ('<div class="prose"><h1>Explore all resources</h1>'
            '<p class="muted">Filter every paper, dataset, benchmark, tool, course, competition and organization in one place. Filters are saved in the address bar, so you can share a view.</p></div>'
            '<div id="explorer" class="explorer"><div class="ex-bar">'
            '<input id="ex-q" type="search" placeholder="Search titles and descriptions…" aria-label="Search resources">'
            '<select id="ex-src" aria-label="Source"><option value="">All sources</option></select>'
            '<select id="ex-sort" aria-label="Sort"><option value="rel">Relevance</option><option value="new">Newest first</option><option value="old">Oldest first</option><option value="az">A to Z</option></select></div>'
            '<div class="ex-chips" id="ex-area" role="group" aria-label="Area"></div>'
            '<div class="ex-chips" id="ex-type" role="group" aria-label="Type"></div>'
            '<p id="ex-count" class="muted" aria-live="polite"></p><div id="ex-list" class="cards"></div>'
            '<button id="ex-more" class="btn" type="button" hidden>Show more</button>'
            '<noscript><p>This page needs JavaScript. Use the sidebar to browse the pages instead.</p></noscript></div>')

def library_page():
    lib = ROOT / "library"
    rows = []
    for sub in sorted(p for p in lib.iterdir() if p.is_dir()):
        items = "".join(
            f'<article class="card"><h3 class="card-title"><a href="{sub.name}/{html.escape(f.name)}">{html.escape(f.stem.replace("_", " "))}'
            f'<span class="ext" aria-hidden="true"></span></a></h3><div class="card-top"><span class="chip pdf">PDF</span>'
            f'<span class="chip">{f.stat().st_size/1e6:.1f} MB</span></div></article>' for f in sorted(sub.glob("*.pdf")))
        rows.append(f'<h2 id="{sub.name}">{sub.name.title()}</h2><div class="cards">{items}</div>')
    body = ("<h1>Library</h1><p>Local PDF copies of freely redistributable papers, reports and proposals. IEEE and other restricted papers are link-only in the paper lists. "
            f'Files keep their original licenses; see the repository <a href="{REPO}/blob/main/LICENSE" target="_blank" rel="noopener">LICENSE</a>.</p>' + "".join(rows))
    toc = [{"level": 2, "id": s.name, "name": s.name.title(), "children": []} for s in sorted(p for p in lib.iterdir() if p.is_dir())]
    return body, toc

# ---------------------------------------------------------------- output
TEMPLATE = (ROOT / "website" / "template.html").read_text(encoding="utf-8")

def topnav(url):
    out = []
    for label, u in [("Recent", "docs/recent.html"), ("Papers", "docs/vla.html"), ("Data", "docs/datasets.html"),
                     ("Tools", "docs/tools.html"), ("Explore", "explore.html")]:
        cur = ' aria-current="page"' if url == u else ""
        out.append(f'<a href="{rel(url, u)}"{cur}>{label}</a>')
    return "".join(out)

def render(path, pages, lib_exists, body, title, url, toc=None, edit=None, home=False, extra_class=""):
    toc = toc or []
    flat = flatten(toc)
    toc_html = ""
    if len(flat) >= 3 and not home:
        toc_html = '<nav class="toc" aria-label="On this page"><h2>On this page</h2><ul>' + "".join(
            f'<li class="l{t["level"]}"><a href="#{t["id"]}">{html.escape(html.unescape(strip_md(t["name"])))}</a></li>' for t in flat) + "</ul></nav>"
    prefix = rel(url, "x").replace("x", "") or "./"
    page = TEMPLATE
    repl = {"{{TITLE}}": html.escape(SITE_NAME if home else f"{title} · {SITE_NAME}"), "{{PREFIX}}": prefix,
            "{{NAV}}": nav_html(pages, url, lib_exists), "{{BODY}}": body, "{{TOC}}": toc_html,
            "{{EDIT}}": edit or REPO, "{{REPO}}": REPO, "{{CLASS}}": ("home" if home else "doc") + extra_class,
            "{{SITE}}": SITE_NAME, "{{DESC}}": html.escape(TAGLINE),
            "{{TOPNAV}}": topnav(url)}
    for k, v in repl.items():
        page = page.replace(k, v)
    return page

def edit_url(path):
    """Generated topic pages are edited through their YAML source."""
    slug = Path(path).stem
    if path.startswith("docs/") and (ROOT / "data" / f"{slug}.yaml").exists():
        return f"{REPO}/edit/main/data/{slug}.yaml"
    return f"{REPO}/edit/main/{path}"

def entry_json(e, pages, lib_exists):
    def url(u):
        return u if u.startswith("http") else (target_url(e["page"].path, u, pages, lib_exists) or "")
    pl = e["primary"]
    return {"t": e["title"][:240], "d": e["desc"][:240], "p": e["page"].label, "s": e["section"],
            "h": e["page"].url + ("#" + e["sid"] if e["sid"] else ""), "u": url(pl[1]) if pl else "",
            "a": e["area"], "k": e["type"], "src": e["src"], "y": e["year"], "pdf": 1 if e["pdf"] else 0,
            "v": e["venue"], "c": next((u for l, u in e["links"] if "github.com" in u), "")}

def main():
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    pages = {p: Page(p) for p in md_files()}
    lib_exists = (ROOT / "library").is_dir()
    for pg in pages.values():
        resolve_links(pg, pages, lib_exists)
    in_nav = {p for _, t in NAV for p in ([t] if isinstance(t, str) else t)}
    for p in in_nav:
        if p.endswith(".md") and p not in pages: errors.append(f"nav references missing file {p}")
    for p in pages:
        if p not in in_nav: print(f"note: {p} is built but not in the sidebar")
    if errors:
        print("\n".join(sorted(set(errors)))); sys.exit(1)

    all_entries = [e for pg in pages.values() for e in pg.entries]          # per-page counts (home stats)
    entries, seen = [], set()                                               # one card per paper in Explore and search
    ranked = sorted(all_entries, key=lambda e: (e["type"] != "paper", not e["venue"], not any("github.com" in u for _, u in e["links"]),
                                                  e["page"].path == "docs/recent.md", e["area"] == "general"))
    for e in ranked:
        key = e["primary"][1] if e["primary"] and e["primary"][1].startswith("http") else None
        if key and key in seen:
            continue
        if key: seen.add(key)
        entries.append(e)
    for pg in pages.values():
        home = pg.path == "README.md"
        if home:
            body = home_body(pages, entries, all_entries); toc = []
        else:
            head = re.match(r"^\s*(<h1[^>]*>.*?</h1>)", pg.html, re.S)
            h1 = head.group(1) if head else ""
            rest = pg.html[len(head.group(0)):] if head else pg.html
            body = (breadcrumbs(pg.path, pg.url, pages) + '<div class="prose">' + h1 + jump_chips(pg) + rest + "</div>"
                    + prev_next(pg.path, pg.url, pages, lib_exists))
            toc = pg.toc
        dest = OUT / pg.url
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render(pg.path, pages, lib_exists, body, pg.title, pg.url, toc, edit_url(pg.path), home), encoding="utf-8")

    (OUT / "explore.html").write_text(render("@explore", pages, lib_exists, breadcrumbs("@explore", "explore.html", pages) + explore_body()
                                             + prev_next("@explore", "explore.html", pages, lib_exists), "Explore all", "explore.html", extra_class=" wide"), encoding="utf-8")
    if lib_exists:
        shutil.copytree(ROOT / "library", OUT / "library")
        body, toc = library_page()
        (OUT / "library" / "index.html").write_text(render("library/", pages, lib_exists,
            breadcrumbs("library/", "library/index.html", pages) + '<div class="prose">' + body + "</div>" + prev_next("library/", "library/index.html", pages, lib_exists),
            "Library", "library/index.html", toc), encoding="utf-8")
    (OUT / "assets").mkdir(exist_ok=True)
    banner = ROOT / "assets" / "banner.png"
    try:
        from PIL import Image
        im = Image.open(banner).convert("RGB"); im.thumbnail((1800, 1000)); im.save(OUT / "assets" / "banner.jpg", quality=78, optimize=True)
    except Exception:
        shutil.copy(banner, OUT / "assets" / "banner.jpg")
    shutil.copytree(ROOT / "website" / "static", OUT / "static")
    idx = [entry_json(e, pages, lib_exists) for e in entries]
    (OUT / "search-index.json").write_text(json.dumps(idx, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    (OUT / ".nojekyll").write_text("")
    print(f"built {len(pages)} pages, {len(entries)} entries -> {OUT}")

if __name__ == "__main__":
    main()
