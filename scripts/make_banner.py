#!/usr/bin/env python3
"""Generate assets/banner.png: road in perspective, LiDAR-style rings and detection boxes.

Usage: python scripts/make_banner.py   (needs pillow)
"""
from __future__ import annotations

import math
import pathlib

from PIL import Image, ImageDraw, ImageFilter

W, H, HORIZON = 1800, 800, 300
TEAL, AMBER, ROSE = (45, 212, 191), (255, 194, 71), (251, 122, 155)
OUT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "banner.png"


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def road_x(side: int, y: float, half_bottom: float = 760, half_top: float = 6) -> float:
    t = (y - HORIZON) / (H - HORIZON)
    return W / 2 + side * (half_top + (half_bottom - half_top) * t)


def main() -> None:
    img = Image.new("RGB", (W, H))
    px = ImageDraw.Draw(img)
    top, mid, bottom = (7, 13, 14), (13, 38, 40), (9, 20, 22)
    for y in range(H):
        px.line([(0, y), (W, y)], fill=lerp(top, mid, y / HORIZON) if y < HORIZON else lerp(mid, bottom, (y - HORIZON) / (H - HORIZON)))

    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    g = ImageDraw.Draw(glow)
    g.ellipse((W / 2 - 520, HORIZON - 120, W / 2 + 520, HORIZON + 120), fill=TEAL + (70,))
    img = Image.alpha_composite(img.convert("RGBA"), glow.filter(ImageFilter.GaussianBlur(70)))

    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.polygon([(road_x(-1, HORIZON), HORIZON), (road_x(1, HORIZON), HORIZON), (road_x(1, H), H), (road_x(-1, H), H)], fill=(10, 20, 22, 235))
    for side in (-1, 1):
        d.line([(road_x(side, HORIZON), HORIZON), (road_x(side, H), H)], fill=TEAL + (170,), width=3)
    # dashed centre line, spacing grows with perspective
    y = HORIZON + 4.0
    while y < H:
        t = (y - HORIZON) / (H - HORIZON)
        length = 4 + 70 * t * t
        y2 = min(H, y + length)
        w0, w1 = 1 + 9 * t, 1 + 9 * min(1, (y2 - HORIZON) / (H - HORIZON))
        cx = W / 2
        d.polygon([(cx - w0, y), (cx + w0, y), (cx + w1, y2), (cx - w1, y2)], fill=AMBER + (230,))
        y = y2 + 6 + 90 * t * t
    # sensor rings around the ego vehicle
    ego = (W / 2, H + 40)
    for r in range(1, 6):
        rx, ry = 190 * r, 62 * r
        d.ellipse((ego[0] - rx, ego[1] - ry, ego[0] + rx, ego[1] + ry), outline=TEAL + (max(30, 120 - 20 * r),), width=2)
    # detection boxes (pseudo-3D: front face + offset back face)
    boxes = [(-0.42, 0.38, TEAL), (0.34, 0.55, AMBER), (0.58, 0.30, TEAL), (-0.15, 0.20, ROSE), (-0.62, 0.62, TEAL)]
    for lane, depth, col in boxes:
        yy = HORIZON + (H - HORIZON) * depth
        t = depth
        cx = W / 2 + lane * (road_x(1, yy) - W / 2)
        bw, bh = 150 * t + 14, 90 * t + 9
        d.rectangle((cx - bw / 2, yy - bh, cx + bw / 2, yy), outline=col + (230,), width=2)
        dx, dy = bw * 0.18, bh * 0.25
        d.rectangle((cx - bw / 2 + dx, yy - bh - dy, cx + bw / 2 + dx, yy - dy), outline=col + (130,), width=1)
        for (ax, ay), (bx, by) in [((cx - bw / 2, yy - bh), (cx - bw / 2 + dx, yy - bh - dy)), ((cx + bw / 2, yy - bh), (cx + bw / 2 + dx, yy - bh - dy)),
                                   ((cx + bw / 2, yy), (cx + bw / 2 + dx, yy - dy))]:
            d.line([(ax, ay), (bx, by)], fill=col + (130,), width=1)
    # planned trajectory
    pts = []
    for i in range(0, 41):
        t = i / 40
        yy = H - 10 - (H - HORIZON - 60) * t
        pts.append((W / 2 + 120 * math.sin(t * 2.2) * (1 - t) * 1.2, yy))
    d.line(pts, fill=(255, 255, 255, 215), width=4, joint="curve")
    img = Image.alpha_composite(img, layer).convert("RGB")
    OUT.parent.mkdir(exist_ok=True)
    img.save(OUT, optimize=True)
    print(f"wrote {OUT} ({OUT.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
