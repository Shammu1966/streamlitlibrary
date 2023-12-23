#importing module
import streamlit as st

st.title("Form")
st.subheader("Enter details below")

with st.form("form1",clear_on_submit=True):
  name=st.text_input("Enter Name")
  email=st.text_input("Enter email")
  message=st.text_area("Message")
  age=st.slider("Enter your age",min_value=10,max_value=100)
  st.write(age)

  submit=st.form_submit_button("Confirm Me")
