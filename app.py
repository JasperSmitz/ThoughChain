from flask import Flask, render_template, request, jsonify, session
from models import get_model
from query_generator import generate_queries
from paper_fetcher import fetch_all_papers
from paper_screening import screen_papers
from paper_downloader import download_and_extract_papers
from paper_analyzer import analyze_papers
from report_generator import generate_report

from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "replace-this-secret-key"
CORS(app)

shared_state = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start-search", methods=["POST"])
def start_search():
    question = request.json.get("query", "")
    if not question:
        return jsonify(error="Empty query"), 400
    model = get_model()
    shared_state["question"] = question
    shared_state["model"] = model
    return jsonify(status="ok")

@app.route("/step/queries")
def step_queries():
    model = shared_state["model"]
    question = shared_state["question"]
    queries = generate_queries(model, question)
    shared_state["queries"] = queries
    return jsonify(queries=queries)

@app.route("/step/fetch")
def step_fetch():
    queries = shared_state["queries"]
    all_papers = fetch_all_papers(queries)
    found = []
    for papers in all_papers.values():
        for p in papers:
            if "title" in p:
                found.append(p["title"])
    shared_state["all_papers"] = all_papers
    shared_state["found_titles"] = found
    return jsonify(found_papers=found)

@app.route("/step/screen")
def step_screen():
    model = shared_state["model"]
    question = shared_state["question"]
    all_papers = shared_state["all_papers"]
    screened = screen_papers(model, question, all_papers)
    screened_titles = list(screened.keys())
    shared_state["screened_papers"] = screened
    shared_state["screened_titles"] = screened_titles
    return jsonify(screened_papers=screened_titles)

@app.route("/step/analyze")
def step_analyze():
    model = shared_state["model"]
    question = shared_state["question"]
    screened = shared_state["screened_papers"]
    downloaded = download_and_extract_papers(screened)
    findings = analyze_papers(model, question, downloaded)
    shared_state["findings"] = findings
    return jsonify(findings=findings)

@app.route("/step/report")
def step_report():
    model = shared_state["model"]
    question = shared_state["question"]
    findings = shared_state["findings"]
    report = generate_report(model, question, findings)
    return jsonify(report=report)

if __name__ == "__main__":
    app.run(debug=True)
