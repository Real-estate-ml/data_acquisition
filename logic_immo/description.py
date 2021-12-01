from bs4 import BeautifulSoup
import requests
from time import sleep
import re, string

a = ['https://www.logic-immo.com/detail-vente-d4ee5582-687c-25e7-a1e1-f712f59b2ab3.htm', 'https://www.logic-immo.com/detail-vente-2bb9060d-5b6a-30c7-1178-ddb7cf53810b.htm']

def get_description(var):
    """
    The aim of this function is to return all the description from a list of links

    #Parameter :    var (list) : List of all the links
                    price (list) :

    #Return :   price_clean (list) : A list containing all the descriptions
    """
    headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'}
    description_clean = []
    for i in range(0, len(var)):
        page = requests.get(var[i], headers=headers) #Import for drive
        print(page)
        soup = BeautifulSoup(page.text, "html.parser")
        description = soup.find("p", {"class": "descrProperty"})
        for i in description:
            regex = re.compile('[%s]' % re.escape(string.punctuation))
            description_clean.append(regex.sub(" ", i.text))
        sleep(1.1)
    return(description_clean)

print(get_description(a))
print(len(get_description(a)))

