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

@app.route("/profile/delete", methods=["GET"])
def profile_delete():
    return render_template("profile_delete.html")

@app.route("/result", methods=["POST"])
def result():
    # get user from the database based on his / her session token from cookie "session_token"
    session_token = request.cookies.get("session_token")
    user = db.query(User).filter_by(session_token=session_token).first()

    # Invoer komende van index.html lezen
    invoer = request.form.get("guess")
    code = "NOK"

    try:
        guess = int(invoer)
    except ValueError:
        # Foutieve invoer opvangen
        message = "Dat was geen (geheel) getal. Probeer aub opnieuw..."
        return render_template("result.html", user=user, message=message, code=code)
    else:
        # De invoer was een geheel getal
        if 1 <= guess <= 30:
            # De invoer ligt tussen 1 en 30
            if guess == user.secret_number:
                message = "Het geheime nummer is inderdaad " + str(user.secret_number) + ". " + \
                          "Een nieuw geheim nummer wordt ingesteld..."
                code = "OK"
                response = make_response(render_template("result.html", user=user, message=message, code=code))

                # Een nieuw geheim nummer initialiseren
                new_secret = random.randint(1, 30)
                user.secret_number = new_secret

                # Update the user object in the database
                db.add(user)
                db.commit()

                return response

            elif guess > user.secret_number:
                message = "Your guess is not correct... try something smaller."
                return render_template("result.html", user=user, message=message, code=code)
            elif guess < user.secret_number:
                message = "Your guess is not correct... try something bigger."
                return render_template("result.html", user=user, message=message, code=code)
        else:
            # Out of bounds
            message = "Het getal moet tussen 1 en 30 liggen. Probeer aub opnieuw..."
            return render_template("result.html", user=user, message=message, code=code)


@app.route("/logout")
def reset_user():
    # Cookie session_token deleten zodat er terug moet worden ingelogged
    response = make_response(redirect(url_for('index')))
    response.set_cookie("session_token", expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
