import pickle
import streamlit as st


st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.header("Top 50 books")
popular_df = pickle.load(open('artifacts/popular_df.pkl', 'rb'))


for i in range(len(popular_df)):
    st.text(str(i+1)+". "+popular_df.iloc[i][1])
    st.image(popular_df.iloc[i][3])
