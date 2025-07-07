import unittest
from scrapesmart.scraper import ScrapeSmart

class TestScrapeSmart(unittest.TestCase):
    def setUp(self):
        self.scraper = ScrapeSmart("https://example.com")
        self.scraper.fetch()

    def test_fetch_text(self):
        text = self.scraper.get_text()
        self.assertTrue(len(text) > 0)

    def test_fetch_links(self):
        links = self.scraper.get_links()
        self.assertIsInstance(links, list)

    def test_fetch_images(self):
        images = self.scraper.get_images()
        self.assertIsInstance(images, list)

if __name__ == "__main__":
    unittest.main()
