# Flask portion of our movie ratings app
# Becca Bruggman and Gowri Grewal
# Hackbright Day 23 7.18.13
"""
model.py has the Class and model for this app
seed.py loads the seed data in the database
ratings.db is the database, and there are 3 tables: users, movies and ratings

ASSIGNMENT: build out some CRUDL-style views for User and Ratings objects
be able to create a new user
"""
from flask import Flask, render_template, redirect, request
import model

app = Flask(__name__)

@app.route("/")
def index():
    movie_list = model.session.query(model.Movie).all()
    return render_template("index.html", movies=movie_list)

@app.route("/login")
def login():
    user_id = request.args.get("user_id")
    password = request.args.get("password")
    ratings_list = model.session.query(model.Rating).filter_by(user_id=user_id).order_by(model.Rating.movie_id)
    return render_template("loggedin.html", user_id=user_id, ratings_list=ratings_list)

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
    # ratings_list = model.session.query(model.Rating).all()
    return render_template("users.html", users=user_list)

# click on a user and view list of movies they've rated, as well as the ratings
@app.route("/user_ratings")
def show_user_ratings():
    user_id = request.args.get("user_id")
    ratings_list = model.session.query(model.Rating).filter_by(user_id=user_id).order_by(model.Rating.movie_id)
    return render_template("user_ratings.html", user_id=user_id, ratings_list=ratings_list)

# when logged in, be able to add or update a personal rating for a movie.
@app.route("/change_rating")
def change_rating():
    movie_id=request.args.get("movie_id")
    movie_name=model.session.query(model.Movie).get(movie_id)
    user_id=request.args.get("user_id")
    rating=request.args.get("rating")
    rating=model.Rating(id=id, user_id=user_id, movie_id=movie_id, rating=rating)
    model.session.add(rating)
    model.session.commit()
    return render_template("change_rating.html", movie_id=movie_id, movie_name=movie_name, user_id=user_id)

@app.route("/add_rating")
def add_rating():
    user_id = request.args.get("user_id")
    return render_template("add_rating.html", user_id=user_id)


if __name__== "__main__":
    app.run(debug=True)