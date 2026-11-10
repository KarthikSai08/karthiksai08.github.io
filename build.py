"""Export the FastAPI site to plain static files in ./dist (for free, always-on hosting).

Usage:  python build.py
Then host the ./dist folder on GitHub Pages, Cloudflare Pages or Netlify.
"""
import shutil
from pathlib import Path

from fastapi.testclient import TestClient

import main

main.STATIC_MODE = True
OUT = Path(__file__).parent / "dist"
if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()

html = TestClient(main.app).get("/").text
# relative asset paths so the site works from any sub-path (e.g. username.github.io/portfolio/)
html = html.replace('"/static/', '"static/')
(OUT / "index.html").write_text(html, encoding="utf-8")
shutil.copytree(Path(__file__).parent / "static", OUT / "static")
for keep in OUT.rglob(".gitkeep"):
    keep.unlink()
(OUT / ".nojekyll").touch()
print("Built static site in", OUT)
