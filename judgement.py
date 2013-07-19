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
    return render_template("index.html", users=user_list)


# ASSIGNMENT: build out some CRUDL-style views for User and Ratings objects
# be able to create a new user
@app.route("/add_user")
def add_user():
    age = request.args.get("age")
    gender = request.args.get("gender")
    occupation = request.args.get("occupation")
    zipcode = request.args.get("zipcode")
    user = model.User(age=age, gender=gender, occupation=occupation, zipcode=zipcode)
    model.session.add(user)
    model.session.commit()
    return render_template("user_added.html", user_id=user.user_id)

# view a list of users
@app.route("/users")
def show_users():
    user_list = model.session.query(model.User).all()
    return render_template("users.html", users=user_list)

# click on a user and view list of movies they've rated, as well as the ratings
@app.route("/user_ratings")
def show_user_ratings(user_id):
    ratings_list = model.session.query(model.Ratings).filter_by(user_id=user_id)
    return render_template("user_ratings.html", user_id=user_id, ratings_list=ratings_list)

# be able to log in as a user
# when logged in, be able to add or update a personal rating for a movie.

if __name__== "__main__":
    app.run(debug=True)