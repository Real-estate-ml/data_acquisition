import requests
from bs4 import BeautifulSoup
from math import ceil
import time

# Lien du scraping
AvendreAlouer_url = "https://www.avendrealouer.fr/recherche.html?pageIndex=1&sortPropertyName=ReleaseDate&sortDirection=Descending&searchTypeID=1&typeGroupCategoryID=1&localityIds=3-75&typeGroupIds=1&minimumPrice=199000&maximumPrice=200000&searchId=client-637696892120430000&hasAlert=false"

# header pour Windows
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

# Scraping pour trouver les informations de la page generale
r = requests.get(AvendreAlouer_url, headers=headers)
c = r.content
# print(c)
soup = BeautifulSoup(c, "html.parser")

# On récupère le nombre d'annonces trouvées :
Nb_annonces = soup.find("h1", {"class": "h1title"})  # Recupère le titre de la recherche
all_annonces = ""
all_annonces = (Nb_annonces.text.strip())
print(all_annonces)

# Pour avoir le nombre de pages:
temp_string = all_annonces
numbers = [int(temp) for temp in temp_string.split() if temp.isdigit()]
int_list = [int(i) for i in numbers]
int_list = [ceil(i / 25) for i in int_list]  # 25 car 25 annonces par pages maxi
print(int_list)

"Creation des variables qu'on veux recupérer :"
links = []
all_links = []

for i in range(int_list[0]):  # boucle for pour parcourir toutes les pages et ne pas oublier d'annonce
    # print(i+1)
    # my_url = "https://www.avendrealouer.fr/recherche.html?pageIndex=" + str(i + 1) + "&sortPropertyName=Price&sortDirection=Ascending&searchTypeID=1&typeGroupCategoryID=6&localityIds=3-75&typeGroupIds=47,48&maximumPrice=" + str(budget_utilisateur) + "&minimumSurface=" + str(surface_utilisateur) + "&bedroomComfortIds=" + str(chambres_utilisateur) + "&searchId=client-637572957167650000&hasAlert=false"
    my_url = "https://www.avendrealouer.fr/recherche.html?pageIndex=" + str(
        i + 1) + "&sortPropertyName=ReleaseDate&sortDirection=Descending&searchTypeID=1&typeGroupCategoryID=1&localityIds=3-75&typeGroupIds=1&minimumPrice=199000&maximumPrice=200000"
    # print(my_url)
    r = requests.get(my_url, headers=headers)
    c = r.content
    # print(c)
    soup = BeautifulSoup(c, "html.parser")

    # On récupère les liens cliquable des biens
    baseUrl = "https://www.avendrealouer.fr"
    Lien = soup.find_all("div", {"class": "listing-item-head"})

    for url in Lien:
        # print(url.a["href"])
        links.append(url.a['href'])
        links = list(set(links))

    # supprime les doublons suivant les annonces on peut visiter en virtuelle ou voir l'annonce donc le lien est double
    for x in links:
        all_links.append(baseUrl + x)
        all_links = list(set(all_links))
    # print(all_links)
    i = 1
    for y in all_links:
        re = requests.get(y, headers=headers)
        ce = re.content
        # print(c)
        soup2 = BeautifulSoup(ce, "html.parser")
        fichier = open("data_" + str(i) + ".html", "wb")
        fichier.write(c)
        fichier.close()
        time.sleep(3)
        i=i+1
print(len(links))
print((all_links))

# initialisation  des variables :
all_prices = []





