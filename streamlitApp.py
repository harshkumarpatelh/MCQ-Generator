import streamlit as st
import json

# loading output json file format
with open('F:/ML/NLP/MCQ-Generator/Response.json','r') as f:
    RESPONSE_JSON = json.load(f)

# creating a title for the app
st.title("Generate MCQ with AI")

with st.form("user_input"):
    st.file_uploader("upload pdf or text")

    number = st.number_input("Number of MCQ",min_value = 3, max_value = 50)
    subject = st.text_input("Write subject", max_chars = 20)
    tone = st.text_input("Comlexity level of Questions", max_chars = 20, placeholder = 'Simple')
    button = st.form_submit_button("Create MCQ")