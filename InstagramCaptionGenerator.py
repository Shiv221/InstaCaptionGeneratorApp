from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import streamlit as st

apiKey = st.secrets["openai_api_key"]
llm = OpenAI(openai_api_key=apiKey,temperature=0.9)


# streamlit framework


st.title('Welcome to InstaCaptions.AI!')
input_text=st.text_input("just entered the photo type (Travel Photo,Food Photo,Selfie, Nature Photo, Fitness Photo, Marraige Photo, Gym Photo) and get best captions for your post")
text ="Instagram 20 captions for"+input_text
st.write(llm(text))



# prompt = PromptTemplate(
# input_variables=["photoType"],
#     template= "Instagram 20 captions and 20 hashtags for {photoType}"+input_text
# )

# print(prompt.format(input_text="photoType"))

# st.write(llm(prompt.format(photoType=["photoType"])))
