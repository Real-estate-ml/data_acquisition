from bs4 import BeautifulSoup
import requests
from time import sleep
import re

a = ['https://www.logic-immo.com/detail-vente-d4ee5582-687c-25e7-a1e1-f712f59b2ab3.htm', 'https://www.logic-immo.com/detail-vente-2bb9060d-5b6a-30c7-1178-ddb7cf53810b.htm']


def get_rooms(var):
    """
    The aim of this function is to return all the room from a list of links

    #Parameter :    var (list) : List of all the links
                    floor (list) : List of all the tag which contains the rooms

    #Return :   floor_clean (list) : A list containing all the rooms
    """
    headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'}
    room_clean = []
    for i in range(0, len(var)):
        page = requests.get(var[i], headers=headers)
        print(page)
        soup = BeautifulSoup(page.text, "html.parser")
        room = soup.find("em", {"class": "feature mobileOnly"})
        for i in room:
            regex = re.compile(r'[a-z]\.')
            room_clean.append(regex.sub(" ", i.text))
        sleep(1.1)
    return(room_clean)

print(get_rooms(a))
print(len(get_rooms(a)))

