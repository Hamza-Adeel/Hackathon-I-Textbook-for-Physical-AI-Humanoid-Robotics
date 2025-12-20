import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_urls_from_sitemap(sitemap_url: str) -> list[str]:
    """
    Fetches and parses a sitemap to extract all URLs.
    """
    urls = []
    logging.info(f"Fetching sitemap from {sitemap_url}")
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "xml")
        locs = soup.find_all("loc")
        urls = [loc.text for loc in locs]
        logging.info(f"Found {len(urls)} URLs in sitemap.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching sitemap: {e}")
    return urls

def crawl_homepage(base_url: str) -> list[str]:
    """
    Crawls the homepage to find links.
    """
    urls = []
    logging.info(f"Crawling homepage at {base_url}")
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            url = urljoin(base_url, href)
            urls.append(url)
        logging.info(f"Found {len(urls)} links on homepage.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error crawling homepage: {e}")
    return urls

def get_all_documentation_urls(start_url: str) -> list[str]:
    """
    Gets all documentation URLs from a Docusaurus website.
    """
    sitemap_url = urljoin(start_url, "sitemap.xml")
    urls = get_urls_from_sitemap(sitemap_url)

    if not urls:
        logging.warning("Sitemap not found or empty, falling back to homepage crawl.")
        urls = crawl_homepage(start_url)

    # Fix incorrect URLs from sitemap
    corrected_urls = []
    for url in urls:
        path = urlparse(url).path
        corrected_urls.append(urljoin(start_url, path))

    doc_urls = [
        url for url in corrected_urls
        if urlparse(url).path.startswith("/docs/")
    ]
    
    # Also add the base url to the list of urls to crawl
    if start_url not in doc_urls:
        doc_urls.append(start_url)

    unique_urls = list(set(doc_urls))
    logging.info(f"Found {len(unique_urls)} unique documentation URLs.")
    return unique_urls

if __name__ == "__main__":
    # Example usage:
    # This should be a docusaurus site, e.g., "https://hackathon-i-textbook-for-physical-a.vercel.app/"
    test_url = "https://hackathon-i-textbook-for-physical-a.vercel.app/"
    all_urls = get_all_documentation_urls(test_url)
    logging.info(f"Found {len(all_urls)} documentation URLs:")
    for url in all_urls:
        print(url)
