import streamlit as st
from PIL import Image

st.title("Рецепты")

st.subheader("Рецепты, которые пользователю понравились в прошлом")

col1, col2, col3 = st.columns(3)

image_width = 200
image_height = 150

def load_and_resize_image(image_path, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height))
    return img

with col1:
    st.image(load_and_resize_image("data/1.jpg", image_width, image_height))
with col2:
    st.image(load_and_resize_image("data/2.jpg", image_width, image_height))
with col3:
    st.image(load_and_resize_image("data/3.jpg", image_width, image_height))

st.subheader("Рекомендуемые рецепты")

col4, col5, col6 = st.columns(3)

with col4:
    st.image(load_and_resize_image("data/4.jpg", image_width, image_height))
with col5:
    st.image(load_and_resize_image("data/5.jpg", image_width, image_height))
with col6:
    st.image(load_and_resize_image("data/6.jpg", image_width, image_height))
