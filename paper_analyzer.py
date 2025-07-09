
def analyze_papers(model, question, downloaded_papers):
    papers_to_analyze = "\n".join(
        [f"- Title of the paper: {title}\n  {full_text}" for title, full_text in downloaded_papers.items()]
    )

    analysis_prompt = f"""\nFor the following research question: {question}, please review the following papers and extract any useful information in regards to the question.

Each paper includes a title, author and its text. Based on the content, return a list of key findings, insights, or conclusions that directly address the research question.

Papers:
{papers_to_analyze}
"""
    response = model.invoke(analysis_prompt)
    return response.content
