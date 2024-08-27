import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key="")
model=genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

st.set_page_config(page_title="Ask Me Anything")

st.header("Trying Power of LLM (gemini)")

input=st.text_input("Common Ask Me ??:",key="input")
submit=st.button("Press me for Answer")

if(submit):
     response=get_gemini_response(input)
     st.subheader("The output is")
     st.write(response)
