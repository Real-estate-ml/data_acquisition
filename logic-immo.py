from bs4 import BeautifulSoup
import requests
from time import sleep

url = 'https://www.logic-immo.com/vente-immobilier-ile-de-france,1_0/options/groupprptypesids=1,2,6,7,12/page='

class links_logic_immo:
    """
    The aim of this class is to scrap all the (href) links of the a balise with class: linkToFa

    # Parameters: url (str) : url of yhe website
    """

    def __init__(self, url):
        self.url = url

    def get_all_links(nothing):
        """
        #Parameter : url (str) url of the website ending by 'page='
                     url2 (str) url of the website with page 1 to ...
                     links (list) A list containing all the tags a

        #Return : links_clean (list) : A list containing all links
        """
        links_clean = []
        for i in range(7, 15):
            url2 = str(url+str(i))
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
            page = requests.get(url2, headers=headers)
            print(page)
            soup = BeautifulSoup(page.text, "html.parser")
            links = soup.find_all('a', {"class": "linkToFa"})
            for zbrr in links:
                links_clean.append(zbrr['href'])
            sleep(1.1)
        return links_clean


liens = links_logic_immo(url)
a = liens.get_all_links()

print(a)
print(len(a))

#160