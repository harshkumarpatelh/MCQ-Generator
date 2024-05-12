from langchain_community.llms import OpenAI #deprecated from langchain.llms import OpenAI for langchain==0.2.0.
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains.sequential import SequentialChain
from langchain.callbacks import get_openai_callback
import json
import os
from dotenv import load_dotenv   

load_dotenv()
key = os.getenv('openai_key')


# creating LLM object
llm = ChatOpenAI(openai_api_key = key, model_name='gpt-3.5-turbo',temperature =0.7)

with open('F:/ML/NLP/MCQ-Generator/Response.json','r') as f:
    RESPONSE_JSON = json.load(f)

template =  """
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz  of {number} multiple choice questions for {subject} students in {tone} tone. 
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to format your response like  RESPONSE_JSON below  and use it as a guide. \
Ensure to make {number} MCQs
### RESPONSE_JSON
{RESPONSE_JSON}
"""

# prompt template for  generation of quiz
prompt_template = PromptTemplate(
    input_variables=['text','number','subject','tone','RESPONSE_JSON'],
    template=template
)
#creating object of simple chain for LLM and prompt
quiz_chain = LLMChain(llm =llm, prompt=prompt_template, output_key = 'quiz',verbose=True)

template2="""
You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
if the quiz is not at per with the cognitive and analytical abilities of the students,\
update the quiz questions which needs to be changed and change the tone such that it perfectly fits the student abilities
Quiz_MCQs:
{quiz}

Check from an expert English Writer of the above quiz:
"""
# prompt template for  evaluation generated quiz
evalution_prompt_template = PromptTemplate(
    input_variables=['subject','quiz'],
    template=template2
)
#creating object of simple chain for LLM and prompt for evaluation
review_chain = LLMChain(llm =llm, prompt=evalution_prompt_template, output_key = 'review',verbose=True)

# chaining two LLM object sequentially for generation and evaluuation
generate_evaluate_chain = SequentialChain(chains=[quiz_chain,review_chain],input_variables=['text','number','subject','tone','RESPONSE_JSON'],output_variables=['quiz','review'])

