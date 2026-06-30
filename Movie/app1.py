import streamlit as st  #---imported for create frontend
import requests         #---This helps to connect stremlit and fastapi

API_URL = "http://127.0.0.1:8000"   #---local url

#---Below are streamlit components for different purpose
st.title('🎬 Movie Explorer & Review Management System')
st.write(
    "Welcome to the Movie Explorer & Review Management System! This application helps to perform CRUD operations "
    "where you can easily view, add, search, update, "
    "and delete movie tracking entries alongside their rating scale scores."
)

menu=st.sidebar.selectbox(
    'Select Options',
    ['View All Movies',
    'Search / Filter Movies',
    'Add New Movie',
    'Update Movie',
    'Delete Movie']
)

st.write("---") 

#######################################################
# View All Movies
#######################################################

#---if block, executing for when user choose View All Movies,
##--- using bridge to connect streamlit with fastapi get method(read data)

if menu=='View All Movies':
    st.header('All Movies')
    response = requests.get(f'{API_URL}/movies')  #---using requests to connect frontend and backend
    movies=response.json()                        #---this step is to convert backend data to json format and storing it
    if movies:
        st.table(movies)
    else:
        st.warning('No Movies found')

#######################################################
# Search / Filter Movies
#######################################################

#---This block of code, executing for when user choose Search / Filter Movies,
##--- using bridge to connect streamlit with fastapi get method(read data based on provided individual input)
###---selectbox for different genre,language,rating and passing them in get of fastapi

elif menu=='Search / Filter Movies':
    st.header('Search Movies')
    Genre=st.selectbox('Genre',['Action','Comedy','Drama','Sci-Fi'],index=None,placeholder="Select Genre")
    Language=st.selectbox('Language',['Telugu','Hindi','English'],index=None,placeholder="Select Language")
    Rating = st.selectbox("Rating",options=[1,2,3,4,5,6,7,8,9,10],index=None,placeholder="Select Rating")
    if st.button('Search'):
        params={'genre':Genre,
                'language':Language,
                'rating':Rating
        }
        response = requests.get(
            f"{API_URL}/movie",params=params
        )
        st.write(response.json())
        

#######################################################
# Add New Movie
#######################################################

#---This block of code, executing for when user choose Add New Movie,
##--- using bridge to connect streamlit with fastapi post method(creat data)

elif menu=='Add New Movie':
    st.header('Add Movie')
    movie_id=st.number_input('Enter movie ID',min_value=1,step=1)
    Movie_name=st.text_input('Enter movie name')
    Genre=st.selectbox('Select Genre',['Comedy','Action','Drama','Sci-Fi'])
    Language=st.selectbox('Select Language',['English','Telugu','Hindi'])
    Rating=st.number_input('Enter a 1-10 Rating',min_value=1,max_value=10,step=1,key='add rating')
    if st.button('Add Movie'):
        #---in below the left side are keys and right side the given variables above 
        #---which are mapped direclty to backend validation model
        data={
            'id':movie_id,
            'movie_name':Movie_name,
            'genre':Genre,
            'language':Language,
            'rating':Rating
        }
        response = requests.post(f'{API_URL}/movies',json=data)

        #---Access the response message from the backend jason dict
        st.success(response.json()["Message"])

#######################################################
# Update Movie
#######################################################
#---This block of code, executing for when user choose Update Movie,
##--- using bridge to connect streamlit with fastapi put method(to update data of existing)

elif menu == "Update Movie":
    st.header("Update Movie")
    movie_id=st.number_input('Enter THE Movie ID',min_value=1,step=1,key='update_id')
    Movie_name=st.text_input('Enter Movie Name')
    Genre=st.selectbox('select genre',['Drama','Action','Comedy','Sci-Fi'],key='Genre_update')
    Language=st.selectbox('select language',['Telugu','Hindi','English'],key='Language_update')
    Rating=st.number_input('enter a 1-10 rating',min_value=1,max_value=10,step=1,key='Rating_update')
    if st.button('Update'):
        data={
            'id':movie_id,
            'movie_name':Movie_name,
            'genre':Genre,
            'language':Language,
            'rating':Rating
        }        
        response = requests.put(f'{API_URL}/movies/{movie_id}',json=data)
        st.success(response.json()['Message'])
        
        st.write(response.status_code)
        st.write(response.json())

#######################################################
# Delete Movie
#######################################################
#---This block of code, executing for when user choose Delete Movie,
##--- using bridge to connect streamlit with fastapi delete method(to delete data of existing)

elif menu == "Delete Movie":
    st.header("Delete Movie")
    movie_id=st.number_input('Enter Movie ID to delete',min_value=1,step=1,key='delete_id')
    if st.button('Delete'):
        response = requests.delete(f"{API_URL}/movies/{movie_id}")
        st.success(response.json()["Message"])        

