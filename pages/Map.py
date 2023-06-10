import streamlit as st
import folium
import pandas as pd
from streamlit_folium import folium_static
from folium import Marker
from folium import plugins
from folium.plugins import MarkerCluster 
st.set_page_config(page_title='EV Demand Optimisation')
st.header('EV Demand over India')
json1 = f"india.geojson"


# st.sidebar.header("Select Data:")
# city = st.sidebar.multiselect(
#     "Select the City:",
#     options=df["City"].unique(),
#     # default=df["City"].unique()
# )

m = folium.Map(location=[23.47,77.94], tiles='CartoDB positron', name="Light Map",
               zoom_start=4, attr="My Data attribution")

india_ev = f"ev_data.csv"
india_ev_data = pd.read_csv(india_ev)

choice = ['vehicle count']
choice_selected = st.selectbox("Select choice", choice)

folium.Choropleth(
    geo_data=json1,
    name="choropleth",
    data=india_ev_data,
    columns=["state_code",choice_selected],
    key_on="feature.properties.state_code",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=.1,
    legend_name=choice_selected
).add_to(m)
folium.features.GeoJson('india.geojson',name="States", popup=folium.features.GeoJsonPopup(fields=["st_nm"])).add_to(m)
folium_static(m, width=800, height=500)

# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)


############
ev_stations_df = pd.read_csv('coordinate2.csv')
ev_stations_df.head()

ev_stations_df['x_cor'] = ev_stations_df['x_cor'] 
ev_stations_df['y_cor'] = ev_stations_df['y_cor'] 


map = folium.Map(location=[26.850000,80.949997], tiles='openstreetmap', zoom_start=8)

# Add points to a marker cluster
mc = MarkerCluster()
for idx, row in ev_stations_df.iterrows():
    mc.add_child(Marker(location=[row['x_cor'], row['y_cor']],popup=int(row['charging_ports'])))

# add the marker cluster to the map
map.add_child(mc)

# Display the map
folium_static(map, width=800, height=500)


########

import math
coord_list = [(lat, lon) for lat, lon in zip(ev_stations_df['x_cor'], ev_stations_df['y_cor']) if not math.isnan(lat) and not math.isnan(lon)]
z = folium.Map(location=(26.850000,80.949997), tiles="Cartodb dark_matter", zoom_start=7)
plugins.HeatMap(coord_list, radius=20).add_to(z)
folium_static(z, width=800, height=500)