from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

from app.config import (
    CHROMA_PATH,
    EMBEDDING_MODEL,
    OLLAMA_BASE_URL,
)


COLLECTION_NAME = "wordpress_rag"


def get_embeddings():
    return OllamaEmbeddings(
        model=EMBEDDING_MODEL,
        base_url=OLLAMA_BASE_URL,
    )


def create_vector_store(documents):
    embeddings = get_embeddings()

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=CHROMA_PATH,
        collection_name=COLLECTION_NAME,
    )

    return vector_store


def get_vector_store():
    embeddings = get_embeddings()

    vector_store = Chroma(
        persist_directory=CHROMA_PATH,
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
    )

    return vector_store