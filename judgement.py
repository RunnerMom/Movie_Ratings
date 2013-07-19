# Flask portion of our movie ratings app
# Becca Bruggman and Gowri Grewal
# Hackbright Day 23 7.18.13

# model.py has the Class and model for this app
# seed.py loads the seed data in the database
# ratings.db is the database, and there are 3 tables: users, movies and ratings

from flask import Flask, render_template, redirect, request
import model

app = Flask(__name__)

@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(20).all()
    return render_template("user_list.html", users=user_list)

if __name__== "__main__":
    app.run(debug=True)
# ASSIGNMENT: build out some CRUDL-style views for User and Ratings objects
# be able to create a new user
# view a list of users
# click on a user and view list of movies they've rated, as well as the ratings
# be able to log in as a user
# when logged in, be able to add or update a personal rating for a movie.