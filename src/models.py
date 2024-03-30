import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy import Table

Base = declarative_base()

follower_association = Table(
    'follower_association', Base.metadata,
    Column('user_from_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('user_to_id', Integer, ForeignKey('follower.id'), primary_key=True)
)

class Follower(Base):
    __tablename__ = 'follower'

    id = Column(Integer, primary_key=True)

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    name = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250))
    followers = relationship("Follower", backref="user", lazy=True)

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(String(250), ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(250), ForeignKey('user.id'))


class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True)
    media_type = Column(Enum)
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
