###importation des biblitheques
import pandas as pd
import scrapy   
import requests 
from bs4 import BeautifulSoup

##liste des urls a scrap
urls = [
    "https://us.racingstats247.com/horses/United-States/",
    "https://www.racingstats247.com/horses/United-Kingdom/",
    "https://fr.racingstats247.com/chevaux/France/",
    "https://ca.racingstats247.com/horses/Canada/",
    "https://ie.racingstats247.com/horses/Ireland/"
]

all_dataframes = []  ##liste pour les donnees recuprer

for url in urls:   ##boucle pour recuperer les donnees dans chaque url
    headers = {
    'User -Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
    try:
        reponse = requests.get(url, headers=headers) ##requete get pour recuperer les pages
        reponse.raise_for_status()  # Vérifie les erreurs HTTP
        soup = BeautifulSoup(reponse.text, "html.parser")
        table = soup.find('table', id='racingContentPlaceHolder_gvTopHorses')
        
        if table:
            headers = [th.get_text(strip=True) for th in table.find_all("th")]
            rows = []
            for tr in table.find_all("tr")[1:]:
                cols = tr.find_all("td")
                if len(cols) > 1:
                    rows.append([col.get_text(strip=True) for col in cols])
            df = pd.DataFrame(rows, columns=headers)
            all_dataframes.append(df)
            print(df.head())
        else:
            print(f'Erreur lors de la récupération du tableau pour {url}')
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération de la page {url}: {e}")

# Exporter toutes les données dans un seul fichier CSV
if all_dataframes:
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_csv("cheveaux.csv", index=False)
    print("Les données ont été exportées dans 'cheveaux.csv'.")
else:
    print("Aucune donnée à exporter.")