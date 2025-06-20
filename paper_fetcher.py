
import os
import requests
import getpass

def get_papers(query, limit=5):
    if not os.environ.get("SEMANTIC_SCHOLAR_API_KEY"):
        os.environ["SEMANTIC_SCHOLAR_API_KEY"] = getpass.getpass(
            "Enter API key for Semantic Scholar: "
        )
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": query,
        "limit": limit,
        "fields": "title,authors,year,url,abstract,openAccessPdf"
    }
    headers = {"x-api-key": os.environ["SEMANTIC_SCHOLAR_API_KEY"]}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print(f"Error fetching for '{query}':", response.status_code, response.text)
        return []

def fetch_all_papers(search_queries):
    all_papers = {}
    for query in search_queries:
        papers = get_papers(query)
        all_papers[query] = papers
    return all_papers
