from fastapi import FastAPI
from db import models
from db.database import engine
from routers import user, post, comment
from fastapi.staticfiles import StaticFiles
from authentication import auth

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"Hello World"}



models.Base.metadata.create_all(engine)
app.mount("/images", StaticFiles(directory="images"), name="images")