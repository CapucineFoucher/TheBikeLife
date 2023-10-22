### Importing librairies ###
import streamlit as st
from Plots import Plot
from Menu import menu
from Introduction import Introduction


# Menu

menu.createmenu()


# Introduction of the project

df = Introduction.getData('reseau-cyclable.csv')

Introduction.introduction()


# Visualizations

Plot.howManyBicycleLanes(df)

Plot.typesOfItineraries(df)

Plot.itineraryLength(df)

filtered_data = Plot.visPerArrdt(df)

Plot.percentageItineraries(filtered_data)

Plot.evolutionRoutesNetwork(df)

Plot.lengthItineraries(df)

Plot.StatusRoads(df)


# Conclusion

st.markdown('<p style="color: lightcoral; font-size: 30px; font-weight: bold; display : inline">🚲 So ? You are going to hop on your bike or what ? 🚲</p>', unsafe_allow_html=True)
