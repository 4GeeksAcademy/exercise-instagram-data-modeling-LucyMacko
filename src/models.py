from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    
    ID = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column (String(250), nullable=False)
    lastname = Column (String(250), nullable=False)
    email = Column(String(250), nullable=False, primary_key=True, unique= True )

#done
class Post(Base):
    __tablename__ = 'Post'
    
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.ID'))

#done
class Media(Base):
    __tablename__ = 'Media'
    
    ID = Column(Integer, primary_key=True)
    type = Column(Enum)
    url = Column(String)
    post_id = Column(Integer, ForeignKey('Post.ID'))     

#done
class Comment(Base):
    __tablename__ = 'Comment'
    
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String, nullable=False)
    author_id= Column(Integer, ForeignKey('User.ID'))
    post_id = Column(Integer, ForeignKey('Post.ID'))
   
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
