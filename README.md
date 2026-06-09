# 📊 Customer Shopping Trends Dashboard

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0+-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25.0+-FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

Une solution moderne de visualisation et d'analyse des tendances d'achat clients, combinant une **API REST performante (FastAPI)** et un **Dashboard analytique interactif (Streamlit)**.

---

## 📝 Description du Projet

Ce projet exploite le dataset **Customer Shopping Trends** pour offrir aux entreprises des indicateurs clés (KPIs) et des visualisations interactives permettant de mieux comprendre les comportements d'achat de leurs clients. 

> [!NOTE]
> **Dataset Source :** [Customer Shopping Latest Trends Dataset (Kaggle)](https://www.kaggle.com/datasets/bhadramohit/customer-shopping-latest-trends-dataset)

---

## ⚙️ Fonctionnalités Clés

### ⚡ API REST (FastAPI)
- **Calculs en temps réel** des indicateurs clés de performance (KPIs).
- **Endpoints documentés** pour l'intégration de systèmes tiers (Swagger UI / ReDoc).
- **Recherche par client** dynamique (`/customers/{id}`).

### 📊 Dashboard Interactif (Streamlit)
- **KPI Cards** synthétiques (Montant moyen dépensé, Produit phare, Utilisation des codes promo).
- **Visualisations graphiques** interactives :
  - *Distribution des notes* (Histogramme des avis clients).
  - *Utilisation des codes promo* (Partage en diagramme circulaire).
  - *Méthodes de paiement préférées* (Répartition par type de transaction).
- **Analyses croisées** : Tableau dynamique du produit le plus vendu par catégorie.

---

## 📂 Architecture des Fichiers

```directory
shopping-trends-dashboard/
├── main.py                # Point d'entrée de l'API FastAPI
├── dashboard.py           # Application Dashboard Streamlit
├── shopping_trends.csv    # Source de données locale (CSV)
├── README.md              # Documentation du projet
└── requirements.txt       # Liste des dépendances Python
```

---

## 🚀 Installation & Lancement Rapide

### 1️⃣ Cloner le dépôt
```bash
git clone https://github.com/achrafthedev/shopping-trends-dashboard.git
cd shopping-trends-dashboard
```

### 2️⃣ Configurer l'environnement virtuel
```bash
# Création de l'environnement virtuel
python -m venv venv

# Activation
# Sur Windows :
venv\Scripts\activate
# Sur macOS/Linux :
source venv/bin/activate
```

### 3️⃣ Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4️⃣ Lancer l'API FastAPI
```bash
uvicorn main:app --reload
```
* **Documentation interactive (Swagger) :** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **API de base :** [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 5️⃣ Lancer le Dashboard Streamlit
Dans un nouveau terminal (avec l'environnement virtuel activé) :
```bash
streamlit run dashboard.py
```
* **Accès local :** [http://localhost:8501](http://localhost:8501)

---

## 📡 Documentation des Endpoints de l'API

Tous les endpoints renvoient des données structurées au format JSON :

| Méthode | Endpoint | Description | Exemple de Réponse |
| :--- | :--- | :--- | :--- |
| `GET` | `/kpi/average-spend` | Calcule le montant moyen des achats. | `{"average_spend": 59.76}` |
| `GET` | `/kpi/rating-distribution` | Distribution des notes des avis clients. | `{"rating_distribution": {"4.0": 120, "5.0": 85}}` |
| `GET` | `/kpi/promo-usage` | Pourcentage de transactions avec code promo. | `{"promo_usage_percentage": 43.0}` |
| `GET` | `/products/top` | Identifie le produit le plus acheté. | `{"top_product": "Blouse"}` |
| `GET` | `/customers/{customer_id}` | Récupère la ligne complète d'un client. | `{"Customer ID": 1, "Age": 55, "Item Purchased": "Blouse", ...}` |

---

## 🛠️ Stack Technique

* **Langage :** [Python 3.8+](https://www.python.org/)
* **Framework Backend :** [FastAPI](https://fastapi.tiangolo.com/) + [Uvicorn](https://www.uvicorn.org/)
* **Frontend/Data Viz :** [Streamlit](https://streamlit.io/) + [Matplotlib](https://matplotlib.org/)
* **Manipulation de Données :** [Pandas](https://pandas.pydata.org/)

---

## 🤝 Contribution & Support

Les contributions, issues et suggestions d'amélioration sont les bienvenues !
1. Forkez le projet.
2. Créez votre branche de fonctionnalité (`git checkout -b feature/AmazingFeature`).
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`).
4. Pushez votre branche (`git push origin feature/AmazingFeature`).
5. Ouvrez une Pull Request.

---

## 📧 Contact & Liens

* **Développeur :** Achraf (achrafthedev)
* **Email :** achrafthedev@gmail.com
* **GitHub :** [@achrafthedev](https://github.com/achrafthedev)
* **Licence :** MIT License
