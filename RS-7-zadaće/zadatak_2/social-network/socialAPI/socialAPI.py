from fastapi import FastAPI, HTTPException
from models.models import createPost,Post, UserRequest
from typing import List
import aiohttp

posts = []

app = FastAPI()

@app.post("/objava",response_model=Post)
def create_post(create_post: createPost):
    new_id = len(posts)+1
    new_post=Post(
        id=new_id,
        korisnik=create_post.korisnik,
        tekst=create_post.tekst,
        vrijeme=create_post.vrijeme
    )
    posts.append(new_post)
    return new_post
    
@app.get("/objava/{id}",response_model=Post)
def get_post_by_id(id: int):
    for post in posts:
        if post.id == id:
            return post
    raise HTTPException(status_code=404, detail="Objava nije pronađena")

@app.post("/korisnici/{korisnik}/objave", response_model=List[Post])
async def get_posts_by_user(korisnik: str, auth_request: UserRequest):
    if not await provjeri_korisnika(auth_request.username, auth_request.password):
        raise HTTPException(status_code=404, detail="Greška")

    user_posts = [post for post in posts if post.korisnik == korisnik]
    if not user_posts:
        raise HTTPException(status_code=404, detail=f"Ne postoje objave za korisnika {korisnik}")
    return user_posts



async def provjeri_korisnika(username: str, password: str) -> bool:
    async with aiohttp.ClientSession() as session:
        async with session.post("http://authapi:8000/dummy_login", json={"username": username, "password": password}) as response:
            if response.status == 200:
                return True
            return False

        