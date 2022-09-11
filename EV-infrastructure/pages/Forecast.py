import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
sns.set_theme()
import base64
# import streamlit as st  
# read csv from a github repo
df = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")
demand_data = pd.read_csv('isme_supply_ka_index hai.csv')
existing_ev = pd.read_csv('exisiting_EV_infrastructure_2018.csv')
n_df = pd.read_csv('New_to_feed.csv')
# n_df.columns = ['demand_point_index', 'x_coordinate', 'y_coordinate', '2016', '2017',
#        '2018', '2019', '2020', '2021', '2022', '2023', '2025',
#        'demand_point_index', 'x_coordinate', 'y_coordinate',
#        'supply_point_ka_index']
st.set_page_config(
    page_title = 'Real-Time Visualization',
    page_icon = '✅',
    layout = 'wide'
)

# dashboard title

st.title("Real-Time Visualization of the Predicted EV Charging Points Demand Dashboard")

# top-level filters 
list1 = np.array([2019,2020,2021,2022,2023])
job_filter = st.selectbox("Select the Year", list1)
print(job_filter)

# creating a single-element container.
placeholder = st.empty()
# Get some data
df1 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')



# dataframe filter 

df = df[df['job']==job_filter]
job_f = str(job_filter)
list1 = []
for i in range(100):
    list1.append((n_df[n_df['supply_point_ka_index']==i][job_f].sum()))
list1 = np.array(list1)
list2 = []
for i in range(100):
    list2.append((n_df[n_df['supply_point_ka_index']==i]['2022'].sum()))
list2 = np.array(list2)
list3 = []
for i in range(100):
    list3.append((n_df[n_df['supply_point_ka_index']==i]['2023'].sum()))
list3 = np.array(list3)
# near real-time / live feed simulation 

for seconds in range(20):

    plt.figure(figsize=(20,20))
    
    with placeholder.container():

        fig_col1, fig_col2 = st.columns(2)
        # with fig_col1:
        #     st.markdown("### First Chart")
        #     fig = px.density_heatmap(data_frame=df, y = 'age_new', x = 'marital')
        #     st.write(fig)
        with fig_col1:
            st.markdown("### Demand at each supply point")
            fig2 = px.line(x=np.arange(0,100),y=list1,labels={'x':"Supply Point",'y':"Total Demand"})
            st.write(fig2)
        with fig_col2:
            st.markdown("#### Classifying the demand points that would get charged from classified charging point")
            fig4 = px.scatter(demand_data, x="x_coordinate", y="y_coordinate",color='supply_point',hover_data=['supply_point'])
            # fig4 = plt.scatter(demand_data,x='x_coordinate',y='y_coordinate')
            # fig5 = px.add_scatter(existing_ev,x="x_coordinate",y="y_coordinate")
            # fig6 = px.scatter(demand_data,y='x_coordinate',x='y_coordinate',hover_data=['supply_point_ka_index'])
            st.write(fig4)
        fig_col4,fig_col5 = st.columns(2)
        with fig_col4:
            st.markdown("### 2023")
            fig8 = px.line(x=np.arange(0,100), y=list2,labels={'x':"Supply Point",'y':"Total Demand"},color_discrete_sequence=["red", "green", "blue", "goldenrod", "magenta"])
            st.write(fig8)
            

        with fig_col5:
            st.markdown("### 2024")
            fig9 = px.line(x=np.arange(0,100),y=list3,labels={'x':"Supply Point",'y':"Total Demand"},color_discrete_sequence=["green", "blue", "goldenrod", "magenta"])
            st.write(fig9)
            # st.write(fig5)
        # st.markdown("### Detailed Data View")
            # st.dataframe(df)
        # fig_col6 = st.columns(1)
        # with fig_col6:
        #     st.markdown("### Compare")
        #     fig = go.Figure()
        #     fig.add_trace(go.Scatter(
        #         x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
        #         y=[0, 1, 2, 3, 4, 5, 6, 7, 8],
        #         name="Name of Trace 1"       # this sets its legend entry
        #     ))
        #     fig.add_trace(go.Scatter(
        #         x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
        #         y=[1, 0, 3, 2, 5, 4, 7, 6, 8],
        #         name="Name of Trace 2"
        #     ))
        #     st.write(fig)
    time.sleep(5)
            #placeholder.empty()

