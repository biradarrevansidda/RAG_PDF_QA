import os
from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()


def get_llm():
    groq_api_key = os.getenv("GROQ_API_KEY")

    if not groq_api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. "
            "Add your Groq API key to the .env file."
        )

    return ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0,
        api_key=groq_api_key,
        max_tokens=500
    )