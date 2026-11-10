# Karthik Sai S - Portfolio

FastAPI + Jinja2 portfolio. All content lives in `data.py`; edit it and redeploy.

## Run locally
    pip install -r requirements.txt
    uvicorn main:app --reload
Open http://localhost:8000

## Deploy for free (recommended: GitHub Pages, always on, no cold starts)
The portfolio is exported to plain static files, so it loads instantly and never sleeps.
1. Create a **public** GitHub repo (for a clean URL, name it `<username>.github.io`, or use any name like `portfolio`).
2. Push this folder to it (branch `main`).
3. In the repo: Settings > Pages > Source: **GitHub Actions**.
4. Every push now rebuilds and publishes the site (see `.github/workflows/pages.yml`).
Your site: `https://<username>.github.io/` (or `/<repo-name>/`).
5. Put that URL in `SITE_URL` in `data.py` so LinkedIn/WhatsApp show the preview card.

Alternatives: Cloudflare Pages or Netlify. Build command `pip install -r requirements.txt && python build.py`, publish directory `dist`.

## Build the static site locally
    python build.py      # output in ./dist
    python -m http.server -d dist 8000

## Optional: run as a live FastAPI app (Render free tier sleeps after ~15 min idle)
`render.yaml` is included. Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`.

## Endpoints (FastAPI mode only)
/ (site) · /api/profile (JSON) · /api/docs (Swagger) · /health

To add project demo images, see ADD_DEMO_IMAGES.md
