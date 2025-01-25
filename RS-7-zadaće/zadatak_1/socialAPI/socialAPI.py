from fastapi import FastAPI, HTTPException
from models.models import createPost,Post
from typing import List

posts = []

app = FastAPI()

@app.post("/objava",response_model=Post)
def create_post(post: createPost):
    new_id = len(posts)+1
    new_post=Post(
        id=new_id,
        korisnik=post.korisnik,
        tekst=post.tekst,
        vrijeme=post.vrijeme
    )
    posts.append(new_post)
    return new_post
    
@app.get("/objava/{id}",response_model=Post)
def get_post_by_id(id: int):
    for post in posts:
        if post.id == id:
            return post
    raise HTTPException(status_code=404, detail="Objava nije pronađena")

@app.get("/korisnici/{korisnik}/objave", response_model=List[Post])
def get_posts_by_user(korisnik: str):
    user_posts=[post for post in posts if post.korisnik == korisnik]
    if not user_posts:
        raise HTTPException(status_code=404, detail=f"Ne postoje objave za korisnika {korisnik}")
    return user_posts