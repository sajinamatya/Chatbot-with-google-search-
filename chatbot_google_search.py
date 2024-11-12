import streamlit as st
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, dotenv_values
import requests
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate

# Loading the .env file for getting the access ot its all the variables
load_dotenv()

# Loading environment variables from .env file
config = dotenv_values(".env")
# Getting access to all the Required API KEY from env file 
GOOGLE_API_KEY = config.get("GOOGLE_API_KEY")
GEMINI_API_KEY = config.get("GEMINI_API_KEY")
SEARCH_ENGINE_ID = config.get("SEARCH_ENGINE_ID")


def load_prompt():
    try:
        with open("prompt.txt", "r") as prompt_read:
            prompt = prompt_read.read()
    except FileNotFoundError:
        print("Error: 'prompt.txt' file not found.")
    except PermissionError:
        print("Error: Permission denied when accessing file  'prompt.txt'.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
    return prompt

# Intialization of the Gemini model
def intialize_model():
    """ Intializing the gemini model to generate the response for user inputs"""
    try: 
        gemini_model = ChatGoogleGenerativeAI(model="gemini-pro",
                                temperature=0.4)
    except Exception as e:
        print("An error has occured in initalization of the gemini model", str(e))
    return gemini_model

    
def extract_gemini_response(user_query):
    """Get response from Gemini API using the .invoke() method."""
    prompt = load_prompt()
    prompt_template = PromptTemplate(template=prompt, input_variables=["user_query"])
    gemini_model = intialize_model()
    # Use the new .invoke() method
    try:
        chain = LLMChain(llm=gemini_model, prompt=prompt_template)
  
        # Invoke the Gemini model
        response = chain.invoke({"user_query": user_query},return_only_outputs=True)
        
       
        return response['text']
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None


def google_search(user_input):
    """Extract top 5 search results using Google's Custom Search API as per the user entered input """
    search_url = "https://www.googleapis.com/customsearch/v1"
    parameter = {
        "key": GOOGLE_API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "q": user_input,
        "num": 5  
    }
    
    try:
        response = requests.get(search_url, params=parameter)
        if response.status_code == 200:
            return response.json().get("items", [])
    except Exception as e:
        st.error(f"Error while extracting search results from google search: {e}")
    
    return []






