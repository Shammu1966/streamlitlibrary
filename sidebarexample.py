# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 00:15:26 2023

@author: SharPrash
"""


import streamlit as st
import time
from streamlit.logger import get_logger

#from SessionState import _get_state
LOGGER = get_logger(__name__)

#state = _get_state()

def run():
   # st.set_page_config(
        page_title="Property Listing Entry and Graphs"
   #    )
    

st.write(" ")

st.sidebar.success("Select from Below")

st.markdown(
        """
        ### Property Page Entry
        """
    )



# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

with st.sidebar:
  #  with st.echo():
         st.write("You have selected ")
         st.write(add_selectbox)
         st.write("you have selected ")
         st.write(add_radio)

with st.spinner("Loading..."):
       time.sleep(1)
       st.write("")
st.sidebar.success("Done!")
    
#state.sync()    
    
if __name__=="__main__":
   run()