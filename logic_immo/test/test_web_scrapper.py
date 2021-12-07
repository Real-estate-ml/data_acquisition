from src.web_scrapper import WebScrapper
from bs4 import BeautifulSoup

def test_get_page_number():
    web_scrapper = WebScrapper("base_url")
    f = open("test/html_test/home_page.html", "r")
    home_page = BeautifulSoup(f.read(), "html.parser")
    f.close()
    expected_pages_number = 3326
    web_scrapper.set_last_page_number(home_page)
    assert web_scrapper.nb_pages == expected_pages_number

def test_get_all_links_for_page():
    web_scrapper = WebScrapper("base_url")
    f = open("test/html_test/home_page.html", "r")
    home_page = BeautifulSoup(f.read(), "html.parser")
    f.close()
    expected_found_links = 21
    found_links = web_scrapper.get_all_links_for_page(home_page)
    assert len(found_links) == expected_found_links