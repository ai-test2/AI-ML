import streamlit as st
import pandas as pd

# 1. Postavka stranice u "wide" režim (izgled modernog portala)
st.set_page_config(
    page_title="AI & ML App",
    page_icon="⚡",
    layout="wide"
)
# 2. LIJEVI PANEL (SIDEBAR) - Meni sa aplikacijama
st.sidebar.title("AI & ML modeli")
st.sidebar.markdown("---")

from streamlit_option_menu import option_menu

with st.sidebar:
    st.markdown("### Odaberite model")
    
    odabrana_aplikacija = option_menu(
        menu_title=None,
        options=["Kauzalni ML", "Prediktivni ML", "Sentiment Analiza"],
        icons=None,
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
             "icon": {"display": "none"}, # Potpuno sakriva ikone ako ih negdje povuče
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "padding": "8px 12px",
                "border-radius": "8px", # Zaobljeni rubovi u Google stilu
                "--hover-color": "rgba(155, 155, 155, 0.1)", # Suptilni hover efekt
            },
            # Google-like aktivna stavka: nježna siva pozadina i tamniji/jasniji tekst
            "nav-link-selected": {
                "background-color": "rgba(155, 155, 155, 0.1)", 
                "color": "#1f1f1f", # Prilagodi boju teksta ako želiš (ili makni ovu liniju pa će uzeti temu)
                "font-weight": "500",
                "border-radius": "8px",
            },
        }
    )



st.sidebar.markdown("---")

# ----------------------------------------------------
# KAUZALNI ML SEKCIJA
# ----------------------------------------------------
if odabrana_aplikacija == "Kauzalni ML":
  # Ovaj podmeni se POJAVLJUJE SAMO KADA JE IZABRAN "Kauzalni ML"
  st.sidebar.markdown("### Koraci kauzalnog toka")

  korak = st.sidebar.radio(
      "Izaberite korak:",
      [
          "1. Učitavanje biblioteka",
          "2. Upload podataka",
          "3. ATE (Average Treatment Effect)",
          "4. CATE & SHAP",
          "5. Potencijal varijabli T",
          "6. Decision Tree Rules",
          "7. Best Channel Allocation",
          "8. Uplift Kvadrantna Segmentacija",
          "9. Causal Assumptions",
          "10. Refutation / Sensitivity Tests",
          "11. Qini Curve & AUUC",
      ],
  )



    
    st.write("")



# 3. GLAVNI RADNI PROSTOR
if odabrana_aplikacija == "Kauzalni ML":
    st.title("Kauzalni ML")
    st.write("Dobrodošli u modul za kauzalno modeliranje. Pratite korake ispod:")

    # Gumbovi / Tabovi na vrhu radnog prostora za tok rada (Workflow)
    korak1, korak2, korak3, korak4, korak5, korak6, korak7, korak8, korak9, korak10, korak11, korak12, korak13, korak14, korak15, korak16, korak17, korak18, korak19, korak20, korak21, = st.tabs([
        "Učitavanje biblioteka", "", "Upload podataka", "", "ATE", "", "CATE & SHAP", "", "Potencijal varijabli T", "", "Decision Tree Rules", "", "Best Channel Allocation", "", "Uplift Kvadrantna Segmentacija", "", "Causal Assumptions", "", "Refutation / Sensitivity Tests", "", "Qini Curve & AUUC",
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
