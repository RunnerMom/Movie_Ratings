import model
import csv
import time
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker

def convert_date_string(date_string):
    # print date_string
    dt = datetime.strptime(date_string, "%d-%b-%Y")
 
    return dt.date()

def load_users(session):
    # open file
    # read file
    #parse a line
    #create an object
    # add object to a session
    # commit
    # repeat until done
    with open('seed_data/u.user') as csvfile:
        userdata = csv.reader(csvfile, delimiter='|')
        for row in userdata:
            user_record = model.User(user_id=row[0], age=row[1], gender=row[2] , occupation=row[3], zipcode=row[4])
            session.add(user_record)
        session.commit()

def load_movies(session):
    # use u.item
    with open('seed_data/u.itemtest') as csvfile:
        movie_data = csv.reader(csvfile, delimiter='|')
        print ("Loading movie db. This could take several minutes")
        for row in movie_data:

            row_time = row[2]   #this is the non-formatted datetime
            row_name = row[1]   #this is the movie title
            row_name = row_name.decode("latin-1")   #this gets rid of accents
            row_name_list = row_name.split(' ')     #creates a list
            
            if len(row_name_list) > 1:      # if title + year, then pop off the year and save the title only
                row_name_list.pop()
                movie_title = " ".join(row_name_list)
            else:
                movie_title = " ".join(row_name_list)  #if title only, convert back to string

            # try to make an error handler to skip data that does not have proper date formatting

            if row_time:
                # last_date = convert_date_string(row_time) #creates a Python datetime object
                # print last_date, type(last_date)
                movie_record = model.Movie(id = row[0], name=movie_title, released_at=datetime.strptime(row_time, "%d-%b-%Y").date(), imdb_url=row[4]) #populates movie record
                session.add(movie_record)
            session.commit()

def load_ratings(session):
    # use u.data
    with open('seed_data/u.data') as csvfile:
        ratings_data = csv.reader(csvfile, delimiter='\t')
        for row in ratings_data:

            row_timestamp=row[3]

           #  print type(row_timestamp)
            ratings_record = model.Rating(user_id=row[0], movie_id=row[1], rating=row[2], timestamp=row_timestamp)
            session.add(ratings_record)
        session.commit()
           
def main(session):
    # You'll call each of the load_* functions with the session as an argument
    # load_users(session)
    load_movies(session)
    # load_ratings(session)

if __name__ == "__main__":
    s= model.connect()
    main(s)
