# Product Search Chatbot with Google Search Integration

A Streamlit-based chatbot application that provides intelligent product information using LLM and integrates with Google Search API to display relevant search results.

## 🚀 Features

- **Interactive Chat Interface**: Clean and intuitive Streamlit UI for seamless user interaction
- **LLM-Powered Responses**: Intelligent product information and recommendations powered by language models
- **Google Search Integration**: Displays relevant product search results using Google Search API
- **Product-Focused**: Specifically designed to handle product-related queries with smart filtering
- **Real-time Suggestions**: Provides product recommendations when requested

## 📋 Prerequisites

- Python 3.8 or higher
- Google Search API credentials
- LLM API access (OpenAI, Anthropic, or similar)
- Streamlit

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/product-search-chatbot.git
cd product-search-chatbot
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory:
```env
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CSE_ID=your_custom_search_engine_id
LLM_API_KEY=your_llm_api_key
```

## 📦 Dependencies

```txt
streamlit
google-api-python-client
python-dotenv
openai  # or your preferred LLM library
requests
```

## 🎯 How It Works

1. **User Input**: Users enter product-related queries through the Streamlit interface
2. **LLM Processing**: The query is processed by the LLM using a specialized system prompt that:
   - Provides clear product descriptions
   - Explains key features and relevant details
   - Offers product suggestions when requested
   - Filters out non-product queries
3. **Google Search**: Simultaneously fetches relevant search results via Google Search API
4. **Response Display**: Shows both the LLM response and search results in an organized format

## 💡 System Prompt

The chatbot uses a structured prompt system:

```
System:
When the user asks about a specific product or item, provide a clear explanation 
about the product based on the user's query.

User Input:
User query: {user_query}

Your Response:
Provide a clear description, key features, or relevant details that answer the 
question clearly.

---
Negative prompt:
[if user_input is not related to any **product** then remind them to search 
about **product** only]

---
System:
when the user ask for the suggestion about the **product**, please provide them.
```

## 🚀 Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Enter your product query in the chat interface

4. Receive:
   - Detailed product information from the LLM
   - Relevant Google search results

## 📝 Example Queries

**Valid queries:**
- "Tell me about iPhone 15 Pro features"
- "Best laptops under $1000"
- "Compare Samsung Galaxy S24 vs iPhone 15"
- "Suggest wireless headphones for running"

**Invalid queries (filtered):**
- "What's the weather today?"
- "Tell me a joke"
- "How to bake a cake?"

## 🔧 Configuration

Customize the chatbot behavior by modifying:

- `prompt.txt`: Adjust the LLM behavior and response style
- `chatbot_google_search.py`: Configure search parameters and API settings
- `user_interface.py`: Modify UI layout and interaction flow




## 🙏 Acknowledgments

- Streamlit for the amazing web framework
- Google Custom Search API for search functionality
- OpenAI/Anthropic for LLM capabilities


**Note**: Remember to keep your API keys secure and never commit them to version control. Always use environment variables or secure secret management systems.
