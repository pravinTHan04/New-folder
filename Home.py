import streamlit as st
st.write("Hello world")
name = st.text_input("Enter your name: ")
if name:
    st.write(name) 
