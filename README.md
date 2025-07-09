# ThoughtChain

ThoughtChain is an AI-powered assistant that builds a short literature review for a given research question. It queries Semantic Scholar, downloads open access papers, screens them with a language model and returns a concise scientific report. A small Flask web interface is also provided.

## Installation

1. Install **Python 3.8** or newer.
2. Install dependencies:

```bash
pip install -r requirements.txt
# additional packages for the web app
pip install flask flask-cors python-dotenv
```

## Configuration

Create a `.env` file in the project root and add your API keys:

```
OPENAI_API_KEY=your-openai-key
SEMANTIC_SCHOLAR_API_KEY=your-semantic-scholar-key
```

The application loads this file automatically. Keep the `.env` file private and never commit it to version control.

## Usage

### Command line example

You can call the pipeline directly from Python:

```bash
python - <<'PY'
from main import run_pipeline
result = run_pipeline("What is the role of epigenetics in Alzheimer's disease?")
print(result["report"])
PY
```

### Web interface

To start the Flask interface run:

```bash
python app.py
```

Open `http://127.0.0.1:5000/` in your browser and enter a research question. The page will display each step of the pipeline and the generated report.

## Further Development

Want to build on this project? Here are a few ideas:

- **Add PDF parsing**: Allow users to upload their own papers and extract insights.
- **Add Long Term Storage**: Allow users to upload their own papers and extract insights.
- **Citation Generator**: Export results in APA/MLA/BibTeX format.
- **LLM Model Swapping**: Use Anthropic Claude, Mistral, or open models like LLaMA via HuggingFace. You could even train models for each specific module.
- **Multi-language Support**: Let users input questions in other languages.
- **User Accounts**: Save searches and generated reports to a personal dashboard.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

