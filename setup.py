from setuptools import setup, find_packages

setup(
    name="scrapesmart",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests", "beautifulsoup4"],
    author="Your Name",
    description="A reusable Python web scraping tool",
    keywords=["web scraping", "python", "beautifulsoup", "requests"]
)
