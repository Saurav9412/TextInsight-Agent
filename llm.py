from langchain_google_genai import ChatGoogleGenerativeAI
from functools import lru_cache
from settings import settings
from dotenv import load_dotenv
import os

load_dotenv()

@lru_cache(maxsize=1)
def build_llm():
    return ChatGoogleGenerativeAI(
        api_key = settings.gemini_api_key.get_secret_value(),
        model = settings.llm_model,
        timeout = settings.llm_timeout_seconds
    )
