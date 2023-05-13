import streamlit as st
import os
import openai 

# get the value of the environment variable named "HOME"
openai.api_key = os.getenv("OPENAI_API_KEY")
st.write("Hello world")
name = st.text_input("Enter your name: ")
if name:
    st.write(name) 
