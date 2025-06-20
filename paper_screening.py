
def screen_papers(model, question, all_papers):
    found_papers = {}
    for query, papers in all_papers.items():
        for paper in papers:
            title = paper.get("title", "No title")
            abstract = paper.get("abstract", "No abstract")
            pdf_url = paper.get("openAccessPdf", {}).get("url", None)
            found_papers[title] = (abstract, pdf_url)

    paper_entries = "\n".join(
        [f"- {title}:\n  {abstract}" for title, (abstract, _) in found_papers.items()]
    )

    screening_prompt = f"""\nFor the following research question: {question}, please review the search results and select the most relevant papers.
Each entry includes a title and its abstract. Based on relevance to the question, return a list of only the titles of relevant papers, separated by semicolons, without any additional text.

Papers:
{paper_entries}
"""
    response = model.invoke(screening_prompt)
    screened_titles = [t.strip() for t in response.content.split(";")]
    return {title: found_papers[title] for title in screened_titles if title in found_papers}
