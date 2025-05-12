from utils.data_manager import DataManager
from utils.login_manager import LoginManager
import pandas as pd
import streamlit as st
from utils.helpers import nav_page

st.title('Login & Registrierung')

st.sidebar.page_link('Start.py', label='Startseite')
st.sidebar.page_link('pages/1_Dashboard.py', label='Dashboard')
st.sidebar.page_link('pages/2_Modulgruppen-Uebersicht.py', label='Modulgruppen-Uebersicht')


data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Institution/kestmo_App")  # Switchdrive

# initialize the login manager
login_manager = LoginManager(data_manager)

if login_manager.login_register():  # Login erfolgreich
    st.success("Login erfolgreich! Daten werden geladen...")

    # Daten aus Dateien laden, falls sie existieren
    try:
        data_manager.load_user_data(
            session_state_key="Pruefungen",
            file_name="Pruefungen.csv",
            initial_value=pd.DataFrame()
        )
    except FileNotFoundError:
        st.warning("Die Datei 'Pruefungen.csv' wurde nicht gefunden. Es wird ein leerer DataFrame verwendet.")

    #try:
     #   data_manager.load_user_data(
      #      session_state_key="Grundlagenpraktika",
       #     file_name="Grundlagenpraktika.csv",
        #    initial_value=pd.DataFrame()
        #)
    #except FileNotFoundError:
    #    st.warning("Die Datei 'Grundlagenpraktika.csv' wurde nicht gefunden. Es wird ein leerer DataFrame verwendet.")

    # Weiterleitung zur Dashboard-Seite
    nav_page('Dashboard')