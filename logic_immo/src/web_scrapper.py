from bs4 import BeautifulSoup
import requests
from time import sleep
from pathlib import Path
from datetime import date
from random import randint
from google.cloud import storage

class WebScrapper():
    def __init__(self, url, start_page, end_page):
        self.url = url
        self.links = []
        self.start_page = start_page
        self.end_page = end_page

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
        current_url = self.url + "/page={}".format(str(page_number))
        page = requests.get(current_url, headers=headers)
        html_soup = BeautifulSoup(page.text, "html.parser")
        return html_soup

    def get_apartment_ad(self, link):
        """[summary]
        :param link: [description]
        :type link: str
        :return: [description]
        :rtype: [type]
        """
        sleep(randint(2, 3))
        headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'}
        page = requests.get(link, headers=headers)
        return page.text

    def set_all_pages_links(self):
        """Get all the apartment ads links
        :return: total links of all pages
        :rtype: list
        """
        for i in range(self.start_page, self.end_page+1):
            html_page = self.get_html_page(i)
            page_links = self.get_all_links_for_page(html_page)
            sleep(randint(1, 2))
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
            blob = bucket.blob("logic-immo/" + date_of_day + "/" + filename)
            blob.upload_from_string(ad_page)
            print(filename + "has been written to GCS")
