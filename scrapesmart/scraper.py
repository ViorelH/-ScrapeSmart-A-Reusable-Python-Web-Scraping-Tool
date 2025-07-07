import requests
from bs4 import BeautifulSoup

class ScrapeSmart:
    def __init__(self, url):
        self.url = url
        self.soup = None

    def fetch(self):
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            self.soup = BeautifulSoup(response.content, "html.parser")
        except Exception as e:
            print(f"[!] Failed to fetch: {e}")

    def get_links(self):
        if not self.soup:
            self.fetch()
        return [a['href'] for a in self.soup.find_all('a', href=True)]

    def get_text(self):
        if not self.soup:
            self.fetch()
        return self.soup.get_text(strip=True)

    def get_images(self):
        if not self.soup:
            self.fetch()
        return [img['src'] for img in self.soup.find_all('img', src=True)]
