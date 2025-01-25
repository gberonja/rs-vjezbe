from pydantic import BaseModel, Field
from datetime import datetime

class Post(BaseModel):
    id: int
    korisnik: str = Field(max_length=20)
    tekst: str = Field(max_length=280)
    vrijeme: datetime
    
class createPost(BaseModel):
    korisnik: str = Field(max_length=20)
    tekst: str = Field(max_length=280)
    vrijeme: datetime
    
