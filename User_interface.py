
from chatbot_google_search import extract_gemini_response,google_search
import streamlit as st

# Main UI of the project

def main():
    """ Main User interface of the project using streamlit """
    st.set_page_config(page_title="Streamlit Container Example", layout="wide")
    # title of the User Interface 
    st.title("Search the item  you are looking for")
    # Text Input field 
    user_input = st.text_input("Enter your search:")
    
    # Checking if the user has entered the text in the textfield or not 
    if user_input:
        
        with st.container():
            

            col1, col2 = st.columns(2)
            with st.spinner("Processing the result..."):
                # if the text is inputed by the user then getting the response from gemini 
                gemini_response,memory = extract_gemini_response(user_input)
                st.markdown(
                        """
                        <style>
                        .stColumn {
                            border: 2px solid orange; 
                            border-radius: 20px;
                            padding: 10px;       
                        }
                        </style>
                        """, 
                        unsafe_allow_html=True
                    )
            with col1:
                st.subheader("Chatbot")
                st.write(gemini_response)
                print(gemini_response)
                if st.button("Clear Conversation"):
                    memory.clear()
            # Fetch Google Search results
            with col2:
                with st.spinner("Fetching search results..."):
                        if "I'm sorry'" not in gemini_response:
                            search_results = google_search(user_input)
                
                        st.subheader("Relevant Links as per the search:")
                        st.write(search_results)
                        if search_results:
                            for result in search_results:
                                link, title, snippet, image = (
                                result.get("link"),
                                result.get("title"),
                                result.get("snippet"),
                                result.get("pagemap", {}).get("cse_image", [{}])[0].get("src")
                                                    )
                                
                                # Display the result with a clickable title, snippet, and image
                                if link and title:
                                    st.markdown(f"### [{title}]({link})")
                                    st.write(snippet)
                                    
                                    if image:
                                        st.image(image, width=280)
                                st.markdown("###")
                        else:
                            st.write("Result Not Found.")


if __name__ == "__main__":
    main()