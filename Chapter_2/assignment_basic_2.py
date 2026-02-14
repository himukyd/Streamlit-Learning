import streamlit as st 
from datetime import date

st.header("Calculate your age")
st.subheader("Hey!!")
name =st.text_input("Enter your name :")
st.write(f"Hey {name} welcome to our age calculator app.")
dob= st.date_input("Enter you DOB :")
curr_date = date.today()

if dob:
    age = curr_date.year - dob.year - (
        (curr_date.month, curr_date.day) < (dob.month, dob.day)
    )
    
    st.success(f"{name}, you are {age} years old 🎉")