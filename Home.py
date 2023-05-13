import streamlit as st
import os
import openai 

# get the value of the environment variable named "HOME"
openai.apikey = os.getenv("OPENAI_APIKEY")
st.write("Hello world")
name = st.text_input("Enter your name: ")
if name:
    st.write(name) 
