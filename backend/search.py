import os
import requests
from dotenv import load_dotenv

load_dotenv()

apiKey = os.getenv('TMDB_API_KEY')

baseURL = "https://api.themoviedb.org/3"

imageBaseURL = "https://image.tmdb.org/t/p"
posterSize = "w200"
backdropSize = "w500"

def getPosterURL(posterPath):
    if posterPath:
        return f"{imageBaseURL}/{posterSize}{posterPath}"
    return None

def getBackdropURL(backdropPath):
    if backdropPath:
        return f"{imageBaseURL}/{backdropSize}{backdropPath}"
    return None

def formatMovie(movie):
    return {
        'id': movie.get('id'),
        'title': movie.get('title'),
        'overview': movie.get('overview'),
        'poster_url': getPosterURL(movie.get('poster_path')),
        'backdrop_url': getBackdropURL(movie.get('backdrop_path')),
        'release_date': movie.get('release_date'),
        'rating': movie.get('vote_average'),
        'vote_count': movie.get('vote_count'),
        'popularity': movie.get('popularity'),
        'genre_ids': movie.get('genre_ids', [])
    }

def searchMovie(query):
    
    url = f"{baseURL}/search/movie"
    
    params = {
        "api_key": apiKey,
        "query": query,
        "language": "en-US",
        "page": 1
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        movies = data.get("results", [])
        return [formatMovie(m) for m in movies]
    else:
        print(f"Error: {response.status_code}")
        return []

def getMovie(movieID):
    
    url = f"{baseURL}/movie/{movieID}"
    
    params = {
        "api_key": apiKey,
        "language": "en-US"
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        movie = response.json()
        return formatMovie(movie)
    else:
        return None
