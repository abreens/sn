###
#
# Les 18 - Database
#
###

from flask import Flask, render_template, request, redirect, url_for, make_response
from models import User, db

app = Flask(__name__)
db.create_all() # create (new) tables in the database


@app.route("/")
def index():
    email_address = request.cookies.get("email")

    # get user from the database based on email address
    user = db.query(User).filter_by(email=email_address).first()

    print("Hello")
    print("De user is: " + user.name)

    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("user-name")
    email = request.form.get("user-email")

    # create a User object
    user = User(name=name, email=email)

    # save the user object into a database
    db.add(user)
    db.commit()

    # save user's email into a cookie
    response = make_response(redirect(url_for('index')))
    response.set_cookie("email", email)

    return response


if __name__ == '__main__':
    app.run(debug=True)
