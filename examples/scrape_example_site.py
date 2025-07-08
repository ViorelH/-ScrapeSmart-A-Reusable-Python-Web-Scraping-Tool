from scrapesmart.scraper import ScrapeSmart

def run_scraper():
    url = "https://example.com"
    '''
    write any URL
    '''
    scraper = ScrapeSmart(url)

    print("Fetching text content...")

    print(scraper.get_text()[:500])

    print("
Found links:")
    print(scraper.get_links())

    print("
Found images:")
    print(scraper.get_images())

if __name__ == "__main__":
    run_scraper()
