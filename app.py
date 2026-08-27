"""
Global AI Adoption in Education - Web Integration of Dashboard and Story
--------------------------------------------------------------------------
A lightweight Flask app that embeds Tableau Dashboards and Stories so
users can explore the "AI Adoption in Education" insights directly in
a browser, without opening Tableau separately.

Run:
    pip install flask
    python app.py

Then open: http://127.0.0.1:5000
"""

from flask import Flask, render_template

app = Flask(__name__)

# ---------------------------------------------------------------------
# Update these with your own published Tableau Public / Server URLs.
# Format for Tableau Public:
#   https://public.tableau.com/views/<WorkbookName>/<ViewName>
# ---------------------------------------------------------------------

TABLEAU_DASHBOARD_URL = "https://public.tableau.com/views/GLOBALAIADOPTIONINEDUCATION/Dashboard2"
TABLEAU_DASHBOARD2_URL = "https://public.tableau.com/views/GLOBALAIADOPTIONINEDUCATION/Dashboard3"
TABLEAU_STORY_URL = "https://public.tableau.com/views/GLOBALAIADOPTIONINEDUCATION/Story1"
TABLEAU_STORY2_URL = "https://public.tableau.com/views/GLOBALAIADOPTIONINEDUCATION/Story2"


@app.route("/")
def home():
    """Landing page - matches the project cover ('View Data Insights')."""
    return render_template("home.html")


@app.route("/dashboard")
def dashboard():
    """Embedded interactive Tableau Dashboard."""
    return render_template("dashboard.html", viz_url=TABLEAU_DASHBOARD_URL)
@app.route("/dashboard2")
def dashboard2():
    """Second interactive Tableau Dashboard."""
    return render_template("dashboard2.html", viz_url=TABLEAU_DASHBOARD2_URL)

@app.route("/story2")
def story2():
    """Second interactive Tableau Story."""
    return render_template("story2.html", viz_url=TABLEAU_STORY2_URL)


@app.route("/story")
def story():
    """Embedded interactive Tableau Story."""
    return render_template("story.html", viz_url=TABLEAU_STORY_URL)


@app.route("/about")
def about():
    """Optional: short project description page."""
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
