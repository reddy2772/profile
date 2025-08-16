import streamlit as st
name = st.text_input("User name: ")
marks = st.number_input("User marks:", min_value=0, max_value=100, step=1)
st.write(f"Hi {name}, you scored {marks} marks.")