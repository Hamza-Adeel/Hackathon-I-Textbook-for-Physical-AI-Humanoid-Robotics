import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_chapter_and_lesson(url: str) -> tuple[str, str]:
    """
    Extracts chapter and lesson from a URL path.
    e.g., /docs/ros-2/understanding-nodes -> ('ros-2', 'understanding-nodes')
    """
    path_parts = urlparse(url).path.strip('/').split('/')
    if len(path_parts) >= 3 and path_parts[0] == 'docs':
        return path_parts[1], path_parts[-1]
    return None, None


def parse_article_content(url: str) -> tuple[str, str, str, str]:
    """
    Fetches a URL and parses the content of the <article> tag.
    Returns the cleaned text, source URL, chapter, and lesson.
    """
    logging.info(f"Parsing content from {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        article = soup.find("article")

        if not article:
            logging.warning(f"No <article> tag found on {url}")
            return None, None, None, None

        # Clean the text
        text = article.get_text(separator=" ", strip=True)
        logging.info(f"Extracted {len(text)} characters from {url}")
        
        # Get metadata from URL
        chapter, lesson = get_chapter_and_lesson(url)

        return text, url, chapter, lesson

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching page content for {url}: {e}")
        return None, None, None, None


if __name__ == '__main__':
    # Example usage:
    test_url = "https://hackathon-i-textbook-for-physical-a.vercel.app/docs/ros-2/understanding-nodes-topics-services"
    text, source_url, chapter, lesson = parse_article_content(test_url)

    if text:
        logging.info(f"URL: {source_url}")
        logging.info(f"Chapter: {chapter}")
        logging.info(f"Lesson: {lesson}")
        logging.info("\nCleaned Text:")
        print(text[:500] + "...")
