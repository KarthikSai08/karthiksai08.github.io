# How to add demo images to your projects

Every project card shows a "Demo coming soon" placeholder until you add images.
It takes two steps and no HTML editing.

## 1. Drop your images in the project's folder

Each project has its own folder inside `static/projects/`:

| Project                              | Folder                            |
|--------------------------------------|-----------------------------------|
| ATMS traffic violation detection     | `static/projects/atms/`           |
| Enterprise Text-to-SQL assistant     | `static/projects/text-to-sql/`    |
| Email classification and routing     | `static/projects/email-routing/`  |
| Supplier ranking advisor             | `static/projects/supplier-ranking/` |
| Read-only AI support chatbot         | `static/projects/support-chatbot/` |

Example: `static/projects/atms/detection.png`

## 2. List the file names in `data.py`

Find the project in `data.py` and put the file names in its `images` list.
Use only the file name, not the folder path:

```python
"slug": "atms",
...
"demo": None,
"images": ["detection.png", "dashboard.png", "violations.png"],
```

Save, redeploy, done. The placeholder is replaced by a swipeable image strip.
Clicking an image opens it full size in a new tab.

## Optional: add a live demo link

```python
"demo": "https://your-demo-url.com",
```

A "Live demo" link then appears next to "Code on GitHub".

## Image tips

- Use 16:9 images (for example 1600x900). Other ratios are cropped to fit.
- Use PNG for screenshots and JPG or WebP for photos. Keep each file under 500 KB.
  Free tools: squoosh.app or tinypng.com.
- Use short lowercase names without spaces: `dashboard.png`, not `My Dashboard (1).png`.
- A short screen recording works better than a screenshot for AI demos.
  Convert it to a GIF or WebP, or upload it to YouTube and use the link as `demo`.
- Blur or remove private data (real emails, customer names, API keys, IP addresses)
  before adding any screenshot, especially from work projects.

## Add a new project

Copy any project block in `data.py`, change the text, give it a unique `slug`,
and create a folder `static/projects/<slug>/`. Card colors rotate automatically.
