import streamlit as st

st.title("HIMANSHU")
st.header("IIT Bhilai")
st.subheader("Graphic Era University Dehradun.")
st.text("Hi my name is Himanshu and curently pursuing maste's in mathematic and computing at IIT Bh and did Bachlours" \
" from Graphic Era University Dehradun.")

st.subheader("Curently Looking for Job in relevent fields.")
select = st.selectbox("Your dream job in what field :" , ["Data Scientist","ML eng.","AI engg.","Soft engg."])
st.write(f"You selected your dream job {select} .")
