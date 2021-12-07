from bs4 import BeautifulSoup
import requests
from time import sleep

class WebScrapper():
    def __init__(self, url):
        self.url = url
        self.nb_pages = 0
        self.links = []
    
    def get_html_page(self, page_number):
        """Get the BeautifulSoup object of an HTML page
        If page_number is None, then just use the base url passed as parameter 
        when instantiating the class.
        If page_number is not None (0..n), then add /page=n to the url
        :param page_number: page number
        :type page_number: int
        :return: HTML object
        :rtype: BeautifulSoup
        """
        headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'}
        current_url = ""
        if page_number != None:
            current_url = self.url + "/page={}".format(str(page_number))
        else:
            current_url = self.url
        page = requests.get(current_url, headers=headers)
        html_soup = BeautifulSoup(page.text, "html.parser")
        return html_soup

    def get_page_number(self, home_page: BeautifulSoup)->int:
        """The aim of this function is to return the number of page from logic_immo website in order to get all the real-estate ads
        :param home_page: home page
        :type home_page: BeautifulSoup object
        :return: total number of pages
        :rtype: int
        """
        number = home_page.find("h1", {"class": "titleSearch"}).text
        numbers = [int(nbr) for nbr in number.split() if nbr.isdigit()]
        pages_number = int(numbers[0]/20)
        return pages_number

    def get_all_pages_links(self):
        """Get all the apartment ads links
        :return: total links of all pages
        :rtype: list
        """
        for i in range(0, self.get_page_number(self.url)):
            soup = BeautifulSoup(self.get_html_page(i).text, "html.parser")
            links = soup.find_all('a', {"class": "linkToFa"})
            for j in links:
                self.links.append(j['href'])
            sleep(1.1)
        return self.links

    def export_to_gcs(self):
        """Export the HTML to Google Cloud Storage
        """
        None



