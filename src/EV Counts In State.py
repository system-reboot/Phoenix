import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='EV Demand Optimisation')
st.header('Survey Results 2021')


df = pd.read_csv('ev_data.csv')


k= pd.read_csv('perc.csv')

# --- PLOT BAR CHART
bar_chart = px.bar(k,
                   x='State',
                   y='vehicle count',
                   text='vehicle count',
                   color_discrete_sequence = ['#F63366']*len(k),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)


# --- PLOT PIE CHART
pie_chart = px.pie(k,
                title='Total No. of Participants',
                values='vehicle count',
                names='State')

st.plotly_chart(pie_chart)