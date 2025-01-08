import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Charger le dataset
data = pd.read_csv('shopping_trends.csv')

# Dashboard interactif avec Streamlit
st.set_page_config(page_title="Customer Shopping Trends Dashboard", layout="wide")
st.title("📊 Customer Shopping Trends Dashboard")
st.markdown("---")

# Section 1 : KPI Cards
st.header("🔎 Key Performance Indicators (KPIs)")
col1, col2, col3 = st.columns(3)

# KPI 1 : Montant moyen dépensé
average_spend = data['Purchase Amount (USD)'].mean()
col1.metric("Montant moyen dépensé", f"${average_spend:.2f}")

# KPI 2 : Produit le plus vendu
top_product = data['Item Purchased'].value_counts().idxmax()
col2.metric("Produit le plus vendu", top_product)

# KPI 3 : Taux d'utilisation des codes promo
promo_usage_percentage = (data['Promo Code Used'].value_counts(normalize=True) * 100)['Yes']
col3.metric("Taux d'utilisation des codes promo", f"{promo_usage_percentage:.2f}%")

st.markdown("---")

# Section 2 : Visualisations
st.header("📊 Visualisations des Données")

# Configuration des tailles et styles des graphiques
plt.style.use('ggplot')

# Répartition des notes attribuées
st.subheader("Répartition des notes attribuées")
rating_distribution = data['Review Rating'].value_counts()
fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(rating_distribution.index, rating_distribution.values, color="skyblue")
ax.set_title("Distribution des Notes", fontsize=12)
ax.set_xlabel("Notes", fontsize=10)
ax.set_ylabel("Nombre d'Avis", fontsize=10)
st.pyplot(fig)

# Taux d'utilisation des codes promo
st.subheader("Taux d'utilisation des codes promo")
promo_usage = data['Promo Code Used'].value_counts()
fig, ax = plt.subplots(figsize=(5, 5))
ax.pie(promo_usage, labels=promo_usage.index, autopct='%1.1f%%', startangle=90, colors=["#FF9999", "#66B3FF"], wedgeprops={"edgecolor": "black"})
ax.set_title("Utilisation des Codes Promo", fontsize=12)
st.pyplot(fig)

# Méthodes de paiement les plus utilisées
st.subheader("Méthodes de paiement les plus utilisées")
payment_methods = data['Payment Method'].value_counts()
fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(payment_methods.index, payment_methods.values, color="#66C2A5")
ax.set_title("Répartition des Méthodes de Paiement", fontsize=12)
ax.set_xlabel("Méthodes de Paiement", fontsize=10)
ax.set_ylabel("Nombre de Transactions", fontsize=10)
plt.xticks(rotation=45, ha="right")
st.pyplot(fig)

st.markdown("---")

# Section 3 : Insights supplémentaires
st.header("📈 Insights Supplémentaires")

# Produit le plus vendu par catégorie
st.subheader("Produit le plus vendu par catégorie")
top_products_by_category = data.groupby('Category')['Item Purchased'].apply(lambda x: x.value_counts().idxmax())
st.dataframe(top_products_by_category)
