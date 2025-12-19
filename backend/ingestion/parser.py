import requests
from bs4 import BeautifulSoup, Tag

def get_article_content(url: str) -> Tag | None:
    """
    Fetches a URL and returns the BeautifulSoup Tag for the <article> element.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        article = soup.find("article")
        if not article:
            print(f"No <article> tag found at {url}")
            return None

        # Remove unnecessary elements
        for element in article.find_all(["nav", "footer", "aside"]):
            element.decompose()
        
        return article

    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    test_url = "https://hackathon-i-textbook-for-physical-a.vercel.app/docs/ros-2/understanding-nodes-topics-services"
    article_tag = get_article_content(test_url)
    if article_tag:
        print(f"Successfully extracted <article> content from {test_url}:")
        print(article_tag.get_text(strip=True)[:500] + "...")