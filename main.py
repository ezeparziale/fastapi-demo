from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/create_posts")
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"title {payLoad['title']} content: {payLoad['content']}"}