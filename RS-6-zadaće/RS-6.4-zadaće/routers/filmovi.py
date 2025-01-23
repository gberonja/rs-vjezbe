from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional, Literal
from data_loader import load_movies
from models.models import Movie


movies = load_movies("film.json")

router = APIRouter()

@router.get("/movies", response_model=List[Movie])
def get_all_movies(
    min_year: Optional[int] = Query(None, ge=1900, description="Minimum release year of the movie"),
    max_year: Optional[int] = Query(None, ge=1900, description="Maximum release year of the movie"),
    min_rating: Optional[float] = Query(None, ge=0.0, le=10.0, description="Minimum IMDb rating of the movie"),
    max_rating: Optional[float] = Query(None, ge=0.0, le=10.0, description="Maximum IMDb rating of the movie"),
    type: Optional[Literal["movie", "series"]] = Query(None, description="Type of content: 'movie' or 'series'")
):
    filtered_movies = movies
    
    
    def extract_max_year(year: str) -> Optional[int]:
        # Pomoćna funkcija zbog problema s godinama (string)
        if "-" in year:
            parts = year.split("-")
            if parts[-1].isdigit(): 
                return int(parts[-1])
            elif parts[0].isdigit(): 
                return int(parts[0])
        elif year.isdigit(): 
            return int(year)
        return None

    # Min Year
    if min_year is not None:
        filtered_movies = [
            movie for movie in filtered_movies
            if movie.Year[:4].isdigit() and int(movie.Year[:4]) >= min_year
        ]

    # Max Year
    if max_year is not None:
        filtered_movies = [
            movie for movie in filtered_movies
            if movie.Year[:4].isdigit() and int(movie.Year[:4]) <= max_year
        ]
        
    # Min Rating
    if min_rating is not None:
        filtered_movies = [
            movie for movie in filtered_movies
            if movie.imdbRating != "N/A" and float(movie.imdbRating) >= min_rating
        ]

    # Max Rating
    if max_year is not None:
        filtered_movies = [
            movie for movie in filtered_movies
            if (parsed_year := extract_max_year(movie.Year)) is not None and parsed_year <= max_year
        ]
        
    # Type  
    if type is not None:
        filtered_movies = [
            movie for movie in filtered_movies
            if movie.Type.lower() == type.lower()
        ]
        
    if not filtered_movies:
        raise HTTPException(status_code=404, detail="No movies found matching the given filters.")

    return filtered_movies


@router.get("/movies/{imdb_id}", response_model=Movie)
def get_movie_by_imdb_id(imdb_id: str):
    """Retrieve a movie by its IMDb ID."""
    for movie in movies:
        if movie.imdbID == imdb_id:
            return movie
    raise HTTPException(status_code=404, detail=f"Movie with IMDb ID {imdb_id} not found.")

@router.get("/movies/title/{title}", response_model=Movie)
def get_movie_by_title(title: str):
    """Retrieve a movie by its title."""
    for movie in movies:
        if movie.Title.lower() == title.lower():
            return movie
    raise HTTPException(status_code=404, detail=f"Movie with title '{title}' not found.")
