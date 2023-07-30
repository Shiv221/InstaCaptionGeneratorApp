from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import streamlit as st

llm = OpenAI(openai_api_key='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',temperature=0.9)


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