###
#
# Les 21 - Must-have features: edit, delete, list all, details
#
###

import random
import uuid
import hashlib
from flask import Flask, render_template, request, redirect, url_for, make_response
from models import User, db

app = Flask(__name__)
db.create_all()  # create (new) tables in the database


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/index", methods=["GET"])
def index():
    # Session token uit cookie "session_token" lezen
    session_token = request.cookies.get("session_token")

    if session_token:
        # Cookie bestaat, haal gebruikersgegevens op uit de databank
        user = db.query(User).filter_by(session_token=session_token).first()
    else:
        # Cookie bestaat niet, initialiseer de gebruiker op None
        user = None

    return render_template("index.html", user=user)


@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("user-name")
    email = request.form.get("user-email")
    password = request.form.get("user-password")

    # hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # see if user already exists
    user = db.query(User).filter_by(email=email).first()

    if not user:
        # create a User object
        secret_number = random.randint(1, 30)
        user = User(name=name, email=email, secret_number=secret_number, password=hashed_password)
        # save the user object into a database
        db.add(user)
        db.commit()

    # Check if password matches.
    if hashed_password != user.password:
        message = "Go back and try again."
        code = "wrong_pwd"
        return render_template("result.html", message=message, code=code)

    elif hashed_password == user.password:
        # Create a random session token for this user
        session_token = str(uuid.uuid4())
        # Save the session token in the database
        user.session_token = session_token
        db.add(user)
        db.commit()
        # save user's session token into a cookie
        response = make_response(redirect(url_for('index')))
        response.set_cookie("session_token", session_token, httponly=True, samesite='Strict')
        return response


@app.route("/profile", methods=["GET"])
def profile():
    session_token = request.cookies.get("session_token")

    # get user from the database based on her/his email address
    user = db.query(User).filter_by(session_token=session_token).first()

    if user:
        return render_template("profile.html", user=user)
    else:
        return render_template("index.html", user=user)


@app.route("/profile/edit", methods=["GET", "POST"])
def profile_edit():
    session_token = request.cookies.get("session_token")

    # get user from the database based on her/his email address
    user = db.query(User).filter_by(session_token=session_token).first()

    if request.method == "GET":
        if user:  # if user is found
            return render_template("profile_edit.html", user=user)
        else:
            return render_template("index.html", user=user)

    elif request.method == "POST":
        name = request.form.get("profile-name")
        email = request.form.get("profile-email")

        # update the user object
        user.name = name
        user.email = email

        # store changes into the database
        db.add(user)
        db.commit()

        return redirect(url_for("profile"))


@app.route("/profile/delete", methods=["GET", "POST"])
def profile_delete():
    session_token = request.cookies.get("session_token")

    # get user from the database based on her/his email address
    user = db.query(User).filter_by(session_token=session_token).first()

    if request.method == "GET":
        if user:  # if user is found
            return render_template("profile_delete.html", user=user)
        else:
            return render_template("index.html", user=user)

    elif request.method == "POST":
        # delete the user in the database
        db.delete(user)
        db.commit()
        return redirect(url_for("index"))


@app.route("/users", methods=["GET"])
def all_users():
    users = db.query(User).all()

    return render_template("users.html", users=users)


@app.route("/user/<user_id>", methods=["GET"])
def user_details(user_id):
    user = db.query(User).get(int(user_id))  # .get() can help you query by the ID

    return render_template("user_details.html", user=user)


@app.route("/logout")
def reset_user():
    # Cookie session_token deleten zodat er terug moet worden ingelogged
    response = make_response(redirect(url_for('index')))
    response.set_cookie("session_token", expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
