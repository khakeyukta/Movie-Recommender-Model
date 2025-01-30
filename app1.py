import streamlit as st
import requests 
import pickle
def recommend(movie):
    index=movies[movies["title"]==movie].index[0]
    distances=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
    recommended_moviename=[]
    recommended_movieposter=[]
    for i in distances[1:6]:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_moviename.append(movies.iloc[i[0]].title)
        recommended_movieposter.append(fetch_poster(movie_id))
    return recommended_moviename,recommended_movieposter

def fetch_poster(movie_id):
    url=('https://api.themoviedb.org/3/movie/{}?api_key=0fab12ec0d4b32b721a381e4f79ec172'.format(movie_id)) 
    data=requests.get(url) 
    data=data.json() 
    poster_path=data['poster_path']
    full_path='http://image.tmdb.org/t/p/w500'+ poster_path 

    return full_path


st.header("RECOMMENDER SYSTEM")
movies=pickle.load(open("artifacts\movies_list.pkl","rb"))
similarity=pickle.load(open("artifacts\similarity.pkl","rb"))
movielist=movies["title"]
selected_movies=st.selectbox("Select a movie",movielist)

if st.button('Recommend'):

    recommended_movie_name,recommend_movie_poster=recommend(selected_movies)
    col1,col2,col3,col4,col5=st.columns(5)

    with col1:
        st.text(recommended_movie_name[0])
        st.image(recommend_movie_poster[0],width=100)

    with col2:
        st.text(recommended_movie_name[1])
        st.image(recommend_movie_poster[1],width=100)
    with col3:
        st.text(recommended_movie_name[2])
        st.image(recommend_movie_poster[2],width=100)
    with col4:
        st.text(recommended_movie_name[3])
        st.image(recommend_movie_poster[3],width=100)
    with col5:
        st.text(recommended_movie_name[4])
        st.image(recommend_movie_poster[4],width=100)