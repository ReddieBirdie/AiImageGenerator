import os
import streamlit
from huggingface_hub import InferenceClient
import streamlit as st
import io

st.set_page_config(layout="wide")

styles = [
    "Illustration style",
    "Whimsical watercolor style",
    "Disney pixar animation style",
    "Line drawing style",
    "High-definition and realistic style",
    "Origami style",
    "Studio Ghibli style",
    "Multiple poses",
    "Side lighting",
    "Isometric views"
]

st.title("Ai Image Generator")
st.subheader("Inputs")
style = st.selectbox("Select a style for you image", options=styles)
name = st.text_input("Enter the subject of the image")
location = st.text_input("Enter the location of the image")
looks = st.text_input("Enter characteristic of image (cool, fierce, cute, etc)")
outfit = st.text_input("Enter the outfit of the subject")
size = st.number_input("Enter the size of the image",value = 400,min_value = 100)

prompt = f"Generate an image of a {name}, living in a {location}. It looks {looks} and is dressed like a {outfit}. The style is {style}"

st.write(prompt)

if(st.button("Generate")):
    with st.spinner("loading . . ."):
        os.environ["HF_TOKENS"] = "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"

        client = InferenceClient(
          provider="nscale",
          api_key=os. environ ["HF_TOKENS"],
        )

        # output is a PIL.Image object
        image = client.text_to_image(
          prompt,
          model="stabilityai/stable-diffusion-xl-base-1.0",
        )
    st.image(image,width = size)
    buffer = io.BytesIO()
    image.save(buffer,format = 'PNG')
    st.download_button(
        label = "download image",
        data = buffer.getvalue(),
        file_name = "image.png",
        mime = "image/png"
    )