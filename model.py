from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker

ENGINE = None
Session = None

Base = declarative_base()

### Class declarations go here
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key = True)
    age = Column(Integer, nullable = True)
    gender = Column(String(1), nullable=True)
    occupation = Column(String(64), nullable=True)
    zipcode = Column(String(5), nullable=True)

class Movie(Base):
    import datetime
    __tablename__= "movies"     #when do we use u.item instead of "movie?"

    id = Column(Integer, primary_key = True)
    name = Column(String(64), nullable = True)
    released_at = Column(Date(), nullable = True)   # look up in tutorial
    imdb_url = Column(String(64), nullable = True)

class Rating(Base):             #u.data = "rating" ??
    __tablename__ = "ratings"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, nullable = True)
    movie_id = Column(Integer, nullable = True)
    rating = Column(Integer, nullable = True)
    timestamp = Column(Integer, nullable = True)

### End class declarations

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo=False)
    Session = sessionmaker(bind=ENGINE)

    return Session()


def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
