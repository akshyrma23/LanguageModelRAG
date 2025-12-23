from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model = ChatOpenAI()

st.header("Reasarch Assistant")

user_input = st.text_area("Enter your query here:") 
if st.button('Submit'):
    result = model.invoke(user_input)
    st.write(result.content)
