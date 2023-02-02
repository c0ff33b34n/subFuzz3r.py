# c0ff33b34n
# Basic URL fetcher

import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_urls(url):
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not fetch URLs from {url}: {e}")
        return []
    if response.status_code != 200:
        print(f"Error: Could not fetch URLs from {url} (HTTP status code {response.status_code})")
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    links = [link.get("href") for link in soup.find_all("a")]
    filtered_links = []
    for link in links:
        if link is not None:
            parsed_link = urlparse(link)
            if parsed_link.scheme and parsed_link.netloc:
                filtered_links.append(link)
    return filtered_links

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch URLs from websites")
    parser.add_argument("-u", "--url", action="append", dest="sources",
                        help="URL of a website to fetch URLs from")
    args = parser.parse_args()
    sources = args.sources or []
    if not sources:
        print("Error: No source URL specified. Use the -u option to specify a source.")
        exit(1)
    urls = []
    for source in sources:
        urls.extend(get_urls(source))
    for link in urls:
        print(link)
