
from models import get_model
from query_generator import generate_queries
from paper_fetcher import fetch_all_papers
from paper_screening import screen_papers
from paper_downloader import download_and_extract_papers
from paper_analyzer import analyze_papers
from report_generator import generate_report

def run_pipeline(question: str) -> dict:
    model = get_model()
    search_queries = generate_queries(model, question)
    all_papers = fetch_all_papers(search_queries)

    found_titles = []
    for papers in all_papers.values():
        for paper in papers:
            if "title" in paper:
                found_titles.append(paper["title"])

    screened_papers = screen_papers(model, question, all_papers)
    screened_titles = list(screened_papers.keys())

    downloaded_papers = download_and_extract_papers(screened_papers)
    findings = analyze_papers(model, question, downloaded_papers)
    report = generate_report(model, question, findings)

    return {
        "queries": search_queries,
        "found_papers": found_titles,
        "screened_papers": screened_titles,
        "findings": findings,
        "report": report
    }



# if __name__ == "__main__":
#     main()
