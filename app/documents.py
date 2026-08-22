from bs4 import BeautifulSoup
from langchain_core.documents import Document


def wordpress_to_documents(posts):
    documents = []

    for post in posts:
        title = post["title"]["rendered"]
        html_content = post["content"]["rendered"]
        url = post["link"]
        wordpress_id = post["id"]

        soup = BeautifulSoup(
            html_content,
            "html.parser",
        )

        text = soup.get_text(
            separator="\n",
            strip=True,
        )

        full_text = "{}\n\n{}".format(
            title,
            text,
        )

        document = Document(
            page_content=full_text,
            metadata={
                "wordpress_id": wordpress_id,
                "title": title,
                "url": url,
                "content_type": "post",
            },
        )

        documents.append(document)

    return documents