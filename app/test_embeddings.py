from langchain_ollama import OllamaEmbeddings


embeddings = OllamaEmbeddings(
    model="nomic-embed-text:latest",
    base_url="http://localhost:11434",
)


vector = embeddings.embed_query(
    "What is this website about?"
)


print("Embedding dimensions:", len(vector))
print("First 5 values:", vector[:5])