from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import auth, post, user, vote

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

app.include_router(auth.router, prefix="/api/v1")
app.include_router(post.router, prefix="/api/v1")
app.include_router(user.router, prefix="/api/v1")
app.include_router(vote.router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "Bienvenido a la demo de fastapi!!!!"}
