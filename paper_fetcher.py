
import requests

def get_papers(query, limit=5):
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": query,
        "limit": limit,
        "fields": "title,authors,year,url,abstract,openAccessPdf"
    }
    headers = {"x-api-key": "98w2jxk0Aa6zIXkD7153V8WrUTqdF8vD4zbFcgXo"}
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
