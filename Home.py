import streamlit as st
import os
import openai 

# get the value of the environment variable named "HOME"
openai.api_key = os.getenv("OPENAI_API_KEY")
st.write("Hello world")
name = st.text_input("Enter your name: ")
btn = st.button("sent")
if btn:
    st.write(name) 
    response = openai.Completion.create(
                model="text-davinci-003",
                prompt=name,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )
    st.write(response)
