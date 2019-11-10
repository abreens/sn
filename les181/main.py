###
#
# Exercise 18.1 - Update the Guess a secret number game
#
# Now that you've learned how to save an object into a database and read from it, you can update the
# "Guess a secret number" game.
#
# Your user model should have the following fields:
#   id (integer)
#   name (string)
#   email (string)
#   secret_number (integer)
#
# The secret_number field will hold the secret number that user has to guess.
#
###

import random
from flask import Flask, render_template, request, redirect, url_for, make_response
from models import User, db

app = Flask(__name__)
db.create_all()  # create (new) tables in the database


@app.route("/", methods=["GET"])
def index():
    # Een eMail adres uit cookie "email" lezen
    email_address = request.cookies.get("email")

    if email_address:
        # Cookie bestaat, haal gebruikersgegevens op uit de databank
        user = db.query(User).filter_by(email=email_address).first()
    else:
        # Cookie bestaat niet, initialiseer de gebruiker op None
        user = None

    return render_template("index.html", user=user)


@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("user-name")
    email = request.form.get("user-email")

    # see if user already exists
    user = db.query(User).filter_by(email=email).first()

    if not user:
        # create a User object
        secret_number = random.randint(1, 30)
        user = User(name=name, email=email, secret_number=secret_number)

        # save the user object into a database
        db.add(user)
        db.commit()

    # save user's email into a cookie
    response = make_response(redirect(url_for('index')))
    response.set_cookie("email", email)

    return response


@app.route("/result", methods=["POST"])
def result():
    # get user from the database based on his / her eMail address from cookie "email"
    email_address = request.cookies.get("email")
    user = db.query(User).filter_by(email=email_address).first()

    # Invoer komende van index.html lezen
    invoer = request.form.get("guess")
    code = "NOK"

    try:
        guess = int(invoer)
    except ValueError:
        # Foutieve invoer opvangen
        message = "Dat was geen (geheel) getal. Probeer aub opnieuw..."
        return render_template("result.html", message=message, code=code)
    else:
        # De invoer was een geheel getal
        if 1 <= guess <= 30:
            # De invoer ligt tussen 1 en 30
            if guess == user.secret_number:
                message = "Het geheime nummer is inderdaad " + str(user.secret_number) + ". " + \
                          "Een nieuw geheim nummer wordt ingesteld..."
                code = "OK"
                response = make_response(render_template("result.html", message=message, code=code))

                # Een nieuw geheim nummer initialiseren
                new_secret = random.randint(1, 30)
                user.secret_number = new_secret

                # Update the user object in the database
                db.add(user)
                db.commit()

                return response

            elif guess > user.secret_number:
                message = "Your guess is not correct... try something smaller."
                return render_template("result.html", message=message, code=code)
            elif guess < user.secret_number:
                message = "Your guess is not correct... try something bigger."
                return render_template("result.html", message=message, code=code)
        else:
            # Out of bounds
            message = "Het getal moet tussen 1 en 30 liggen. Probeer aub opnieuw..."
            return render_template("result.html", message=message, code=code)


@app.route("/reset_user")
def reset_user():
    # Cookie "email" deleten
    response = make_response(render_template("index.html"))
    response.set_cookie("user_name", expires=0)

    return response


if __name__ == '__main__':
    app.run(debug=True)
