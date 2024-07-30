import pickle
import streamlit as st
import pandas as pd
import gzip
import pickle

with gzip.open('similarity.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)
# # Load the .pkl file
# with open('similarity.pkl', 'rb') as f:
#     data = pickle.load(f)
#
# # Save the compressed file
# with gzip.open('similarity.pkl.gz', 'wb') as f:
#     pickle.dump(data, f)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []
    for i in movies_list:
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
movie_list = movies['title'].values

st.title('Movie Recommender System')

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)

    for movie in recommended_movie_names:
        st.markdown(f"""
        <div style="border:2px solid #f0f0f0; border-radius:10px; padding: 10px; margin: 10px 0; box-shadow: 2px 2px 12px #aaa;">
            <h3>{movie}</h3>
        </div>
        """, unsafe_allow_html=True)
