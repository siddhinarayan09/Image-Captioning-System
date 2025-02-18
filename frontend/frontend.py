import streamlit as st
import requests
import os

BACKEND_URL = "http://127.0.0.1:5001"  # Flask API URL

st.title("Image Caption Generator")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    if st.button("Generate Caption"):
        files = {"image": uploaded_file.getvalue()}
        uploadImageURL = f"{BACKEND_URL}/api_handler/uploadImage"
        response = requests.post(uploadImageURL, files={"image": uploaded_file})

        if response.status_code == 200:
            file_path = response.json().get("file_path", "Unknown")
            st.success(f"File saved: {file_path}")
        else:
            st.error("Error uploading the file.")
