#!/usr/bin/env python3
"""WCAG 2.2 contrast checker for brand palettes (stdlib only).

Usage:
  contrast_check.py FG:BG[:label] [FG:BG[:label] ...] [--large]
  contrast_check.py --json pairs.json        # [{"fg":"#fff","bg":"#0E7C66","label":"onPrimary/primary","large":false}]

Exit code 1 if any pair fails, so it can gate CI.
Thresholds: normal text 4.5:1, large text / UI components / icons 3:1 (WCAG 2.2 SC 1.4.3, 1.4.11).
"""
import argparse
import json
import sys


def parse_hex(h: str) -> tuple[float, float, float]:
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) == 8:  # AARRGGBB (Flutter style) -> drop alpha
        h = h[2:]
    if len(h) != 6:
        raise ValueError(f"bad colour: {h!r}")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def luminance(rgb) -> float:
    def lin(c):
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg: str, bg: str) -> float:
    l1, l2 = sorted((luminance(parse_hex(fg)), luminance(parse_hex(bg))), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pairs", nargs="*", help="FG:BG[:label]")
    ap.add_argument("--json", help="file with a list of {fg,bg,label,large}")
    ap.add_argument("--large", action="store_true", help="treat CLI pairs as large text / UI (3:1)")
    a = ap.parse_args()

    items = []
    for p in a.pairs:
        parts = p.split(":")
        if len(parts) < 2:
            ap.error(f"expected FG:BG[:label], got {p!r}")
        items.append({"fg": parts[0], "bg": parts[1], "label": ":".join(parts[2:]) or f"{parts[0]} on {parts[1]}", "large": a.large})
    if a.json:
        with open(a.json) as f:
            items.extend(json.load(f))
    if not items:
        ap.error("no pairs given")

    failed = 0
    print(f"{'pair':<34} {'ratio':>7}  need  result")
    for it in items:
        need = 3.0 if it.get("large") else 4.5
        r = ratio(it["fg"], it["bg"])
        ok = r >= need
        failed += not ok
        print(f"{it.get('label', ''):<34} {r:>6.2f}:1  {need:>3}  {'PASS' if ok else 'FAIL'}")
    print(f"\n{len(items) - failed}/{len(items)} pass")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
