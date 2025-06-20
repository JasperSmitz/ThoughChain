
import getpass
import os
from langchain.chat_models import init_chat_model

def get_model():
    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")
    return init_chat_model("gpt-4o-mini", model_provider="openai")
