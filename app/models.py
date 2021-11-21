from sqlalchemy import Column, Intenger, String, Boolean
from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Intenger, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True)