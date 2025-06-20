
def generate_report(model, question, findings):
    report_prompt = f"""\nFor the following research question: {question}, please generate a scientific report based on the following findings:

{findings}
Please ensure the report is structured with an introduction, methods, results, and discussion sections. The report should be concise, scientifically rigorous, and suitable for publication in a peer-reviewed journal.
For the methods section, please include a brief description of how the papers were selected and analyzed, using a LangChain-based approach to generate search terms and gather relevant papers from Semantic Scholar, and then screen and analyze those papers.
"""
    response = model.invoke(report_prompt)
    return response.content
