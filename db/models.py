from sqlalchemy.orm import relationship

from .database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.schema import ForeignKey


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    posts = relationship("Post", back_populates="user")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime)
    creator_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="posts")
