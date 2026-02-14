import streamlit as st

st.title("Chai Maker App")
if st.button("Make Chai"):
    st.success("Your cahin is being brew.")

add_masala = st.checkbox("Want to add massala in your tea")

if add_masala :
    st.success("Massala is added in your tea.")

tea_type = st.radio("Pick your tea base :", ["Water","Milk","Honey","Sugar"])

st.write(f"you choose your tea base is :{tea_type}")

tea_flavour = st.selectbox("Chhose your tea flover",["Adrak","Masala","coldtea"])

st.write(f"your tea flover is :{tea_flavour}")

sugar_spoon = st.slider("Sugar lavel in your tea.",0,10,2)
st.write(f"{sugar_spoon} spoon of sugar added in your tea.")

cups = st.number_input("How many no. of teacups you wants.", min_value=1,max_value=10)
st.text(f"Hey! your {cups} cups of tea orderd.")

name = st.text_input("Enter your name :")

if name :
    st.success(f"Hey! {name} you tea is on the way.")

dob = st.date_input("Enter your DOB.")
st.write(f"Your DOB is :{dob}.")