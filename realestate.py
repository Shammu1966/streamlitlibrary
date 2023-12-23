# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 20:34:48 2023

@author: SharPrash
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import streamlit as st


st.title('Real Estate Data in Mumbai ')


##DATE_COLUMN = 'date/time'
# load data
DATA_URL="file1.csv"


@st.cache_data



def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
 #   data['Date'] = pd.to_datetime(data['Date'],errors='coere')
#    data["date"] = data["date"].astype("datetime64")
    return data




 

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')


if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Date wise ')
#hist_values = np.histogram(data["date"].date.year, bins=24, range=(0,12))[0]
hist_values = np.histogram(data['pin'], bins=5 ,range=(0,500000))[0] 
st.bar_chart(hist_values)

# Some number in the range 0-23
#hour_to_filter = st.slider('noofdays', 0, 120, 5)
#filtered_data = data[data['noofdays'] == hour_to_filter]

hour_to_filter = st.slider('pin', 0, 400000, 1)
filtered_data = data[data['pin'] == hour_to_filter]

st.subheader('Map ')
st.map(filtered_data)
