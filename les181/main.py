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


@app.route("/", methods=["GET"])
def index():
    # Het geheime nummer inlezen
    secret_number = request.cookies.get("secret_number")
    response = make_response(render_template("index.html"))

    # Checken of het geheime nummer bestaat
    if not secret_number:
        # Create new cookie
        new_secret = random.randint(1, 30)
        response.set_cookie("secret_number", str(new_secret))

    return response


@app.route("/result", methods=["POST"])
def result():
    secret_number = int(request.cookies.get("secret_number"))
    invoer = request.form.get("guess")

    try:
        guess = int(invoer)
    except ValueError:
        # Foutieve invoer opvangen
        message = "Dat was geen (geheel) getal. Probeer aub opnieuw..."
        error_code = "NOK"
        return render_template("result_error.html", message=message, error_code=error_code)
    else:
        # De invoer was een geheel getal
        if 1 <= guess <= 30:
            # De invoer ligt tussen 1 en 30
            if guess == secret_number:
                message = "Het geheime nummer is inderdaad " + str(secret_number) + ". " + \
                          "Een nieuw geheim nummer wordt ingesteld..."
                response = make_response(render_template("result_success.html", message=message))
                # Een nieuw geheim nummer initialiseren
                response.set_cookie("secret_number", str(random.randint(1, 30)))
                return response
            elif guess > secret_number:
                message = "Your guess is not correct... try something smaller."
                return render_template("result_error.html", message=message)
            elif guess < secret_number:
                message = "Your guess is not correct... try something bigger."
                return render_template("result_error.html", message=message)
        else:
            # Out of bounds
            message = "Het getal moet tussen 1 en 30 liggen. Probeer aub opnieuw..."
            return render_template("result_error.html", message=message)


if __name__ == '__main__':
    app.run(debug=True)
