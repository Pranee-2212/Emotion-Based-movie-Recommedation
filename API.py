import requests
import os
from dotenv import load_dotenv
from api_addressData import movie_genres_id,emotion_recommendations
load_dotenv()

def get_movie_recommendation(id_string):
     url = os.getenv("MOVIE_URL")

     querystring = {"with_genres":str(id_string),"page":"1"}

     headers = {
	     "x-rapidapi-key":os.getenv("MOVIE_RAPID_API_KEY"),
	     "x-rapidapi-host":os.getenv("MOVIE_HOST_API_KEY")
     }
     response = requests.get(url, headers=headers, params=querystring)
     dict=response.json()
     arr=[]
     for i in dict['results']:
          movie_item={
               'title':i['title'],
               'release_date':i['release_date'],
               'overview':i['overview'],
               'poster_path':i['poster_path']
          }
          arr.append(movie_item)
     return arr




def get_song_recommendation(id_string):
     pass 

def get_emotion_index(text):
     requested_genre=emotion_recommendations[text]['movie_genres'][:3]
     idstring=""
     for i in requested_genre:
          idstring+=str(movie_genres_id[i])+","
     return idstring



