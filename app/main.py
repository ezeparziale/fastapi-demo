from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote

# models.Base.metadata.create_all(bind=engine)

origins = ["*"]  # "*" para DEV, completar con URL productiva para PROD

app = FastAPI(
    title="FastApi-Demo-1",
    description="""
    # Fast Api Demo :rocket:
    """,
    version="1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Bienvenido a la demo de fastapi!!!!"}
