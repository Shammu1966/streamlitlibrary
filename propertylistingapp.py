# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 11:44:40 2023

@author: SharPrash
"""


import streamlit as st
import time
import datetime
from streamlit.logger import get_logger

#from SessionState import _get_state
LOGGER = get_logger(__name__)

#state = _get_state()

def run():
   # st.set_page_config(
        page_title="Property Listing Entry and Graphs"
   #    )
    

st.write("Property Listing Entry and Graphs")

st.sidebar.success("Select from Below")

st.markdown(
        """
        ### Property Page Entry
        """
    )



# Using object notation
with st.sidebar.form("my_form"):
  add_selectbox = st.sidebar.selectbox(
    "What do you want to Do Now ?",
    ("Choice From Below ","Add Property Listing", "View Listing", "Modify Listing")
  )

# Using "with" notation
  with st.sidebar:
    add_radio = st.radio(
        "Show Property from below",
        ("Latest (5 days)", "Last 15 days)", "Last 1 Month Old", "More than One Month")
    )

    with st.sidebar:
       st.form_submit_button('Submit Selection')



with st.spinner("Loading..."):
       time.sleep(1)
       st.write("")
st.sidebar.success("Done!")

if (add_selectbox=="Add Property Listing"):
    propertylistingform = st.form('my_property_listing')
    
    start_date = propertylistingform.date_input('Enter start date', value=datetime.datetime(2023,12,23))
    area = propertylistingform.text_input('Your Area:', 'Area Please ? : ')
    place = propertylistingform.text_input('Your Place:', 'Place Please ? : ')
    custcode = propertylistingform.text_input('Customer Code : ','Customer Code Please ? : ')
    #"""
    #num = st.number_input("Higher precision step", min_value=1.0, max_value=5.0, step=1e-6, format="%.5f")
    #"""
    expectedcost = propertylistingform.number_input('Likely Expected Cost ? : ')
    totalarea = propertylistingform.number_input('Total Area ? : ')
    measurementin = propertylistingform.selectbox('Measurement In ', ['Sq Ft','Meter','Inches','Cms'])
    typeofprop = propertylistingform.selectbox('Property Type', ['Flat','Bunglow','Twin Bunglow','Raw House','Land'])
    subtypeprop = propertylistingform.selectbox('Sub Property Type', ['1 BHK','2 BHK','3 BHK','4 BHK','5 BHK or More','None'])
    trantype = propertylistingform.selectbox('Transaction Type ', ['Buy','Sell','Rent','Leased ','Hire Purchase','Bank Dealing','None'])
    desc1 =  propertylistingform.text_area('Description : 1 : ')
    desc2 =  propertylistingform.text_area('Description : 2 : ')
    status1 = propertylistingform.selectbox('Status Type', ['OPEN','Appointment on','None'])
    status_date = propertylistingform.date_input('Enter status date', value=datetime.datetime(2023,12,23))
   
    submit = propertylistingform.form_submit_button('Accept Data')
   
    if submit:
       propertylistingform.subheader('Saving Data')
    else:
       propertylistingform.subheader('&nbsp;')
    
#state.sync()    
    
if __name__=="__main__":
   run()