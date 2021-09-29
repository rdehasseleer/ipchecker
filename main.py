import time

import folium
import matplotlib.pyplot as plt
import pandas as pd
import plotly.figure_factory as ff
import requests
import streamlit as st
from streamlit_folium import folium_static
import numpy as np


st.title("IP Checker")


def check_ip(ip):
    api = "https://ipqualityscore.com/api/json/ip/"+st.secrets['KEY']+"/"+ip
    response = requests.get(api).json()
    return str(response['vpn']), response['latitude'], response['longitude']



uploaded_file = st.sidebar.file_uploader('Upload your spreadsheet')
if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        data = pd.read_csv(uploaded_file)
    else:
        data = pd.read_excel(uploaded_file)
    IP_COLUMN = st.sidebar.selectbox('Column with the IP', data.columns)
    if(len(data.columns)==1):
        data['IP'] = data[IP_COLUMN]
    if IP_COLUMN is not None:
      
        data['VPN'] = "False"
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        markers = []
        for i, value in  data.iterrows():
            # Update progress bar.
            progress_bar.progress(int(100 * i / (len(data)-1)))

            value['VPN'],lat,lon = check_ip(value['IP'])
            markers.append([lat,lon])
        st.table(data)
        st.balloons()
        with st.echo():
            # center on Liberty Bell
            m = folium.Map(location=[48.86, 2.32], zoom_start=8)

            # add marker for Liberty Bell
            tooltip = "Liberty Bell"
            for marker in markers:

                folium.Marker(
                    [marker[0], marker[1]], popup="Liberty Bell", tooltip=tooltip
                ).add_to(m)

            # call to render Folium map in Streamlit
            folium_static(m)
