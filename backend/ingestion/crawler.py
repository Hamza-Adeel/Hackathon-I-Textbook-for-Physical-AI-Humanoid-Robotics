import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_all_doc_urls(base_url: str) -> list[str]:
    """
    Fetches all documentation URLs from a Docusaurus website.
    It first tries to find a sitemap, and falls back to crawling the homepage.
    Ensures all returned URLs have the same base domain as the base_url argument.
    """
    parsed_base_url = urlparse(base_url)
    base_domain = f"{parsed_base_url.scheme}://{parsed_base_url.netloc}"
    
    sitemap_url = urljoin(base_url, "sitemap.xml")
    found_urls = set()

    try:
        response = requests.get(sitemap_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "xml")
            for loc in soup.find_all("loc"):
                sitemap_loc_url = loc.text
                # Normalize URL to use the desired base domain
                if urlparse(sitemap_loc_url).path.startswith("/docs/"):
                    normalized_url = urljoin(base_domain, urlparse(sitemap_loc_url).path)
                    found_urls.add(normalized_url)
            if found_urls:
                return list(found_urls)
    except requests.RequestException:
        pass  # Sitemap not found or failed to fetch, proceed to crawl

    # Fallback to crawling the homepage
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            full_url = urljoin(base_url, href)
            if urlparse(full_url).path.startswith("/docs/"):
                normalized_url = urljoin(base_domain, urlparse(full_url).path)
                found_urls.add(normalized_url)
        return list(found_urls)
    except requests.RequestException as e:
        print(f"Error crawling homepage: {e}")
        return []

if __name__ == "__main__":
    # Example usage
    test_url = "https://hackathon-i-textbook-for-physical-a.vercel.app/"
    doc_urls = get_all_doc_urls(test_url)
    print(f"Found {len(doc_urls)} documentation URLs:")
    for url in doc_urls:
        print(url)