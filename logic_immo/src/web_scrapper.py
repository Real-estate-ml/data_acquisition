from bs4 import BeautifulSoup
import requests
from time import sleep
from pathlib import Path
from datetime import date
from random import randint
from google.cloud import storage

class WebScrapper():
    def __init__(self, url):
        self.url = url
        self.nb_pages = 0
        self.links = []

    # def request_page(self, url):
    #     headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'}
    #     try:
    #         page = requests.get(url, headers=headers)
    #         return page
    #     except Exception as e:
    #         print(e)

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
        if page_number != None:
            current_url = self.url + "/page={}".format(str(page_number))
        else:
            current_url = self.url
        page = requests.get(current_url, headers=headers)
        html_soup = BeautifulSoup(page.text, "html.parser")
        return html_soup

    # Vérifier la validité de chaque page html
    # get data check si c'est valide si pas valide exception
    #def get_validity_html_page(html_page):

    def get_apartment_ad(self, link: str):
        """[summary]
        :param link: [description]
        :type link: str
        :return: [description]
        :rtype: [type]
        """
        sleep(randint(8, 14))
        headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'}
        page = requests.get(link, headers=headers)
        return page.text

    def set_last_page_number(self, home_page):
        """The aim of this function is to return the number of page from logic_immo website in order to get all the real-estate ads
        :param home_page: home page
        :type home_page: BeautifulSoup object
        """
        number = home_page.find("h1", {"class": "titleSearch"}).text
        numbers = [int(nbr) for nbr in number.split() if nbr.isdigit()]
        pages_number = int(numbers[0]/20)
        self.nb_pages = pages_number

    def set_all_pages_links(self):
        """Get all the apartment ads links
        :return: total links of all pages
        :rtype: list
        """
        for i in range(1, self.nb_pages+1):
            html_page = self.get_html_page(i)
            page_links = self.get_all_links_for_page(html_page)
            sleep(randint(12, 20))
            for link in page_links:
                self.links.append(link)


    def get_all_links_for_page(self, html_page):
        """Get all the links for a given page

        :param html_page: HTML Page
        :type html_page: BeautifulSoup
        :return: List of all the links
        :rtype: list[str]
        """
        links = html_page.find_all('a', {"class": "linkToFa"})
        return [link['href'] for link in links]


    def export_to_gcs(self):
        """Export the HTML to Google Cloud Storage
        """
        for index, link in enumerate(self.links, start=1):
            ad_page = self.get_apartment_ad(link)
            today = date.today()
            date_of_day = today.strftime("%d-%m-%Y")
            filename = "apartment_ad_{}_{}.html".format(index, date_of_day)
            client = storage.Client()
            bucket = client.get_bucket('ml-esme-real-estate-data')
            blob = bucket.blob("logic-immo/" + filename)
            blob.upload_from_string(ad_page)
            print(filename)