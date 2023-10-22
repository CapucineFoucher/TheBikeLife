import folium
from streamlit_folium import folium_static
import ast
import plotly.express as px
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import ast


class Introduction :


    @staticmethod
    def getData(path):
        df = pd.read_csv(path, delimiter=';')  # Assurez-vous de spécifier le bon chemin du fichier CSV
        # Conversion de la colonne 'arrdt' en type str et suppression du '.0'
        df['arrdt'] = df['arrdt'].astype(str).str.split('.').str[0]
        # Filtrer les lignes avec des valeurs invalides dans 'arrdt'
        df = df[df['arrdt'].str.isnumeric()]
        # Convertir la colonne 'date_de_livraison' en type datetime
        df['date_de_livraison'] = pd.to_datetime(df['date_de_livraison'])

        return df


    @staticmethod
    def introduction():

        st.title('🚲🇫🇷The Bike Life🇫🇷🚲')
        st.title('Paris and bicycle itineraries : Is it safe to travel by bike in Paris ?')

        st.markdown('<a id="project-description-"></a>', unsafe_allow_html=True)
        st.header('Project description')

        st.write("""
            This project aims at answering a question : Is it safe to travel by bike in Paris ?
        Either if you are a tourist or a born Parisian maybe you want to commute by bike. I mean, why not ? It is pleasant, it makes you work out, most times it is even quicker than public transit or cars and it is eco friendly !
        Here is all the information you will need to make sure your bike experience is safe ! Enjoy the bike life ! xx 
        """)

        st.write(""" The data comes from the official website data.gouv. Its been collected throughout the years by the city of Paris.The dataset contains essential information about cycling routes in Paris, including details like route length, geographical coordinates, itinerary type, and more. """)
