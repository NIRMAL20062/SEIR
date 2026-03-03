import sys
import requests
from bs4 import BeautifulSoup


def title(soup):
    if soup.title and soup.title.string:
        return soup.title.get_text(strip=True)
    return "No title found"

def body(soup):
    if soup.body:
        return soup.body.get_text(" ", strip=True)
    return "No body content found"

def links(soup):
    links = soup.find_all("a", href=True)
    if links:
        return [link["href"] for link in links]
    return []

if len(sys.argv) != 2:
    sys.exit(1)
url = sys.argv[1].strip()
if not url.startswith(("http://", "https://")):
    url = "https://" + url

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

print(title(soup))
print(body(soup))

links = links(soup)
if links:
    for link in links:
        print(link)
else:
    print("No links found")