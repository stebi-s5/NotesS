import streamlit as st
import pandas as pd
from functions.notenrechner import manage_pruefungen
from functions.notenrechner import schnitt_modulgruppe
from functions.notenrechner import modulgruppen
from functions.notenrechner import grundlagenpraktikum
from functions.notenrechner import grundlagenpraktika
from functions.notenrechner import trennlinie_duenn
from functions.notenrechner import trennlinie_stark
from functions.notenrechner import display_sidebar
from utils.data_manager import DataManager

# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('pages/Login.py') 
# ====== End Login Block ======

st.title('Modulgruppen-Uebersicht')

display_sidebar()

data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Institution/kestmo_App")  # switch drive 
data_manager.load_user_data(
        session_state_key='Pruefungen', 
        file_name='Pruefungen.csv', 
        initial_value=pd.DataFrame(),
        parse_dates=['timestamp']
    )


semesters = ['Herbstsemester 1', 'Fruehlingssemester 1', 
             'Herbstsemester 2', 'Fruehlingssemester 2', 
             'Herbstsemester 3', 'Fruehlingssemester 3']

if 'semester' not in st.session_state:
    st.session_state.semester = semesters[0]

semester = st.selectbox('Wähle das Semester', semesters, index=semesters.index(st.session_state.semester))

if semester != st.session_state.semester:
    st.session_state.semester = semester
    st.rerun()



if semester == 'Herbstsemester 1':
    tab1, tab2, tab3, tab4 = st.tabs(['Basiswissen BMLD 1', 'Wissenschaftliche Grundlagen 1', 'Sprache', 'Grundlagenpraktikum 1'])

    with tab1:
        schnitt_modulgruppe(modulgruppen, 'Basiswissen BMLD 1' )
        
        trennlinie_stark()

        manage_pruefungen(
            fach_name='Gesundheitsdaten',
            session_state_key='pruefungen_geda',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
  
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Hämatologie und Hämostaseologie 1',
            session_state_key='pruefungen_hähä1',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])

        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Medizinische Mikrobiologie 1',
            session_state_key='pruefungen_memi1',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])

        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Systemerkrankungen',
            session_state_key='pruefungen_sys',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])


    with tab2:
        schnitt_modulgruppe(modulgruppen, 'Wissenschaftliche Grundlagen 1' )
    
        trennlinie_stark()

        manage_pruefungen(
            fach_name='Biologie 1',
            session_state_key='pruefungen_bio1',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()   

        manage_pruefungen(
            fach_name='Chemie 1',
            session_state_key='pruefungen_che1',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Informatik 1',
            session_state_key='pruefungen_inf1',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Mathematik 1',
            session_state_key='pruefungen_mat1',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
    

    with tab3:
        schnitt_modulgruppe(modulgruppen, 'Sprache' )
        
        trennlinie_stark()

        manage_pruefungen(
            fach_name='Englisch 1',
            session_state_key='pruefungen_eng1',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])

        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Gesellschaftlicher Kontext und Sprache 1',
            session_state_key='pruefungen_gks1',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])



    with tab4:
        grundlagenpraktikum(grundlagenpraktika, 'Grundlagenpraktikum 1')


elif semester == 'Fruehlingssemester 1':
    tab1, tab2, tab3 = st.tabs(['Basiswissen BMLD 2', 'Wissenschaftliche Grundlagen 2', 'Grundlagenpraktikum 2'])

    with tab1:
        schnitt_modulgruppe(modulgruppen, 'Basiswissen BMLD 2' )
        
        trennlinie_stark()

        manage_pruefungen(
            fach_name='Hämatologie und Hämostaseologie 2',
            session_state_key='pruefungen_hähä2',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Histologie und Zytologie 1',
            session_state_key='pruefungen_histo1',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Klinische Chemie und Immunologie 1',
            session_state_key='pruefungen_kci1',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])

        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Medizinische Mikrobiologie 2',
            session_state_key='pruefungen_memi2',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])


    
    with tab2:
        schnitt_modulgruppe(modulgruppen, 'Wissenschaftliche Grundlagen 2' )
        
        trennlinie_stark()

        manage_pruefungen(
            fach_name='Biologie 2',
            session_state_key='pruefungen_bio2',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Chemie 2',
            session_state_key='pruefungen_che2',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Informatik 2',
            session_state_key='pruefungen_inf2',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Mathematik 2',
            session_state_key='pruefungen_mat2',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])

        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Physik',
            session_state_key='pruefungen_phy',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
    
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Englisch 2',
            session_state_key='pruefungen_eng2',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Gesellschaftlicher Kontext und Sprache 2',
            session_state_key='pruefungen_gks2',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])

    with tab3:
        grundlagenpraktikum(grundlagenpraktika, 'Grundlagenpraktikum 2')


if semester == 'Herbstsemester 2':
    tab1, tab2, tab3 = st.tabs(['Analyseprozesse & Labordiagnostik 1', ' Analyse Prozesse & Labordiagnostik 2', ' Externes Praktikum'])

    with tab1:
        schnitt_modulgruppe(modulgruppen, 'Analyseprozesse und Labordiagnostik 1' )
        
        trennlinie_stark()

        manage_pruefungen(
            fach_name='Klinische Chemie und Immunologie 2',
            session_state_key='pruefungen_kci2',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
  
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Histologie und Zytologie 2',
            session_state_key='pruefungen_histo2',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])

        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Immunhämatologie und Transfusionsmedizin 1',
            session_state_key='pruefungen_iht1',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])


    with tab2:
        schnitt_modulgruppe(modulgruppen, 'Analyseprozesse und Labordiagnostik 2' )
    
        trennlinie_stark()

        manage_pruefungen(
            fach_name='Herz-Kreislauf- und respiratorische Erkrankungen',
            session_state_key='pruefungen_hkr',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Neoplasien und hämatologische Erkrankungen',
            session_state_key='pruefungen_neopla',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Selbst- und patientennahe Diagnostik',
            session_state_key='pruefungen_spd',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Hygiene und Epidemiologie',
            session_state_key='pruefungen_hyep',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
            
    
    with tab3:
        grundlagenpraktikum(grundlagenpraktika, 'Externes Praktikum Fachbereich A')


if semester == 'Fruehlingssemester 2':
    tab1, tab2 = st.tabs(['Analyseprozesse & Labordiagnostik 3', ' Externe Praktika'])

    with tab1:
        schnitt_modulgruppe(modulgruppen, 'Analyseprozesse und Labordiagnostik 3' )
        
        trennlinie_stark()

        manage_pruefungen(
            fach_name='Immunhämatologie und Transfusionsmedizin 2',
            session_state_key='pruefungen_iht2',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
  
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Medizinische Genetik 1',
            session_state_key='pruefungen_gen1',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Bewegungsapparat und neurologische Erkrankungen',
            session_state_key='pruefungen_bene',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Endokrinologie, Stoffwechselerkrankungen',
            session_state_key='pruefungen_endo',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
    with tab2:
        grundlagenpraktikum(grundlagenpraktika, 'Externes Praktikum Fachbereich B')
        grundlagenpraktikum(grundlagenpraktika, 'Externes Praktikum Fachbereich C')
        grundlagenpraktikum(grundlagenpraktika, 'Praxisreflexion und interprofessionelles Handeln')


if semester == 'Herbstsemester 3':
    tab1, tab2, tab3, tab4 = st.tabs(['Analyseprozesse & Labordiagnostik 4', 'Kommunikation und Management 1', 'Angewandte Forschung', 'Gesellschaft, Kultur und Gesundheit'])
    
    with tab1:
        schnitt_modulgruppe(modulgruppen, 'Analyseprozesse und Labordiagnostik 4' )
        
        trennlinie_stark()

        manage_pruefungen(
            fach_name='Medizinische Genetik 2',
            session_state_key='pruefungen_gen2',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Urogenitale und gastrointestinale Erkrankugnen',
            session_state_key='pruefungen_uro',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Entwicklungsstörungen und vererbbare Erkrankungen',
            session_state_key='pruefungen_entw',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
    with tab2:
        schnitt_modulgruppe(modulgruppen, 'Kommunikation und Management 1' )
        
        trennlinie_stark()

        manage_pruefungen(
            fach_name='Projekt-, Change- und Risikomanagement 1',
            session_state_key='pruefungen_pcr1',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()    

        manage_pruefungen(
            fach_name='Kommunikation 1',
            session_state_key='pruefungen_kom1',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Evidenzbasiertes Handeln',
            session_state_key='pruefungen_ebh',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Entwicklungen, Trends, Unternehmertum',
            session_state_key='pruefungen_etu',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Gesundheitsförderung und Prävention',
            session_state_key='pruefungen_gepr',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
    with tab3:
        schnitt_modulgruppe(modulgruppen, 'Angewandte Forschung' )
        
        trennlinie_stark()

        manage_pruefungen(
            fach_name='Projektarbeit',
            session_state_key='pruefungen_proj',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Forschungsmethoden 1',
            session_state_key='pruefungen_fors1',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
    with tab4:
        grundlagenpraktikum(grundlagenpraktika, 'Gesellschaft, Kultur und Gesundheit')
        st.markdown('*Einzelne Module nicht bekannt!*')
        
if semester == 'Fruehlingssemester 3':
    tab1, tab2, tab3 = st.tabs(['Gesundheitssystem', 'Kommunikation und Management 2', 'Bachelorarbeit'])

    with tab1:
        schnitt_modulgruppe(modulgruppen, 'Gesundheitssystem' )

        trennlinie_stark()

        manage_pruefungen(
            fach_name='Klinische Pharmakologie und personalisierte Medizin',
            session_state_key='pruefungen_pharma',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Gesundheitssystem und Digital Health',
            session_state_key='pruefungen_gedh',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
    
    with tab2:
        schnitt_modulgruppe(modulgruppen, 'Kommunikation und Management 2' )

        trennlinie_stark()

        manage_pruefungen(
            fach_name='Projekt-, Change- und Risikomanagement 2',
            session_state_key='pruefungen_pcr2',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Forschungsmethoden 2',
            session_state_key='pruefungen_fors2',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])

        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Kommunikation 2',
            session_state_key='pruefungen_kom2',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])

    with tab3:
        manage_pruefungen(
            fach_name='Bachelorarbeit',
            session_state_key='pruefungen_ba',
            spalten=['Pruefung', 'Datum', 'Gewichtung', 'Note'])
        

