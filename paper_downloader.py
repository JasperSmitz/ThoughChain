
import os
import requests
import fitz  # PyMuPDF

def download_and_extract_papers(screened_papers, folder="downloaded_papers"):
    os.makedirs(folder, exist_ok=True)
    downloaded = {}

    for title, (_, pdf_url) in screened_papers.items():
        if not pdf_url:
            print(f"No PDF available for '{title}'")
            continue

        try:
            filename = f"{title[:50].replace('/', '-')}.pdf"
            filepath = os.path.join(folder, filename)

            response = requests.get(pdf_url)
            with open(filepath, "wb") as f:
                f.write(response.content)

            doc = fitz.open(filepath)
            full_text = "".join([page.get_text() for page in doc])

            downloaded[title] = full_text
            print(f"Downloaded and extracted '{title}'")

        except Exception as e:
            print(f"Failed for '{title}': {e}")

    return downloaded
