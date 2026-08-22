from app.wordpress import fetch_posts
from app.documents import wordpress_to_documents
from app.chunking import chunk_documents


def main():
    print("Fetching WordPress posts...")

    posts = fetch_posts()

    print("Posts:", len(posts))

    print("\nConverting posts to LangChain documents...")

    documents = wordpress_to_documents(posts)

    print("Documents:", len(documents))

    print("\nCreating chunks...")

    chunks = chunk_documents(documents)

    print("Total chunks:", len(chunks))

    for index, chunk in enumerate(chunks, start=1):
        print("\n" + "=" * 70)
        print("CHUNK:", index)
        print("=" * 70)

        print("WordPress ID:", chunk.metadata["wordpress_id"])
        print("Title:", chunk.metadata["title"])
        print("URL:", chunk.metadata["url"])

        print("\nCharacters:", len(chunk.page_content))

        print("\nContent:")
        print(chunk.page_content[:800])


if __name__ == "__main__":
    main()