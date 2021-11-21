from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(BaseModel):
    id: int
    title: str
    content: str
    published: str
    created_at: datetime

    class Config:
        orm_mode = True