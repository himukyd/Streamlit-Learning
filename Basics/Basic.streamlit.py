import streamlit as st

st.title("Hello Himanshu 👋")
st.write("This is my first Streamlit app!")

number = st.slider("Select a number", 0, 100)
st.write("You selected:", number)
