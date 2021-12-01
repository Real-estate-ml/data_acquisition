from src.web_scrapper import WebScrapper
from bs4 import BeautifulSoup

def test_get_page_number():
    web_scrapper = WebScrapper("base_url")
    f = open("test/html_test/home_page.html", "r")
    home_page = BeautifulSoup(f.read(), "html.parser")
    f.close()
    expected_pages_number = 3328
    actual_pages_number = web_scrapper.get_page_number(home_page)
    assert actual_pages_number == expected_pages_number