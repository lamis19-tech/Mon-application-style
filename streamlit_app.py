import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Mon Projet", layout="wide")

# Titre principal
st.title("✨ Bienvenue dans mon univers")

# Une petite introduction
st.subheader("La mode et l'élégance à portée de main")

# Création de deux colonnes pour le visuel
col1, col2 = st.columns(2)

with col1:
    st.write("Ici, nous allons construire ton catalogue visuel.")
    # Bouton d'action
    if st.button('Découvrir la collection'):
        st.balloons()
        st.success("C'est parti !")

with col2:
    # Espace pour une image (tu pourras remplacer l'URL plus tard)
    st.image("https://images.unsplash.com/photo-1445205170230-053b83e26371", caption="Inspiration Style")

st.divider()
st.info("Astuce : Pour ajouter tes propres schémas de Canva, il suffira de les importer ici !")
