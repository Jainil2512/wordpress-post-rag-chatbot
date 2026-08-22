import os

from dotenv import load_dotenv


load_dotenv()


WORDPRESS_URL = os.getenv(
    "WORDPRESS_URL"
).rstrip("/")

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434",
)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "nomic-embed-text:latest",
)

LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "llama3.2:3b",
)

LLM_TEMPERATURE = float(
    os.getenv("LLM_TEMPERATURE", "0.0")
)

CHROMA_PATH = os.getenv(
    "CHROMA_PATH",
    "./data/chroma",
)

CHUNK_SIZE = int(
    os.getenv("CHUNK_SIZE", "800")
)

CHUNK_OVERLAP = int(
    os.getenv("CHUNK_OVERLAP", "120")
)

TOP_K = int(
    os.getenv("TOP_K", "5")
)