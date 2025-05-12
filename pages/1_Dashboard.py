import streamlit as st
import pandas as pd
from functions.notenrechner import display_sidebar

# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('pages/Login.py') 
# ====== End Login Block ======

st.title('Dashboard')

display_sidebar()

#st.sidebar.page_link('Start.py', label='Startseite')
#st.sidebar.page_link('pages/1_Dashboard.py', label='Dashboard')
#st.sidebar.page_link('pages/2_Modulgruppen-Uebersicht.py', label='Modulgruppen-Uebersicht')

semesters = ['Herbstsemester 1', 'Fruehlingssemester 1',
             'Herbstsemester 2', 'Fruehlingssemester 2', 
             'Herbstsemester 3', 'Fruehlingssemester 3']

if 'semester' not in st.session_state:
    st.session_state.semester = semesters[0]

semester = st.selectbox('Wähle das Semester', semesters, index=semesters.index(st.session_state.semester))

if semester != st.session_state.semester:
    st.session_state.semester = semester
    st.rerun()
