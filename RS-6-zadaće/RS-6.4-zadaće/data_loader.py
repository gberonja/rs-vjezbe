import json
import os
from models.models import Movie

def load_movies(file_name: str) -> list[Movie]:
    # Zbog očito nekih problema s mojim VSCodeom, morao sam na kraju
    # ovako pročitati json file
    current_dir = os.path.dirname(os.path.abspath(__file__)) 
    file_path = os.path.join(current_dir, file_name)

    with open(file_path, 'r', encoding='utf-8') as data_file:
        data = json.load(data_file)

    movies = []
    for item in data:
            movie = Movie(**item)
            movies.append(movie)
    return movies
