import streamlit as st

st.title("Programing Languages")
st.subheader("Hey please pick your fav. programing language. :")
lang = st.selectbox("Select which one.",['C','C++','Python','Java'])
st.text(f"Hey you selected {lang} that is good programing language.")
st.success("Great!!😇")