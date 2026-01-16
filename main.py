

import os
os.environ['GOOGLE_API_KEY']  = st.secrets["GOOGLE_API_KEY"]

# Using Google Models (Gemini Pro)
from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

from langchain_core.prompts import PromptTemplate

# Create prompt template for generating tweets

tweet_template = "Give me {number} tweets on {topic}"

tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ['number', 'topic'])

from langchain_core.prompts import ChatPromptTemplate


# Create LLM chain using the prompt template and model
tweet_chain = tweet_prompt | gemini_model

# Set up the Streamlit app - frontend
#pip install --upgrade langchain langchain-google-genai streamlit

import streamlit as st
st.header("Tweet Generator")
st.subheader("Generate engaging tweets using Generative AI")

topic = st.text_input("Enter a topic for your tweet:")
number = st.number_input("Number of tweets to generate:", min_value=1, max_value=10, value=1)

if st.button("Generate Tweets"):
    tweets = tweet_chain.invoke({"number" : number, "topic" : topic})
    st.write(tweets.content)
# To run the app, use the command: streamlit run main.py




