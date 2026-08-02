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

st.sidebar.markdown("### Odaberite model")

opcije = ["Kauzalni ML", "Prediktivni ML", "Sentiment Analiza"]

# Inicijalizacija stanja
if "odabrana_aplikacija" not in st.session_state:
    st.session_state.odabrana_aplikacija = "Kauzalni ML"

# Prikaz gumba jedan ispod drugog
for opcija in opcije:
    # Provjeravamo je li trenutna opcija odabrana da promijenimo stil/izgled
    is_selected = (st.session_state.odabrana_aplikacija == opcija)
    
    # Koristimo st.button s punom širinom unutar sidebara
    if st.sidebar.button(
        opcija, 
        key=f"btn_{opcija}", 
        use_container_width=True,
        type="primary" if is_selected else "secondary"
    ):
        st.session_state.odabrana_aplikacija = opcija
        st.rerun()

odabrana_aplikacija = st.session_state.odabrana_aplikacija




from streamlit_option_menu import option_menu

with st.sidebar:
    st.markdown("### Odaberite model")
    
    odabrana_aplikacija = option_menu(
        menu_title=None,  # Sakrivamo glavni naslov izbornika jer već imamo markdown iznad
        options=["Kauzalni ML", "Prediktivni ML", "Sentiment Analiza"],
        icons=None,  # Maknuli smo ikonice da bude potpuno minimalistički (samo tekst)
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "orange", "font-size": "14px"}, 
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee", # Suptilna boja na hover
            },
            "nav-link-selected": {"background-color": "#02ab21"}, # Boja kada je odabrano (možeš prilagoditi)
        }
    )
























odabrana_aplikacija = st.sidebar.pills(
    "Odaberite model",
    ["Kauzalni ML", "Prediktivni ML", "Sentiment Analiza"]
)

odabrana_aplikacija = st.sidebar.segmented_control(
    "Odaberite model",
    ["Kauzalni ML", 
     "Prediktivni ML", 
     "Sentiment Analiza"],
    default="Kauzalni ML"
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
