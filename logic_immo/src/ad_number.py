from bs4 import BeautifulSoup
import requests

url = 'https://www.logic-immo.com/vente-immobilier-ile-de-france,1_0/options/groupprptypesids=1'

def get_ad_number(url):
    """
    The aim of this function is to return the number of page from logic_immo website in order to get all the real-estate ads
    :param url: url of the website.
    :return number: number of pages.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    number = soup.find("h1", {"class": "titleSearch"}).text
    numbers = [int(nbr) for nbr in number.split() if nbr.isdigit()]
    nombre_de_pages = int(numbers[0]/20)
    return(nombre_de_pages)

print(get_ad_number(url))