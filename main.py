import time
import math 
import folium
import matplotlib.pyplot as plt
import pandas as pd
import plotly.figure_factory as ff
import requests
import streamlit as st
from streamlit_folium import folium_static
import numpy as np
from ipinfo import IPInfo
import statistics
st.title("IP Checker")


def check_ip(ip):
    api = "https://ipqualityscore.com/api/json/ip/"+st.secrets['KEY']+"/"+ip
    response = requests.get(api).json()
    return response


uploaded_file = st.sidebar.file_uploader('Upload your spreadsheet')
if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        data = pd.read_csv(uploaded_file)
    else:
        data = pd.read_excel(uploaded_file)
    IP_COLUMN = st.sidebar.selectbox('Column with the IP', data.columns)
    if(len(data.columns) == 1):
        data['IP'] = data[IP_COLUMN]
    if IP_COLUMN is not None:

        data['VPN'] = "False"

        progress_bar = st.progress(0)
        status_text = st.empty()
        markers = []
        for i, value in data.iterrows():
            # Update progress bar.
            progress_bar.progress(int(100 * i / (len(data)-1)))

            response = check_ip(value['IP'])
            ipinfo = IPInfo(response)
            value['VPN'], lat, lon = ipinfo.vpn, ipinfo.latitude, ipinfo.longitude
            markers.append([lat[0], lon[0], ipinfo.get_location()])
        st.table(data)
        st.balloons()
        avg_lat =  statistics.mean([lat for lat, lon, dest in markers])
        avg_lon =  statistics.mean([lon for lat, lon, dest in markers])
        # center on Liberty Bell
        m = folium.Map(location=[avg_lat,avg_lon], zoom_start=4)

        # add marker for Liberty Bell
        st.title("IP Map")
        tooltip = "Liberty Bell"
        for marker in markers:
            folium.Marker(
                [marker[0], marker[1]], popup=marker[2], tooltip=marker[2]
            ).add_to(m)

        # call to render Folium map in Streamlit
        folium_static(m)
