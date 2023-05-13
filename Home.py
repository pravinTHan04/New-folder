import streamlit as st
import openai 
import os

# Set up the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define a function to generate text using the OpenAI API
def generate_text(prompt):
    response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )
    return response.choices[0].text

# Set up the Streamlit app
st.title("OpenAI GPT-3 Text Generation")
name = st.text_input("Enter your name: ")
if st.button("Generate Text"):
    with st.expander("Generated Text"):
        if name:
            text = generate_text(name)
            st.write(text)
        else:
            st.write("Please enter a name.")
