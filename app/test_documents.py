from app.wordpress import fetch_posts
from app.documents import wordpress_to_documents


posts = fetch_posts()

documents = wordpress_to_documents(posts)

print("WordPress posts:", len(posts))
print("LangChain documents:", len(documents))

for document in documents:
    print("\n---")
    print("Title:", document.metadata["title"])
    print("URL:", document.metadata["url"])
    print("ID:", document.metadata["wordpress_id"])
    print("Content:")
    print(document.page_content[:300])