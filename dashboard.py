import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dashboard interactif avec Streamlit
st.title("Dashboard - Customer Shopping Trends")

# KPI : Montant moyen dépensé
average_spend = 59.76  # Exemple de donnée
st.metric("Montant moyen dépensé", f"${average_spend:.2f}")

# Visualisation de la répartition des notes
rating_distribution = {
    5: 100,
    4: 200,
    3: 150,
    2: 50,
    1: 30
}
fig, ax = plt.subplots()
ax.bar(rating_distribution.keys(), rating_distribution.values())
st.pyplot(fig)
