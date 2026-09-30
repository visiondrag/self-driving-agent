# Contributing

1. Pick the right file in `data/` (topic = file, section = group inside it).
2. Add one line to the section's `papers:` list:

   ```yaml
   - {id: "2406.03877", title: "Bench2Drive: ...", venue: "NeurIPS'24 D&B", code: "https://github.com/...", note: "one short takeaway"}
   ```

   - `id`: arXiv id (`YYMM.NNNNN`). No arXiv paper? use `url:` and set `year:` instead.
   - `title`: exact arXiv title (the verifier compares it).
   - `venue` (optional): `CVPR'25`, `NeurIPS'24 D&B`, `arXiv`, ...
   - `org`, `code`, `note` optional. Keep notes to one short line; say *why* the paper matters.
3. Run `python scripts/build.py` and commit both `data/` and the regenerated `docs/` + `README.md`.
4. Run `python scripts/verify.py` if you have network access; CI does it too.

A paper may appear in several topics when it genuinely belongs to each (e.g. EMMA in VLA and Industry).

Inclusion bar: peer-reviewed, widely cited, released code/data, a strong benchmark result, or a clear new idea.
Recent arXiv-only papers are welcome if they meet one of those.
