import model
import csv
import time
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker


# def load_users(session):
#     # open file
#     # read file
#     #parse a line
#     #create an object
#     # add object to a session
#     # commit
#     # repeat until done
#     with open('seed_data/u.user') as csvfile:
#         userdata = csv.reader(csvfile, delimiter='|')
#         for row in userdata:
#             user_record = model.User(age=row[1], zipcode=row[4])
#             session.add(user_record)
#         session.commit()

def load_movies(session):
    # use u.item
    with open('seed_data/u.itemtest') as csvfile:
        movie_data = csv.reader(csvfile, delimiter='|')
        for row in movie_data:

            row_time = row[2]

            if row_time != "%d-%b-%Y"
                continue
            else:
                get_date = (time.strptime(row_time, "%d-%b-%Y"))
                print type(get_date)

                last_date = datetime.fromtimestamp(time.mktime(get_date))
                print type(last_date)
                # movie_record = model.Movie(name=row[1], released_at=(last_date), imdb_url=row[3])
            #     session.add(movie_record)
            # session.commit()

# def load_ratings(session):
#     # use u.data
#     pass

def main(session):
    # You'll call each of the load_* functions with the session as an argument
   # load_users(session)
    load_movies(session)

if __name__ == "__main__":
    s= model.connect()
    main(s)
