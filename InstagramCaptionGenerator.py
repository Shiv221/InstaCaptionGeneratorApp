from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import streamlit as st

apiKey = st.secrets["openai_api_key"]
llm = OpenAI(openai_api_key=apiKey,temperature=0.9)


# streamlit framework

st.title('Celebrity Search Results')
input_text=st.text_input("Search the topic u want")
text ="Instagram 20 captions for"+input_text
st.write(llm(text))


# prompt = PromptTemplate(
# input_variables=["photoType"],
#     template= "Instagram 20 captions and 20 hashtags for {photoType}"+input_text
# )

# print(prompt.format(input_text="photoType"))

# st.write(llm(prompt.format(photoType=["photoType"])))
