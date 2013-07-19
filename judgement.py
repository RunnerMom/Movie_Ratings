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
    user_list = model.session.query(model.User).all()
    return render_template("user_list.html", users=user_list)

if __name__== "__main__":
    app.run(debug=True)
