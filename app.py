import streamlit as st
import pandas as pd

# 1. Postavka stranice u "wide" režim (izgled modernog portala)
st.set_page_config(
    page_title="AI & ML Control Center",
    page_icon="⚡",
    layout="wide"
)

# 2. LIJEVI PANEL (SIDEBAR) - Meni sa aplikacijama
st.sidebar.title("🎛️ Control Portal")
st.sidebar.markdown("---")

odabrana_aplikacija = st.sidebar.radio(
    "Odaberite modul:",
    ["Kauzalni ML", "Prediktivni ML", "Sentiment Analiza"]
)

st.sidebar.markdown("---")
st.sidebar.caption("Sistem v1.0 | Streamlit & GitHub Connected")


# 3. GLAVNI RADNI PROSTOR
if odabrana_aplikacija == "Kauzalni ML":
    st.title("🎯 Kauzalni ML Modul")
    st.write("Dobrodošli u modul za kauzalno modeliranje. Pratite korake ispod:")
    
    # Gumbovi / Tabovi na vrhu radnog prostora za tok rada (Workflow)
    korak1, korak2, korak3 = st.tabs([
        "1. 📦 Učitaj Biblioteke", 
        "2. 📂 Upload Podataka", 
        "3. 🚀 Pokreni Analizu"
    ])
    
    # --- KORAK 1: Učitavanje biblioteka ---
    with korak1:
        st.subheader("Učitavanje potrebnih Python paketa")
        if st.button("Učitaj CausalML i Scikit-Learn"):
            # Ovdje u pozadini učitavate vaše biblioteke
            st.success("Biblioteke su uspješno učitane u memoriju!")
            
    # --- KORAK 2: Upload i validacija podataka ---
    with korak2:
        st.subheader("Unos podataka")
        st.info("Napomena: Podaci moraju imati standardizovane kolone ($x_1, x_2, \dots, x_n$).")
        
        uploaded_file = st.file_uploader("Dodajte vašu CSV datoteku", type=["csv"])
        
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.write("### Pregled učitanih podataka:")
            st.dataframe(df.head())
            
    # --- KORAK 3: Izvršavanje analize ---
    with korak3:
        st.subheader("Pokretanje kauzalnog modela")
        if st.button("Pokreni Kauzalnu Analizu"):
            st.balloons()
            st.success("Analiza je uspješno završena!")

elif odabrana_aplikacija == "Prediktivni ML":
    st.title("📈 Prediktivni ML Modul")
    st.warning("Ovaj modul je trenutno u fazi izrade.")

elif odabrana_aplikacija == "Sentiment Analiza":
    st.title("💬 Sentiment Analiza Modul")
    st.warning("Ovaj modul je trenutno u fazi izrade.")
