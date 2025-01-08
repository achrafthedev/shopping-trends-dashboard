from fastapi import FastAPI
import pandas as pd


# Initialisation de l'application FastAPI
app = FastAPI()

# Charger le dataset
file_path = "shopping_trends.csv"
data = pd.read_csv(file_path)

# Endpoint : Montant moyen dépensé par client
@app.get("/kpi/average-spend")
def get_average_spend():
    average_spend = data['Purchase Amount (USD)'].mean()
    return {"average_spend": round(average_spend, 2)}

# Endpoint : Répartition des notes attribuées
@app.get("/kpi/rating-distribution")
def get_rating_distribution():
    rating_distribution = data['Review Rating'].value_counts().to_dict()
    return {"rating_distribution": rating_distribution}

# Endpoint : Taux d'utilisation des codes promo
@app.get("/kpi/promo-usage")
def get_promo_usage():
    promo_usage_percentage = (data['Promo Code Used'].value_counts(normalize=True) * 100)['Yes']
    return {"promo_usage_percentage": round(promo_usage_percentage, 2)}

# Endpoint : Produits les plus vendus
@app.get("/products/top")
def get_top_products():
    top_product = data['Item Purchased'].value_counts().idxmax()
    return {"top_product": top_product}

# Endpoint : Informations sur un client spécifique
@app.get("/customers/{customer_id}")
def get_customer_info(customer_id: int):
    customer = data[data['Customer ID'] == customer_id]
    if customer.empty:
        return {"error": "Client not found"}
    return customer.to_dict(orient="records")[0]

# uvicorn main:app --reload