import streamlit as st

# Configuration
st.set_page_config(page_title="The Smart Closet", layout="wide")

# Titre
st.title("✨ The Smart Closet")
st.subheader("Votre guide d'élégance personnalisé")

# Organisation en colonnes
col1, col2 = st.columns(2)

with col1:
    st.write("Bienvenue dans votre espace dédié au style.")
    if st.button('Lancer une surprise 🎈'):
        st.balloons()

with col2:
    # Image d'inspiration mode
    st.image("https://images.unsplash.com/photo-1490481651871-ab68de25d43d", caption="Style & Élégance")

st.divider()
st.info("Prochaine étape : Intégrer vos schémas et visuels ici !")

