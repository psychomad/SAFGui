import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import time

# Forziamo il tema Dark tramite configurazione
st.set_page_config(
    page_title="Centuria SAF Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# CSS per forzare lo sfondo scuro e testo chiaro su tutta la pagina
st.markdown("""
    <style>
    /* Sfondo principale */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    /* Cards delle metriche */
    [data-testid="stMetricValue"] {
        color: #00ff00 !important;
    }
    [data-testid="stMetricLabel"] {
        color: #808b96 !important;
    }
    div[data-testid="stMetric"] {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 20px;
        border-radius: 10px;
    }
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0b0e14;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Centuria SAF | Security Monitor")

# Sidebar
st.sidebar.header("Settings")
saf_url = st.sidebar.text_input("SAF API URL", "http://localhost:3000/api/stats")

if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=['Timestamp', 'Total', 'Blocked'])

def fetch_stats():
    try:
        response = requests.get(saf_url, timeout=0.5)
        return response.json()
    except:
        return None

# Layout
metrics_row = st.columns(3)
chart_row = st.columns(1)

data = fetch_stats()

if data:
    with metrics_row[0]:
        st.metric("Total Packets", f"{data['total_packets']:,}")
    with metrics_row[1]:
        # Rosso se ci sono blocchi, verde se zero
        st.metric("Blocked Attacks", f"{data['blocked_packets']:,}")
    with metrics_row[2]:
        st.metric("Active Blacklist", data['active_blacklist_count'])

    # Aggiornamento storico
    new_entry = pd.DataFrame([{
        'Timestamp': pd.Timestamp.now(),
        'Total': data['total_packets'],
        'Blocked': data['blocked_packets']
    }])
    st.session_state.history = pd.concat([st.session_state.history, new_entry], ignore_index=True).tail(30)

    with chart_row[0]:
        fig = px.line(st.session_state.history, x='Timestamp', y=['Total', 'Blocked'], 
                      title="Real-time Network Load",
                      template="plotly_dark",
                      color_discrete_map={"Total": "#00ff00", "Blocked": "#ff0000"})
        
        # Miglioriamo il layout del grafico per il tema scuro
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig, width='stretch')
else:
    st.warning("🔌 Waiting for SAF Core... (Check port 3000)")

# Refresh rapido per l'effetto "Real-time"
time.sleep(1)
st.rerun()
