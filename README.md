# Scraper de Données pour Courses Hippiques

Ce projet est un outil de scraping conçu pour extraire des informations sur les courses hippiques depuis le site [Daily Racing Form (DRF)](https://www.drf.com/). Il propose une interface graphique basique (GUI) pour visualiser les données et naviguer dans les différentes fonctionnalités.

---

## **Fonctionnalités**

### **Scraper**
- **Extraction des résultats des courses** :
  - Récupère les chevaux classés parmi les 3 premiers dans une course.
  - Parcourt les dates pour collecter les données sur plusieurs jours.
- **Extraction des courses à venir** :
  - Identifie les chevaux inscrits dans des courses à venir.
  - Génère dynamiquement les URL des pistes et des dates.
- **Support des pistes américaines** :
  - Une liste de pistes comme *Churchill Downs*, *Tampa Bay Downs*, etc., est incluse.
  
### **Interface Graphique (GUI)**
- **Vues disponibles** :
  - **Statistiques des équipes** : Placeholder pour intégrer des statistiques.
  - **Pronostics** : Placeholder pour intégrer des prédictions basées sur les données collectées.
- **Navigation simple** :
  - Interface intuitive permettant de naviguer entre les différents écrans.

---

## **Prérequis**

- **Version de Python** : 3.8 ou supérieur
- **Dépendances Python** :
  - `requests`
  - `beautifulsoup4`
  - `tkinter` (souvent inclus avec Python)

Pour installer les dépendances :
```bash
pip install -r requirements.txt
```

---

## **Utilisation**

### **1. Scraping des données**
Utilisez la classe `Scrapper` pour collecter des données sur les courses en fournissant une plage de dates et un ID de piste :
```python
from scrapper import Scrapper
from datetime import datetime

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 1, 31)

scraper = Scrapper()
scraper.scroll_through_dates(start_date, end_date, Track_ID="CD", Finished=True)
```

### **2. Interface Graphique**
Lancez l'application avec l'interface graphique en exécutant le fichier principal :
```bash
python main.py
```
Naviguez entre les différentes sections via l'interface utilisateur.

---

## **Structure des fichiers**

```
.
├── scrapper.py          # Classe pour le scraping des données
├── gui.py               # Implémentation de l'interface graphique
├── main.py              # Point d'entrée de l'application
├── requirements.txt     # Liste des dépendances Python
└── README.md            # Documentation du projet
```

---

## **Améliorations futures**
- **Scraper** :
  - Finaliser les méthodes pour extraire toutes les informations clés des courses.
  - Améliorer la gestion des erreurs.
- **GUI** :
  - Intégrer les données collectées pour affichage dans l'interface.
  - Ajouter des outils de filtrage et d'analyse.
- **Sauvegarde** :
  - Ajouter une fonctionnalité d'exportation des données en CSV ou en base de données.
- **Automatisation** :
  - Ajouter un système de planification pour des exécutions automatiques.

---

## **Contributions**

Les contributions sont bienvenues ! Si vous souhaitez contribuer :
1. Forkez le dépôt.
2. Créez une branche pour vos modifications.
3. Faites un commit avec une description claire.
4. Soumettez une pull request.

---

## **Licence**

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus d'informations.

---

## **Auteur**
BILL YAN
HENINTSOA RAMAKAVELO
PIERRE STEVE NGWEHA
JEFF DJOUSSE
IZAC TIOTE
