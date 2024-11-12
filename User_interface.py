# Main UI 
from googlesearch import extract_gemini_response,google_search,load_prompt
import streamlit as st




# Main UI
def main():
    """ Main User interface of the project using streamlit """
    st.set_page_config(page_title="Streamlit Container Example", layout="wide")
    # title of the User Interface 
    st.title("Search Anything you want")
    # Text Input field 
    user_input = st.text_input("Enter your search:")
    # Checking if the user has entered the text in the textfield or not 
    if user_input:
        
        with st.container():
            

            col1, col2 = st.columns(2)
            with st.spinner("Generating response..."):
                # if the text is inputed by the user then getting the response from gemini 
                gemini_response = extract_gemini_response(user_input)
                st.markdown(
                        """
                        <style>
                        .stColumn {
                            border: 2px solid red; /* Green border */
                            border-radius: 10px;       /* Rounded corners */
                            padding: 10px;             /* Inner padding */
                            margin: 3px;              /* Space between columns */
                        }
                        </style>
                        """, 
                        unsafe_allow_html=True
                    )
            with col1:
                st.subheader("Chatbot Response:")
                st.write(gemini_response)

            # Fetch Google Search results
            with col2:
                with st.spinner("Fetching search results..."):
                    search_results = google_search(user_input)
                
                st.subheader("Relevant Links as per the search:")
                
                if search_results:
                    for result in search_results:
                        link = result.get("link")
                        title = result.get("title")
                        snippet = result.get("snippet")
                        image = result.get("pagemap", {}).get("cse_image", [{}])[0].get("src")

                        # Display the result with a clickable title, snippet, and image
                        if link and title:
                            st.markdown(f"### [{title}]({link})")
                            st.write(snippet)
                            
                            if image:
                                st.image(image, width=250)
                        st.markdown("---")
                else:
                    st.write("No relevant results found.")


if __name__ == "__main__":
    main()