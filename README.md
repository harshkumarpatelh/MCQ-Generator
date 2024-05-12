# MCQ-Generator
Welcome to MCQ Generator with AI!
It is an streamlit application which offer user to generator MCQ question from a uploaded pdf or text file uploaded by user. User can generator minimum 3 and maximum 50 MCQ from that file at once. Must enter the related subject for which MCQ will be generated and also enter complexity level of questions(e.g. simple, medium,hard).
It was developed in [langchain framework](https://python.langchain.com/v0.1/docs/get_started/introduction/) and used [ChatOpenAI](https://python.langchain.com/v0.1/docs/integrations/chat/openai/#chaining), LLMchain through langchain. I have used OpenAI [gpt-3.5-turbo-0125](https://platform.openai.com/docs/models/gpt-3-5-turbo) model for generation. Finally, used streamlit for application creation and deployed on [AWS EC2 instance](https://ap-southeast-2.console.aws.amazon.com/ec2/home?region=ap-southeast-2#Home:)

# How to run on local system
  Open your terminal and folloe these steps
1. git clone https://github.com/harshkumarpatelh/MCQ-Generator.git
2. Now change Directory to MCQ-Generator
    `cd MCQ-Generator
3. Install all libraries
    `pip install -r rquirements.txt
4. Run the streamlit app(Must add OpenAI api key(i.e. open_key) in the environment in which you are running it or create venv)
    command<streamlit run streamlitApp.py>