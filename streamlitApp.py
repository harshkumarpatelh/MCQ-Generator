import streamlit as st
import json
from langchain.callbacks import get_openai_callback
from src.mcqgenerator.mcqgenerator import generate_evaluate_chain
from src.mcqgenerator.utils import read_file, get_table_data
import traceback
import pandas as pd

# loading output json file format
with open('F:/ML/NLP/MCQ-Generator/Response.json','r') as f:
    RESPONSE_JSON = json.load(f)
# converting file into json format
RESPONSE_JSON = json.dumps(RESPONSE_JSON)

# creating a title for the app
st.title("Generate MCQ with AI")

with st.form("user_input"):
    uploaded_file = st.file_uploader("Upload pdf or text")

    number = st.number_input("Number of MCQ",min_value = 3, max_value = 50)
    subject = st.text_input("Enter subject", max_chars = 20,placeholder = 'Geography')
    tone = st.text_input("Comlexity level of Questions", max_chars = 20, placeholder = 'Simple')
    button = st.form_submit_button("Create MCQ")

    if button and uploaded_file is not None and number and subject and tone:
        with st.spinner("creating..."):
            try:
                text = read_file(uploaded_file)
                with get_openai_callback() as cb:
                    response = generate_evaluate_chain(
                        {
                            'text':text,
                            'number':number,
                            'subject':subject,
                            'tone':tone,
                            'RESPONSE_JSON':RESPONSE_JSON
                        }
                    )

            except Exception as e:
                traceback.print_exception(type(e),e,e.__traceback__)
            else:
                if isinstance(response,dict):
                    # extract the quiz from response
                    quiz = response.get('quiz',None)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            st.table(df)
                            # Display the review in text box

                            st.text_area(label = "Review", value = response['review'])
                        else:
                            st.error("Error in table")
                    else:
                        st.write(response)

