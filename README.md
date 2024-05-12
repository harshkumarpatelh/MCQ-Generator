# MCQ-Generator
<p>
  <img src = "media/langchain.png" width = "250px" height ="100px">
  <img src ="media/openai.jpeg" width ="200px" height ="100px">
  <img src ="media/streamlit.png" width ="200px" height ="100px">
</p>

Welcome to MCQ Generator with AI !!\
This is a Streamlit application that allows users to generate multiple-choice questions (MCQs) from an uploaded PDF or text file. Users can generate a minimum of 3 and a maximum of 50 MCQs from the file at once. They must also specify the related subject for which the MCQs will be generated, as well as the complexity level of the questions (e.g., simple, medium, hard).
It was developed in [langchain framework](https://python.langchain.com/v0.1/docs/get_started/introduction/) and used [ChatOpenAI](https://python.langchain.com/v0.1/docs/integrations/chat/openai/#chaining), LLMchain through langchain. I have used OpenAI [gpt-3.5-turbo-0125](https://platform.openai.com/docs/models/gpt-3-5-turbo) model for generation. Finally, used streamlit for application creation and deployed on [AWS EC2 instance](https://ap-southeast-2.console.aws.amazon.com/ec2/home?region=ap-southeast-2#Home:)

## How to run on local system
  Open your terminal and follow these steps
1. git clone https://github.com/harshkumarpatelh/MCQ-Generator.git
2. Now change Directory to MCQ-Generator\
    cd MCQ-Generator
3. Install all libraries\
    pip install -r rquirements.txt
4. Run the streamlit app(Must add OpenAI api key(i.e. open_key) in the environment in which you are running it or create venv)\
    streamlit run streamlitApp.py

### Sample Video Deployed on AWS
https://github.com/harshkumarpatelh/MCQ-Generator/assets/126771343/396c1e49-449a-417a-b0f9-5689ca2ba056

