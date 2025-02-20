import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


#set up environment varibales
import os
from dotenv import load_dotenv

load_dotenv()


#implement langsmith tracking
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
langchain_tracing = os.getenv("LANGCHAIN_TRACING_V2", 'true')
langchain_project = os.getenv("LANGCHAIN_PROJECT")


#Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'As a helpful assistance, please provide the appropriate response to the question asked my the user'),
        ('user', 'Question : {question}')
    ]
)

#function to generate response from the chatbot
def generate_response(question, api_key, model, temperature, max_token):
    os.environ["OPENAI_API_KEY"] = api_key # you'll have to pass your api key every time you call this function (or you can load it from environment openai.api_key = os.getenv("OPENAI_API_KEY"))
    model = ChatOpenAI(model = model)
    chain = prompt | model | StrOutputParser()
    response = chain.invoke(
        {
            'question': question
        }
    )
    return response

#crreate the streamlit app
st.title("Enhance Q&A Chatbot with OpenAI")

#sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your OpenAI api key", type = 'password')

#dropdown to selecte various openai models
model = st.sidebar.selectbox("Select your prefered OpenAI model", ['gpt-4o', 'gpt-4o-mini', 'gpt-4'])

#set the temperature value using slider
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_token = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=100)

##Main interface for user input
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if user_input and api_key:  # Check both conditions
    try:
        response = generate_response(user_input, api_key, model, temperature, max_token)
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
elif user_input and not api_key:
    st.warning("Please enter the OpenAI API key in the sidebar")
else:
    st.write("Please provide a query")