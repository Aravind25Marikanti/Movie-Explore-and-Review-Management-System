from fastapi import FastAPI 
from pydantic import BaseModel

app=FastAPI()  #---This helps to create API's

#---defined pydantic class
class Movie(BaseModel):
    id: int
    movie_name:str
    genre:str
    language: str
    rating: int


#---Instantiate individual movie objects
movie1 = Movie(id=1, movie_name="Inception", genre="Sci-Fi", language="English", rating=9)
movie2 = Movie(id=2, movie_name="RRR", genre="Action", language="Telugu", rating=10)
movie3 = Movie(id=3, movie_name="3 Idiots", genre="Comedy", language="Hindi", rating=9)
movie4 = Movie(id=4, movie_name="Interstellar", genre="Sci-Fi", language="English", rating=9)
movie5 = Movie(id=5, movie_name="Dangal", genre="Drama", language="Hindi", rating=10)

#---Create the object based dataset
movies = [movie1, movie2, movie3, movie4, movie5]

@app.get('/') #---decorator connects url or endpoint with the function in fastapi's

def home():
    return {'Message':'Welcome to Movie Explorer and Review Management System FastAPI'}

@app.get('/movies')  #---used get method to read the data
def get_movies():
    return movies    #---reading all movies in movies list

@app.get('/movies/{movie_id}')        #---used for reading data one movie at time
def get_single_movie(movie_id:int):   #---movie_id is integer so we given as int
    for movie in movies:              #---Loops runs till id is same of entered movie_id if not returns movie not found message
        if movie.id==movie_id:
            return movie
    return 'Movie not found'

@app.get('/movie')        #---used for reading data based on genre,language,rating filter/ None=used as optional boxes
def get_movie_details_filter(genre:str=None,language:str=None,rating:int=None):   
    result=[]
    # for movie in movies:              #---Loops runs and if block runs then that data will be appended in our new list and that details are displayed
    for movie in movies:
        if((genre is None or movie.genre == genre) and (language is None or movie.language == language) and (rating is None or movie.rating == rating)):
            result.append(movie)
    return result


@app.post('/movies')  #---used for adding data ,for loop used to find same move_id if not found it treated as new movie and will add in movies
def add_movies(data: Movie):
    for movie in movies:
        if movie.id==data.id:
            return {'Message': 'Movie Already Exists'}
    movies.append(data)
    return {'Message': 'Movie Added Successfully'}

@app.put('/movies/{movie_id}')    #---used to update the details any of them
def update_movies(movie_id:int,updated_movie: Movie):
    for index,movie in enumerate(movies):       
        if movie.id==movie_id:
            movies[index]=updated_movie
            return {'Message': 'Movie details updated Successfully'}
    return {'Message': 'Movie Not Found'}

@app.delete('/movies/{movie_id}')  #---Used to delete based on movie_id
def delete_movie(movie_id:int):
    for movie in movies:
        if movie.id==movie_id:
            movies.remove(movie)
            return {'Message': 'Movie Deleted Successfully'}
    return {'Message': 'Movie not Found'}