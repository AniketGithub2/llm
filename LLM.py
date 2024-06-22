import streamlit as st
from streamlit_option_menu import option_menu
import os
from langchain.llms import GooglePalm 
from langchain.embeddings import HuggingFaceInstructEmbeddings


# Set up Google API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyCeTe213mlNQVOe4iWq09OIrNjlO6F5n48"
api_key = os.environ.get("GOOGLE_API_KEY")
llm = GooglePalm(google_api_key=api_key, temperature=0.9)


# Set
#  up the styling for the app
st.markdown(
    '''
    <style>
    .title {
        font-size: 48px;
        color: #8A2BE2;
    }
    .sidebar-title {
        font-size: 20px;
        color: black;
    }
    .content {
        font-size: 14px;
    }
    .main {
        background-color: #FAFAD2;  /* Light Goldenrod Yellow */
    }
    
    </style>
    ''',
    unsafe_allow_html=True
)

# Page title
st.markdown('<h1 class="title">Welcome to the Movie Search App!</h1>', unsafe_allow_html=True)

# Center content div
st.markdown('<div class="center-content">', unsafe_allow_html=True)

# Input for user's question
ques = st.text_input('What is your question?')
if st.button('Search'):
    with st.spinner('Loading your result...'):
        result = llm(ques)
        st.write(f'ANSWER: {result}')

# Sidebar with URL inputs
with st.sidebar:
    st.markdown('<h2 class="sidebar-title">URLS</h2>', unsafe_allow_html=True)
    st.markdown('<div class="content">From any websites you can fetch data</div>', unsafe_allow_html=True)
    url1 = st.text_input('URL 1', 'Enter your url')
    url2 = st.text_input('URL 2', 'Enter your url')
    url3 = st.text_input('URL 3', 'Enter your url')
    
    if st.button('Fetch URL'):
        with st.spinner('Fetching URL from server...'):
            # Function to fetch and display content from a URL
  
            
            # Display fetched data from URLs
            if url1 != 'Enter your url':
                st.write(f'Data from {url1}: {fetch_url_content(url1)}')
            if url2 != 'Enter your url':
                st.write(f'Data from {url2}: {fetch_url_content(url2)}')
            if url3 != 'Enter your url':
                st.write(f'Data from {url3}: {fetch_url_content(url3)}')
