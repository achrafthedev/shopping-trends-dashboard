# 📊 Customer Shopping Trends Dashboard

## 📝 Description
Ce projet est un **dashboard interactif** développé avec **Streamlit** et une **API FastAPI** permettant de visualiser les tendances d'achat des clients à partir du dataset **Customer Shopping Trends**. Il offre des visualisations claires et des indicateurs clés (KPI) pour analyser les données clients, les produits vendus, et les préférences des utilisateurs.

## ⚙️ Fonctionnalités principales
- ✅ **API RESTful avec FastAPI** pour exposer les données sous forme d'endpoints.
- ✅ **Dashboard interactif avec Streamlit** pour visualiser les données et les KPI.
- 📊 Visualisations des notes attribuées, des méthodes de paiement, et des taux d'utilisation des codes promo.
- 🔎 **KPI** tels que le montant moyen dépensé, le produit le plus vendu, et le taux d'utilisation des codes promo.

---

## 📂 Structure du projet
```
PythonProject/
├── main.py          # Code de l'API avec FastAPI
├── dashboard.py     # Dashboard interactif avec Streamlit
├── shopping_trends.csv  # Dataset utilisé pour les analyses
└── README.md        # Documentation du projet
```

---

## 🚀 Installation
### 1️⃣ Cloner le projet
```bash
git clone https://github.com/achrafthedev/shopping-trends-dashboard.git
cd shopping-trends-dashboard
```

### 2️⃣ Créer un environnement virtuel (optionnel mais recommandé)
```bash
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4️⃣ Lancer l'API FastAPI
```bash
uvicorn main:app --reload
```
➡️ **Accès à l'API :** [http://127.0.0.1:8000](http://127.0.0.1:8000)  
➡️ **Documentation Swagger UI :** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 5️⃣ Lancer le Dashboard Streamlit
```bash
streamlit run dashboard.py
```
➡️ **Accès au dashboard :** [http://localhost:8501](http://localhost:8501)

---

## 📊 Endpoints de l'API FastAPI
| **Endpoint**           | **Description**                          | **Exemple de réponse**              |
|------------------------|------------------------------------------|-------------------------------------|
| `/kpi/average-spend`    | Retourne le montant moyen dépensé        | `{ "average_spend": 59.76 }`      |
| `/kpi/rating-distribution` | Répartition des notes attribuées       | `{ "rating_distribution": { "5": 100, "4": 200 } }` |
| `/kpi/promo-usage`      | Taux d'utilisation des codes promo       | `{ "promo_usage_percentage": 43.0 }` |
| `/products/top`         | Produit le plus vendu                   | `{ "top_product": "Blouse" }`     |
| `/customers/{customer_id}` | Informations sur un client spécifique | `{ "customer_id": 1, "age": 25 }` |

---

## 🎨 Visualisations incluses dans le Dashboard
| **Visualisation**                      | **Description**                                      |
|---------------------------------------|----------------------------------------------------|
| Répartition des notes attribuées       | Histogramme montrant le nombre d'avis par note      |
| Taux d'utilisation des codes promo     | Graphique en camembert affichant les utilisateurs ayant utilisé un code promo |
| Méthodes de paiement les plus utilisées | Diagramme à barres montrant les préférences de paiement |
| Produit le plus vendu                  | Affichage du produit le plus populaire dans le dataset |

---

## 📌 KPI (Key Performance Indicators)
- 💰 **Montant moyen dépensé par client**
- 📦 **Produit le plus vendu**
- 🎟️ **Taux d'utilisation des codes promo**

---

## 🧪 Tests de l'API
Pour tester les endpoints de l'API, vous pouvez utiliser **Swagger UI** à l'adresse suivante : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) ou un outil comme **Postman**.

---

## 🛠️ Technologies utilisées
- **Python**
- **FastAPI**
- **Streamlit**
- **Pandas**
- **Matplotlib**

---

## 📄 Licence
Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, le modifier et le distribuer.

---

## 🤝 Contributions
Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request sur le dépôt GitHub.

---

## 📧 Contact
Pour toute question ou suggestion, vous pouvez me contacter à :
- **Email :** achrafthedev@gmail.com
- **GitHub :** [https://github.com/achrafthedev](https://github.com/achrafthedev)
