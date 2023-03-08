import pickle
import streamlit as st


st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.header("Books popular yearly")
popular_df_y = pickle.load(open('popular_df_y.pkl', 'rb'))


for i in range(len(popular_df_y)):
    # st.text(str(i+1)+". "+popular_df_y.iloc[i][1]+" Year: "+str(popular_df_y.iloc[i][3]))
    st.text(str(i + 1) + ". "+" Year: " + str(popular_df_y.iloc[i][3]))
    st.text(popular_df_y.iloc[i][1])
 
