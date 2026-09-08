#!/usr/bin/env python3
"""Regenerate sitemap.xml from the HTML files in the repository root.

A page is listed unless it opts out, so a new page is picked up simply by
existing. A page opts out by carrying a noindex robots meta tag, which is
what a half finished page should have until its content is ready.

lastmod comes from the file's last commit date, so it stays honest without
anyone having to remember to touch it.
"""

import glob
import os
import re
import subprocess
import sys
from datetime import date

BASE = "https://ironbarkadvisory.ae"

# Anything not named here gets DEFAULT_PRIORITY. Priority is a weak hint to
# crawlers about relative importance within the site, nothing more.
PRIORITY = {
    "index.html": "1.0",
    "students-families.html": "0.9",
    "institutions.html": "0.9",
    "why-australia.html": "0.8",
    "about.html": "0.7",
    "contact.html": "0.7",
}
CITY_PRIORITY = "0.6"
DEFAULT_PRIORITY = "0.5"

# Never listed, whatever their meta tags say.
ALWAYS_SKIP = {"404.html"}

NOINDEX = re.compile(
    r'<meta\s+name=["\']robots["\']\s+content=["\'][^"\']*\bnoindex\b', re.I
)


def last_modified(path):
    """Date of the last commit that touched this file, or today if unknown."""
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", path],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
        if out:
            return out
    except (subprocess.CalledProcessError, OSError):
        pass
    return date.today().isoformat()


def priority_for(name):
    if name in PRIORITY:
        return PRIORITY[name]
    if name.startswith("why-australia-"):
        return CITY_PRIORITY
    return DEFAULT_PRIORITY


def loc_for(name):
    return BASE + "/" if name == "index.html" else "%s/%s" % (BASE, name)


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)

    entries, skipped = [], []
    for name in sorted(glob.glob("*.html")):
        if name in ALWAYS_SKIP:
            skipped.append((name, "always skipped"))
            continue
        with open(name, encoding="utf-8") as fh:
            if NOINDEX.search(fh.read()):
                skipped.append((name, "noindex"))
                continue
        entries.append(name)

    # Most important first, then alphabetical, so the file reads sensibly and
    # the diff stays small when a page is added.
    entries.sort(key=lambda n: (-float(priority_for(n)), n))

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for name in entries:
        lines += [
            "  <url>",
            "    <loc>%s</loc>" % loc_for(name),
            "    <lastmod>%s</lastmod>" % last_modified(name),
            "    <priority>%s</priority>" % priority_for(name),
            "  </url>",
        ]
    lines.append("</urlset>")
    new = "\n".join(lines) + "\n"

    old = ""
    if os.path.exists("sitemap.xml"):
        with open("sitemap.xml", encoding="utf-8") as fh:
            old = fh.read()

    for name, why in skipped:
        print("skipped %s (%s)" % (name, why))
    print("listed %d page(s)" % len(entries))

    if new == old:
        print("sitemap.xml already up to date")
        return 0
    with open("sitemap.xml", "w", encoding="utf-8") as fh:
        fh.write(new)
    print("sitemap.xml rewritten")
    return 0


if __name__ == "__main__":
    sys.exit(main())
