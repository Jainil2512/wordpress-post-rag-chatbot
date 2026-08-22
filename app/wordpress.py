import requests

from .config import WORDPRESS_URL


def fetch_content(content_type):
    """Fetch published WordPress content."""

    url = "{}/wp-json/wp/v2/{}".format(
        WORDPRESS_URL,
        content_type,
    )

    response = requests.get(
        url,
        params={
            "per_page": 100,
            "status": "publish",
        },
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


def fetch_posts():
    return fetch_content("posts")


def fetch_pages():
    return fetch_content("pages")


def fetch_all():
    return fetch_posts() + fetch_pages()