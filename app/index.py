from app.wordpress import fetch_posts
from app.documents import wordpress_to_documents
from app.chunking import chunk_documents
from app.vector_store import create_vector_store


def main():

    print("=" * 60)
    print("WORDPRESS RAG INDEXER")
    print("=" * 60)

    # --------------------------------------------------
    # 1. Fetch WordPress content
    # --------------------------------------------------

    print("\n[1/4] Fetching WordPress posts...")

    posts = fetch_posts()

    print("Posts fetched:", len(posts))

    # --------------------------------------------------
    # 2. Convert to LangChain documents
    # --------------------------------------------------

    print("\n[2/4] Creating LangChain documents...")

    documents = wordpress_to_documents(posts)

    print("Documents created:", len(documents))

    # --------------------------------------------------
    # 3. Chunk documents
    # --------------------------------------------------

    print("\n[3/4] Creating chunks...")

    chunks = chunk_documents(documents)

    print("Chunks created:", len(chunks))

    # --------------------------------------------------
    # 4. Create Chroma vector database
    # --------------------------------------------------

    print("\n[4/4] Creating ChromaDB vector store...")

    create_vector_store(chunks)

    print("\n" + "=" * 60)
    print("INDEXING COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()