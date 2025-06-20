# ThoughtChain

ThoughtChain is a command-line tool that builds a concise literature review using Semantic Scholar and a language model. It generates search queries, downloads relevant papers, analyzes them and produces a report.

## Setup

1. Install Python 3.8 or newer.
2. Install the required packages:

```bash
pip install langchain requests PyMuPDF
```

3. Provide API keys for OpenAI and Semantic Scholar. You can set them as environment variables:

```bash
export OPENAI_API_KEY=your-openai-key
export SEMANTIC_SCHOLAR_API_KEY=your-semanticscholar-key
```

If the variables are not set, the program will prompt for the keys when run.

## Usage

Run the main script and follow the prompts:

```bash
python main.py
```

Enter your research question when asked. The program will fetch papers, analyze them and print the generated report.
