import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_papers(query, limit=5):
    if not os.environ.get("SEMANTIC_SCHOLAR_API_KEY"):
        raise ValueError("SEMANTIC_SCHOLAR_API_KEY not set in environment.")

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
