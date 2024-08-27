import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
genai.configure(api_key="AIzaSyA2lnH2kXhwvAyZBmm2osOzhdEsAQB9zZE")

model=genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(user_input, image):
    if user_input != "":
        response = model.generate_content([user_input, image])
    else:
        response = model.generate_content(image)
    return response

st.set_page_config(page_title="Using LLM on Images (Gemini)")

st.header("Gemini FLash for Images")


user_input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)


submit = st.button("Click to find what an LLM outputs")

if submit:
    if image is not None:
        response = get_gemini_response(user_input, image)
        st.subheader("The Output")
        st.write(response.text)
    else:
        st.write("Please upload an image.")