
import streamlit as st


class menu:

    @staticmethod
    def createmenu():
        st.sidebar.title('🚲🇫🇷Menu🇫🇷🚲')
        st.sidebar.markdown("""
        - [Project description](#project-description-)
        - [How many bicycle lane are there in Paris ?](#how-many-bicycle-lane)
        - [Map Visualization](#Map-Visualization)
        - [What are the most common type of itinerary in Paris ?](#Common-Types-Of-Itineraries)
        - [Itinerary length according to arrondissement](#Itinerary-Length-According-To-Arrondissement)
        - [Visualization of the different routes according to the arrondissement](#Visualization-Of-The-Different-Routes-According-To-The-Arrondissement)
        - [Percentage of each type of itinerary in the selected district](#Percentage-Of-Each-Type-Of-Itinerary-In-The-Selected-District)
        - [When were cyclable itineraries added ?](#Evolution-Of-The-Routes-Network-Throughout-The-Years)
        - [How long are most itineraries ?](#Length-Of-Itineraries)
        - [What are the most common status for itineraries ?](#Status-Of-Itineraries)
        """)
        st.sidebar.markdown('<p style="color: lightcoral; font-size: 40px; font-weight: bold; display : inline"> #datavz2023efrei </p>', unsafe_allow_html=True)
        st.sidebar.write('My name is Capucine Foucher, I am a student in Business Analytics and Business Intelligence at EFREI Paris. In the context of the course Data Visualization, I have created this dashboard to inform on the possibel commute in bicycle. I hope you will enjoy it !')
