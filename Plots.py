import folium
from streamlit_folium import folium_static
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import ast


class Plot:
    @staticmethod
    def howManyBicycleLanes(df):
        # Print the number of bicycle lane in Paris
        # Add an anchor tag for the section
        st.markdown('<a id="how-many-bicycle-lane"></a>', unsafe_allow_html=True)
        st.header('How many bicycle lane are there in Paris ?')
        st.markdown(
            f'<p style="color: lightcoral; font-size: 100px; font-weight: bold; display : inline">{df.shape[0]}</p> Bicycle lane exists in Paris.',
            unsafe_allow_html=True)

        # Map of Paris with all the bicycle lanes
        # Add an anchor tag for the section
        st.markdown('<a id="Map-Visualization"></a>', unsafe_allow_html=True)
        st.header("Here is the map visualization")

        # Bouton to show the map of Paris

        # Create a map centered on Paris
        m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

        # Display the map
        if st.button('Click to see map of bicycle itineraries in Paris'):
            Plot.add_cycle_routes_to_map(df, m)
            folium_static(m)
            st.markdown("""
                <style>
                    .legend-container {
                        position: fixed;
                        bottom: 50px;
                        left: 50px;
                        padding: 10px;
                        background-color: white;
                        border: 2px solid grey;
                        z-index: 9999;
                    }
                    .legend-title {
                        font-weight: bold;
                        margin-bottom: 5px;
                    }
                    .legend-item {
                        display: flex;
                        align-items: center;
                    }
                    .legend-icon {
                        width: 20px;
                        height: 5px;  /* Adjust the height to resemble a line */
                        margin-right: 5px;
                        background-color: blue;
                    }
                </style>
            """, unsafe_allow_html=True)

            # Add the legend
            st.markdown('<div class="legend-container">', unsafe_allow_html=True)
            st.markdown('<div class="legend-title">Legend</div>', unsafe_allow_html=True)
            st.markdown('<div class="legend-item"><div class="legend-icon"></div> Cycle Routes</div>',
                        unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # Function to add cycling routes to the map
    @staticmethod
    def add_cycle_routes_to_map(df, m):
        # Add the cycling routes to the map
        for index, row in df.iterrows():
            # Convert the string representation of the coordinates into a list of floats
            coordinates = ast.literal_eval(row['geo_shape'])['coordinates']
            # Create a list of coordinate pairs
            coordinates = [[coord[1], coord[0]] for coord in coordinates]
            # Create a polyline from the coordinate pairs
            polyline = folium.PolyLine(locations=coordinates, color='blue')
            # Add the polyline to the map
            polyline.add_to(m)

    @staticmethod
    def typesOfItineraries(df):
        # Repartition of the different itineraries #
        # Add an anchor tag for the section
        st.markdown('<a id="Common-Types-Of-Itineraries"></a>', unsafe_allow_html=True)
        st.header('What are the most common type of itineraries in Paris ?')
        typology_counts = df['typologie_simple'].value_counts()
        # Create a pie chart using Plotly
        fig = px.pie(typology_counts, values=typology_counts.values, names=typology_counts.index,
                     title='Repartition of itinerary by typology')
        # Display the graph in streamlit
        st.plotly_chart(fig)

    @staticmethod
    def itineraryLength(df):
        # Itinerary length according to arrondissement #

        # Add an anchor tag for the section
        st.markdown('<a id="Itinerary-Length-According-To-Arrondissement"></a>', unsafe_allow_html=True)
        st.header('Which districts have the longest itinerary ?')
        # Calculate the total length per arrondissement
        length_by_arrondissement = df.groupby('arrdt')['length'].sum().sort_values().reset_index()

        # Create an interactif horizontal bar plot using Plotly Express
        fig = px.bar(
            length_by_arrondissement,
            x='length',
            y='arrdt',
            orientation='h',
            title='Total length of bike itinerary by district'
        )

        # Display on streamlit
        st.plotly_chart(fig, use_container_width=True)

    @staticmethod
    # Get the coordinates of the first point of each itinerary
    def get_first_point(filtered_data):
        new_data = filtered_data.copy()  # Create a copy of the DataFrame to avoid side effects
        new_data['latitude'] = filtered_data['geo_shape'].apply(
            lambda x: ast.literal_eval(x)['coordinates'][0][1] if pd.notnull(x) else None)
        new_data['longitude'] = filtered_data['geo_shape'].apply(
            lambda x: ast.literal_eval(x)['coordinates'][0][0] if pd.notnull(x) else None)
        return new_data

    @staticmethod
    def visPerArrdt(df):
        # Add an anchor tag for the section
        st.markdown('<a id="Visualization-Of-The-Different-Routes-According-To-The-Arrondissement"></a>',
                    unsafe_allow_html=True)
        st.header('What are the most common type of itinerary by district ?')
        # Convert 'arrdt' in int and sort them in growing order
        arrondissements_sorted = sorted(df['arrdt'].unique(), key=lambda x: int(x))
        # Select a district
        selected_zone = st.selectbox('Select a district', arrondissements_sorted)
        # Filter the data according to the selected district
        filtered_data = df[df['arrdt'] == selected_zone]


        # Create a map centered on the selected district
        fig = px.scatter_mapbox(
            Plot.get_first_point(filtered_data),
            lat='latitude',  # Modifier 'lat' en 'latitude'
            lon='longitude',  # Laisser 'lon' comme 'longitude'
            color='typologie_simple',
            hover_name='typologie_simple',
            zoom=12,
        )

        # Update the layout to display the map
        fig.update_layout(mapbox_style='carto-positron')
        fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
        # Display the map
        st.plotly_chart(fig, use_container_width=True)

        return filtered_data

    @staticmethod
    def percentageItineraries(filtered_data):
        # Add an anchor tag for the section
        st.markdown('<a id="Percentage-Of-Each-Type-Of-Itinerary-In-The-Selected-District"></a>', unsafe_allow_html=True)
        st.header('Percentage of each type of itinerary in the selected district')
        # Calculate the percentage of each type of itinerary
        typology_counts = filtered_data['typologie_simple'].value_counts(normalize=True)
        # Create a bar plot using streamlit
        st.bar_chart(typology_counts, color='#FFC0CB')

    @staticmethod
    def evolutionRoutesNetwork(df):
        # Add an anchor tag for the section
        st.markdown('<a id="Evolution-Of-The-Routes-Network-Throughout-The-Years"></a>', unsafe_allow_html=True)
        st.header('When were cyclable itineraries added ?')
        # Select a year to filter the data
        selected_year = st.slider('Select a year', min_value=df['date_de_livraison'].min().year,
                                  max_value=df['date_de_livraison'].max().year)
        # Filter the data according to the selected year
        filtered_data = df[df['date_de_livraison'].dt.year == selected_year]

        # Create an interactif bar plot using Plotly Express
        fig = px.bar(filtered_data, x='date_de_livraison', y='length',
                     title='Creation of new bicycle itineraries according to time',
                     labels={'date_de_livraison': 'Year', 'length': 'Total length'})
        st.plotly_chart(fig, color='#FFC0CB')

    @staticmethod
    def lengthItineraries(df):
        # Add an anchor tag for the section
        st.markdown('<a id="Length-Of-Itineraries"></a>', unsafe_allow_html=True)
        st.header('How long are most itineraries ?')

        # Select a length range
        min_length, max_length = st.slider('Select a length (in km)', float(df['length'].min()), float(df['length'].max()), (float(df['length'].min()), float(df['length'].max())))

        # Filter the data according to the selected length range
        filtered_data = df[(df['length'] >= min_length) & (df['length'] <= max_length)]

        # Create a histogram using matplotlib
        fig, ax = plt.subplots()
        ax.hist(filtered_data['length'], bins=20, edgecolor='black', linewidth=1.2)
        ax.set_xlabel('Itineraries length (km)')
        ax.set_ylabel("Number of itineraries")
        ax.set_title('Repartition of itineraries length')
        st.pyplot(fig)

    @staticmethod
    def StatusRoads(df):
        # Add an anchor tag for the section
        st.markdown('<a id="Status-Of-Itineraries"></a>', unsafe_allow_html=True)
        st.header('What are the most common status for itineraries ?')

        # Calculate the number of itineraries for each status
        status_counts = df['statut'].value_counts()
        # Create a bar plot using streamlit
        st.bar_chart(status_counts, color='#FFC0CB')