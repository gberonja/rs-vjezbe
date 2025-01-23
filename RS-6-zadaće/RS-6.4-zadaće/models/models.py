from typing import List, Optional, Literal
from pydantic import BaseModel, field_validator


class Actor(BaseModel):
    name: str
    surname: str


class Writer(BaseModel):
    name: str
    surname: str


class Movie(BaseModel):
    Title: str
    Year: str
    imdbID: str
    Rated: Optional[str] = "N/A"
    Released: Optional[str] = "N/A"
    Runtime: str
    Genre: str
    Language: str
    Country: str
    Actors: List[Actor]
    Plot: str
    Writer: List[Writer]
    Type: Literal["movie", "series"]
    Images: Optional[List[str]] = []
    Awards: Optional[str] = "No awards information"
    Poster: Optional[str] = None
    imdbRating: Optional[str]
    imdbVotes: Optional[str]
    totalSeasons: Optional[int] = None
    ComingSoon: Optional[bool] = False

    @field_validator("Year")
    def validate_year(cls, year):
        if len(year) >= 4 and year[:4].isdigit():
            year_int = int(year[:4])
            if year_int <= 1900:
                raise ValueError(f"Year must be greater than 1900, got {year_int}")
        else:
            raise ValueError(f"Year must start with a valid 4-digit number, got {year}")
        return year
    
    @field_validator("Runtime")
    def validate_runtime(cls, runtime):
        if runtime == "N/A": 
            return runtime
        if runtime and runtime[0].isdigit():
            if int(runtime[0]) <= 0:
                raise ValueError(f"Runtime must start with a number greater than 0, got {runtime}")
        else:
            raise ValueError(f"Runtime must start with a valid number or be 'N/A', got {runtime}")
        return runtime
    
    @field_validator("imdbRating")
    def validate_imdb_rating(cls, rating):
        if rating == "N/A":
            return rating
        try:
            rating_float = float(rating)
            if not (0 <= rating_float <= 10):
                raise ValueError(f"imdbRating must be between 0 and 10, got {rating}")
        except ValueError:
            raise ValueError(f"imdbRating must be a valid number or 'N/A', got {rating}")
        return rating

    @field_validator("imdbVotes")
    def validate_imdb_votes(cls, votes):
        if votes == "N/A":
            return votes
        try:
            votes_int = int(votes.replace(",", ""))
            if votes_int <= 0:
                raise ValueError(f"imdbVotes must be greater than 0, got {votes}")
            return votes_int
        except ValueError:
            raise ValueError(f"imdbVotes must be a valid number or 'N/A', got {votes}")

    @field_validator("Actors", mode="before")
    def split_actors(cls, actors):
        if isinstance(actors, str):
            actor_list = []
            for actor in actors.split(","):
                name_parts = actor.strip().split(" ")
                if len(name_parts) >= 2:
                    actor_list.append(Actor(name=name_parts[0], surname=" ".join(name_parts[1:])))
                else:
                    actor_list.append(Actor(name=name_parts[0], surname=""))
            return actor_list
        return actors

    @field_validator("Writer", mode="before")
    def split_writers(cls, writers):
        if isinstance(writers, str):
            writer_list = []
            for writer in writers.split(","):
                name_parts = writer.strip().split(" ")
                if len(name_parts) >= 2:
                    writer_list.append(Writer(name=name_parts[0], surname=" ".join(name_parts[1:])))
                else:
                    writer_list.append(Writer(name=name_parts[0], surname=""))
            return writer_list
        return writers