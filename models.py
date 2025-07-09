import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()  # Load .env variables

def get_model():
    if not os.environ.get("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY not set in environment.")
    return init_chat_model("gpt-4o-mini", model_provider="openai")