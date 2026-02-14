import streamlit as st 
import pandas as pd 

st.title("Chai Sales Deshboard")
file = st.file_uploader("Upload your csv file.",type = ["csv"])

if file :
    df = pd.read_csv(file)
    st.subheader("DataPreview")
    st.dataframe(df)
    st.write(df.describe())