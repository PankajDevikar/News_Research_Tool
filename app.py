import os
import streamlit as st
from dotenv import load_dotenv
from newsapi import NewsApiClient

# Load environment variables from .env file
load_dotenv()

# Retrieve API key
newsapi_key = os.getenv("NEWSAPI_KEY")

# Initialize NewsAPI
newsapi = NewsApiClient(api_key=newsapi_key)

# Function to fetch news articles using NewsAPI
def get_news_articles(query):
    articles = newsapi.get_everything(q=query, language="en", sort_by="relevancy")
    return articles["articles"]

# Streamlit App Interface
## Title of the app with Banner Image
if os.path.exists("img1.jpg"):
    st.image("img1.jpg", width=400)

st.title("Equity Research News Tool")
st.write("Enter your query to get the latest news articles.")

## Sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

## Select the Groq model
available_models = [
    "llama-3.1-8b-instant", 
    "mixtral-8x7b-32768", 
    "gemma2-9b-it", 
    "whisper-large-v3"
]
engine = st.sidebar.selectbox("Select Groq model", available_models)

## Adjust response parameter
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

query = st.text_input("Query")
if st.button("Get News"):
    if query:
        articles = get_news_articles(query)
        if articles:
            st.write("### Latest News Articles:")
            for article in articles[:5]:  # Limit to top 5 articles
                st.write(f"#### {article['title']}")
                st.write(article['description'] or "No description available")
                st.write(f"[Read more]({article['url']})")
        else:
            st.write("No relevant news articles found.")
    else:
        st.write("Please enter a query.")