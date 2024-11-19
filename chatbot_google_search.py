import streamlit as st
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationSummaryMemory
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
    """response from gemini model """
    
    prompt = load_prompt()
    
    #  prompt template
    prompt_template = PromptTemplate(
        template=prompt,
        input_variables=["history", "user_query"]
    )
    
    # Initialization of  the Gemini model
    gemini_model = intialize_model()
    memory = ConversationSummaryMemory(llm=gemini_model)
    # Initialization of buffer  memory 


    #  LLMChain 
    chain = LLMChain(
        llm=gemini_model,
        prompt=prompt_template,
        memory=memory
    )

    try:
        
        
            
            # Get the response from  model
            response = chain.invoke({"user_query": user_query})
            
           
            return response['text'], memory
    
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None



def google_search(user_input):
    """Extract top 5 search results using Google's Custom Search API as per the user entered input """
    google_search_url = "https://www.googleapis.com/customsearch/v1"
    search_query = f"online shopping of {user_input}  "
    parameter = {
        "key": GOOGLE_API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "q": search_query,
        "num": 5  
    }
    
    try:
        response = requests.get(google_search_url, params=parameter)
        if response.status_code == 200:
            return response.json().get("items", [])
    except Exception as e:
        st.error(f"Error while extracting search results from google search: {e}")
    
    return []






