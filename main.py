
from models import get_model
from query_generator import generate_queries
from paper_fetcher import fetch_all_papers
from paper_screening import screen_papers
from paper_downloader import download_and_extract_papers
from paper_analyzer import analyze_papers
from report_generator import generate_report

def main():
    model = get_model()
    question = input("Enter your research question: ")

    print("\n[1] Generating search queries...")
    search_queries = generate_queries(model, question)

    print("\n[2] Fetching papers from Semantic Scholar...")
    all_papers = fetch_all_papers(search_queries)

    print("\n[3] Screening relevant papers...")
    screened_papers = screen_papers(model, question, all_papers)

    print("\n[4] Downloading and extracting PDFs...")
    downloaded_papers = download_and_extract_papers(screened_papers)

    print("\n[5] Analyzing paper content...")
    findings = analyze_papers(model, question, downloaded_papers)

    print("\n[6] Generating final report...")
    report = generate_report(model, question, findings)

    print("\n\nGenerated Report:")
    print(report)

if __name__ == "__main__":
    main()
