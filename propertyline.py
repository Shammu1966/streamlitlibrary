# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 22:56:17 2023

@author: SharPrash
"""

import  streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
st.title('Real Estate System')
DATE_COLUMN = 'date'
##DATA_URL=('./propertylisting_17122023.csv')
DATA_URL=('file1.csv')

@st.cache_data  
def load_data(nrows):
    data=pd.read_csv(DATA_URL,nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase,axis='columns',inplace=True)
    pd.to_datetime(data[DATE_COLUMN]) 
    return data 



#data loading
data_load_state = st.text('loading data') 
#load 10000 records
data=load_data(10000)
data_load_state.text('Done')
if (st.checkbox('Show Property Basic Data ')): 
    st.subheader('Row Data') 
    st.write(data)
    

st.subheader('Date Wise Listing')
##hist_values = np.histogram(data)
#hist_values = np.histogram(data["date"].date.year, bins=24, range=(0,12))[0]
hist_values = np.histogram(data["date"].date.month, bins=12 ,range=(0,12))[0] 
st.bar_chart(hist_values)