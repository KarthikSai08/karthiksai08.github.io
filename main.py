from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import data

BASE = Path(__file__).parent
STATIC_MODE = False  # build.py flips this when exporting the static site
app = FastAPI(title="Karthik Sai S - Portfolio", docs_url="/api/docs", redoc_url=None)
app.mount("/static", StaticFiles(directory=BASE / "static"), name="static")
templates = Jinja2Templates(directory=BASE / "templates")
ASSET_V = int(max(f.stat().st_mtime for f in (BASE / "static").glob("*.*")))


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "v": ASSET_V,
            "site_url": data.SITE_URL.rstrip("/"),
            "why": data.WHY,
            "static_mode": STATIC_MODE,
            "p": data.PROFILE,
            "stats": data.STATS,
            "projects": data.PROJECTS,
            "skills": data.SKILLS,
            "experience": data.EXPERIENCE,
            "education": data.EDUCATION,
            "publication": data.PUBLICATION,
        },
    )


@app.get("/api/profile")
async def profile():
    return {
        "profile": data.PROFILE,
        "projects": data.PROJECTS,
        "skills": dict(data.SKILLS),
        "experience": data.EXPERIENCE,
    }


@app.get("/health")
async def health():
    return {"status": "ok"}
