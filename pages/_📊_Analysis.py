import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.header("Analysis")

image1 = Image.open('pages/A_1.png')
st.image(image1, caption='Analysis 1 - Author with highest no.of books published')

image2 = Image.open('pages/A_2.png')
st.image(image2, caption='Analysis 2 - Top publishers')

image3 = Image.open('pages/A_3.png')
st.image(image3, caption='Analysis 3 - Top 10 highest rated books')

image4 = Image.open('pages/A_4.png')
st.image(image4, caption='Analysis 4 - Top 10 highest rated authors')

image5 = Image.open('pages/A_5.png')
st.image(image5, caption='Analysis 5 - Number of Books published on yearly basis')

image6 = Image.open('pages/A_6.png')
st.image(image6, caption='Analysis 6 - Age distribution')

# st.markdown("<h3 style='text-align: center; color: white;'>Smaller headline in black </h2>", unsafe_allow_html=True)
image7 = Image.open('pages/A_7.png')
st.image(image7, caption='Analysis 7 - Rating distribution')



