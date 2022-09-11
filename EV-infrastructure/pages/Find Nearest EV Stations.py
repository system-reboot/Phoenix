import streamlit as st
import pandas as pd
import numpy as np
list_users = []
# title = st.text_input('Car Registration Number', 'Car Registration Number')
# title1 = st.text_input('Enter your mobile number','Phone Number')
lat1 = float(st.text_input('Enter your longitude',26.5))
lon1 = float(st.text_input('Enter Your Latitude',82.09))
df = pd.read_csv('coordinates.csv')
df['x_cor'] = df['x_cor']+  26.850000
df['y_cor'] = df['y_cor'] + 80.949995
from math import cos,sin, asin, sqrt, pi,atan2

def distance(lat1, lon1, lat2, lon2):
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a))
lat,lon = df['x_cor'].values,df['y_cor'].values
lon_s = 0
lat_s = 0
def nearest(lat1,lon1,lat_x,lon_y):
    distanc = []
    index1 = []
    for i in range(len(lat)):
        distanc.append(distance(lat1,lon1,lat_x[i],lon_y[i]))
        index1.append(i)
    return distanc,index1
distance1,index1= nearest(lat1,lon1,lat,lon)
dist1 = np.array(distance1)
index1 = dist1.argsort()
lat = lat[index1]
lon = lon[index1]
dist1=dist1[index1]
st.write('Shortest point is at {} kms and its latitude is {} and longitude is {}'.format(int(dist1[0]),lat[0],lon[0]))

#map
import folium
from folium import Marker
from folium.plugins import MarkerCluster 
from streamlit_folium import folium_static
# Create a map centered on North Carolina
nc_map = folium.Map(location=[26.5,81.7628341], tiles='openstreetmap', zoom_start=9)

# Add points to a marker cluster
mc = MarkerCluster()
# for idx, row in NC_locations_df.iterrows():
l1 = list(lat[0:5])
l2 = list(lon[0:5])
for i in range(5):
    mc.add_child(Marker(location=[l1[i],l2[i]]))

icon=folium.map.Icon(color='blue', icon_color='white')
mc.add_child(Marker(location=[lat1, lon1]))
# add the marker cluster to the map
nc_map.add_child(mc)

# Display the map
# nc_map
folium_static(nc_map,width=800,height=500)