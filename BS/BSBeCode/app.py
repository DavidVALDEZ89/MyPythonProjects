# On importe requests
import requests
# On importe beautifulsoup
from bs4 import BeautifulSoup as bs

# On défini l'url du site
url = "https://www.gov.uk/search/news-and-communications"
# On utilise la fonction get() du package requests
page = requests.get(url)
soup = bs(page.content, 'html.parser')
# On utilise beautifulsoup pour aller chercher les balises a avec la classe "gem-c-document-list__item-title"
titres_bs = soup.find_all("a", class_="gem-c-document-list__item-title")
# On utilise beautifulsoup pour aller chercher les balises a avec la classe "gem-c-document-list__item-title"
descriptions_bs = soup.find_all("p", class_="gem-c-document-list__item-description")
# On utilise beautifulsoup pour aller chercher les balises p avec la classe "gem-c-document-list__item-description"
updated_bs = soup.find_all("li", class_="gem-c-document-list__attribute")

titres = []
# On initie des listes vides

descriptions = []
# On initie des listes vides

updates = []

for titre in titres_bs:
    # print(titre.string)
    titres.append(titre.string)

# On boucle et on push dans notre liste

for index, description in enumerate(descriptions_bs):
    descriptions.append((index, description.string))

# On boucle et on push dans notre liste

for indexx, update in enumerate(updated_bs):
    updates.append((indexx, update.string))

liste = range (9)
for i in liste :
    print(i,"Titre :\n",titres[i],'\nDescription :\n',descriptions[i][1],"\n \n",end='\r',)
    # print(i,"Trite :\n",titres[i],'\nDescription :\n',descriptions[i][1],"\n",updates[i][2],"\n \n",end='\r',)
    # print (titres[i])
    # print (descriptions[i])
    # print (updates[i])
    
print(updates)
