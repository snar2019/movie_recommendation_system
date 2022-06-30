import streamlit as st
import pickle
import requests




st.title('Movie Recommender System')

#importing pickle files
movies= pickle.load(open('movies_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


movies_list = movies['title'].values

selected_movie = st.selectbox(
    'Select the movie from the drop-down menu',
    movies_list
)
st.write("you entered:  ", selected_movie)


### recommender system code





def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=fa276b2e9990344d86acbe41c3b4c3bf&language=en-US'.format(movie_id)
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_listed = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_listed:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        #fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster





if st.button('Show Recommendations'):
    recommended_movies, recommended_movies_poster = recommend(selected_movie)

    col1, col2,col3,col4,col5= st.columns(5)
    with col1:
        st.text(recommended_movies[0])
        st.image(recommended_movies_poster[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(recommended_movies_poster[1])
    with col3:
        st.text(recommended_movies[2])
        st.image(recommended_movies_poster[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(recommended_movies_poster[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(recommended_movies_poster[4])











