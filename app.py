import streamlit as st
from controller import handle_image_upload, handle_text_query
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="🍽️ Smart Recipe Helper", layout="centered")
st.title("🍽️ Smart Recipe Helper")

# Initialize state for both modes
if "image_result" not in st.session_state:
    st.session_state.image_result = None
if "text_result" not in st.session_state:
    st.session_state.text_result = None
if "text_dish_image_url" not in st.session_state:
    st.session_state.text_dish_image_url = None

# -----------------------------------
# IMAGE MODE
# -----------------------------------
st.header("📷 Upload a Food Image")
uploaded_image = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if st.button("Generate Recipe from Image") and uploaded_image:
    with st.spinner("Analyzing image..."):
        st.session_state.image_result = handle_image_upload(uploaded_image)

if st.session_state.image_result:
    st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)
    
    st.subheader("📝 Ingredients (from Image)")
    st.markdown(st.session_state.image_result["ingredients"] or "Not found")

    st.subheader("👨‍🍳 Preparation (from Image)")
    st.markdown(st.session_state.image_result["preparation"] or "Not found")

    st.subheader("🍽️ Other Recipes (from Image)")
    st.markdown(st.session_state.image_result["related_recipes"] or "Not found")

# -----------------------------------
# TEXT MODE
# -----------------------------------
st.header("💬 Enter Dish Name or Cooking Question")
text_input = st.text_area("e.g. How to make Pulao?")

if st.button("Generate Recipe from Text") and text_input.strip():
    with st.spinner("Generating recipe from text..."):
        st.session_state.text_result = handle_text_query(text_input)

        # Optional: Try to fetch a sample image from Unsplash or a static fallback
        query = text_input.split("make")[-1].strip() if "make" in text_input.lower() else text_input
        img_url = f"https://source.unsplash.com/800x500/?{query.replace(' ', '%20')},food"
        st.session_state.text_dish_image_url = img_url

if st.session_state.text_result:
    if st.session_state.text_dish_image_url:
        st.image(st.session_state.text_dish_image_url, caption="Sample Dish Image", use_container_width=True)

    st.subheader("📝 Ingredients (from Text)")
    st.markdown(st.session_state.text_result["ingredients"] or "Not found")

    st.subheader("👨‍🍳 Preparation (from Text)")
    st.markdown(st.session_state.text_result["preparation"] or "Not found")

    st.subheader("🍽️ Other Recipes (from Text)")
    st.markdown(st.session_state.text_result["related_recipes"] or "Not found")
