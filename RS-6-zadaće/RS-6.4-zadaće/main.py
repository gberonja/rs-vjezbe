from fastapi import FastAPI
from routers.filmovi import router

app = FastAPI()

app.include_router(router)
