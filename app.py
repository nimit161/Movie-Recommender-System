import pickle
import streamlit as st
import requests


API_KEY = st.secrets["API_KEY"]

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return "https://via.placeholder.com/500x750?text=API+Error"

        data = response.json()

        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"

    except Exception as e:
        return "https://via.placeholder.com/500x750?text=Error"


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),
                       reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]]['id']   # ✅ safer access
        recommended_movie_names.append(movies.iloc[i[0]]['title'])
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters


# UI
st.header('Movie Recommender System')

movies = pickle.load(open('model/movie_list.pkl', 'rb'))
# similarity = pickle.load(open('model/similarity.pkl', 'rb'))

import joblib

similarity = joblib.load('model/similarity.pkl')

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
