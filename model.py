from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session
from sqlalchemy import ForeignKey

engine = create_engine("sqlite:///ratings.db", echo=False)
session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

Base = declarative_base()
Base.query = session.query_property()

""" 
The 3 classes below are tables in our ratings.db
"""
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    age = Column(Integer, nullable=True)
    gender = Column(String(1), nullable=True)
    occupation = Column(String(64), nullable=True)
    zipcode = Column(String(5), nullable=True)

class Movie(Base):
    import datetime
    __tablename__= "movies"     #when do we use u.item instead of "movie?"

    id = Column(Integer, primary_key = True)
    name = Column(String(64), nullable = True)
    released_at = Column(Date, nullable = True)   # look up in tutorial
    imdb_url = Column(String(64), nullable = True)

class Rating(Base):             #u.data = "rating" ??
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=True)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=True)
    rating = Column(Integer, nullable=True)
    timestamp = Column(DateTime, nullable=True)

    user = relationship("User", backref=backref("ratings", order_by=id))
    movie = relationship("Movie", backref=backref("ratings", order_by=id))
### End class declarations


def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
