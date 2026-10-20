# Global AI Adoption in Education — Web Integration

Flask app that embeds a Tableau **Dashboard** and **Story** so users can explore
AI-adoption-in-education insights directly in a browser.

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open **http://127.0.0.1:5000**

## Connect your real Tableau views

1. Publish your workbook to **Tableau Public** (or Server/Online).
2. Open the Dashboard, click **Share**, copy the view URL — it looks like:
   `https://public.tableau.com/views/GLOBALAIADOPTIONINEDUCATION/Dashboard2"`
3. Paste it into `app.py`:
   ```python
   TABLEAU_DASHBOARD2_URL = "https://public.tableau.com/views/GLOBALAIADOPTIONINEDUCATION/Dashboard2"
TABLEAU_DASHBOARD3_URL = "https://public.tableau.com/views/GLOBALAIADOPTIONINEDUCATION/Dashboard3"
   TABLEAU_STORY1_URL = "https://public.tableau.com/views/GLOBALAIADOPTIONINEDUCATION/Story1" 
TABLEAU_STORY2_URL = "https://public.tableau.com/views/GLOBALAIADOPTIONINEDUCATION/Story2"
   ```
4. Restart the app — the `<tableau-viz>` component in `dashboard.html` / `story.html`
   will render your live, interactive visualization.

## Project structure

```
global-ai-adoption-app/
├── app.py                 # Flask routes
├── requirements.txt
├── templates/
│   ├── base.html           # shared layout + nav
│   ├── home.html            # landing page ("View Data Insights")
│   ├── dashboard.html        # embedded Tableau Dashboard
│   ├── story.html            # embedded Tableau Story
│   └── about.html            # project description
└── static/
    └── css/style.css        # styling
```

## Progress checklist (matches "Web Integration" subtask)

- [x] Flask app scaffolded with routes
- [x] Tableau Embedding API v3 wired into Dashboard page
- [x] Tableau Embedding API v3 wired into Story page
- [x] Nav + landing page styled to match project cover
- [ ] Swap in your real published Tableau view URLs
- [ ] Deploy (e.g. Render, PythonAnywhere, or Heroku) for a public link
