from bs4 import BeautifulSoup
import requests
from time import sleep

url = 'https://www.logic-immo.com/vente-immobilier-ile-de-france,1_0/options/groupprptypesids=1/page='

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
        for i in range(7, 8):
            url2 = str(url+str(i))
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
            page = requests.get(url2, headers=headers)
            soup = BeautifulSoup(page.text, "html.parser")
            links = soup.find_all('a', {"class": "linkToFa"})
            for j in links:
                links_clean.append(j['href'])
                for k in range(0, len(links_clean)):
                    fichier = open("data_" + str(k) + ".html", "a")
                    page2 = requests.get(links_clean[k], headers=headers)
                    fichier.write(str(page2.content))
                    fichier.close()
                    sleep(1.1)
            sleep(1.1)
        return (links_clean)


liens = links_logic_immo(url)
a = liens.get_all_links()

print(a)
