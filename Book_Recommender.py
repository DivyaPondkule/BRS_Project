import pickle
import streamlit as st


st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="expanded",
)


st.header("Book Recommender system")
model_knn = pickle.load(open('model_knn.pkl', 'rb'))
books_name = pickle.load(open('books_name.pkl', 'rb'))
user_rating = pickle.load(open('user_rating.pkl', 'rb'))
popular_df = pickle.load(open('popular_df.pkl', 'rb'))
user_rating_pivot2 = pickle.load(open('user_rating_pivot2.pkl', 'rb'))

selected_books = st.selectbox(
    "Type or select a book",
    books_name
)

def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(user_rating_pivot2.index[book_id])

    for name in book_name[0]:
        ids = np.where(user_rating['Book-Title'] == name)[0][0]
        ids_index.append(ids)

    for ids in ids_index:
        url = user_rating.iloc[ids]['Image-URL-M']
        poster_url.append(url)
    return poster_url

def recommend_books(bk_name):
    book_list = []
    # index fetch
    if bk_name==' ':
        st.text('Select a book')
    else:
        book_id = np.where(user_rating_pivot2.index==bk_name)[0][0]
        distance,suggestion =  model_knn.kneighbors(user_rating_pivot2.iloc[book_id,:].values.reshape(1,-1),n_neighbors=6)
        poster_url = fetch_poster(suggestion)
        for i in range(len(suggestion)):
            books =user_rating_pivot2.index[suggestion[i]]
            for j in books:
                book_list.append(j)
            return book_list, poster_url

if st.button('Show Recommendations'):
    recommendation_books, poster_url = recommend_books(selected_books)
    for i in range(1,6):
        st.text(str(i)+". " + recommendation_books[i])
        st.image(poster_url[i])
