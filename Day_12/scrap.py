import requests
from bs4 import BeautifulSoup

# L'URL de la page d'accueil de Wikipédia
url = "https://www.youtube.com/"

# Récupération du contenu de la page
response = requests.get(url)

if response.status_code == 200:
    # Parsing du HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extraction de tous les tags <h1>
    h1_tags = soup.find_all('h1')
    
    # Affichage des balises complètes (comme dans ton exemple)
    print(f"List all the h1 tags from {url}:")
    for tag in h1_tags:
        print(tag)
else:
    print(f"Erreur de connexion : {response.status_code}")