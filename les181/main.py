###
#
# Les 17.1 - Guess the secret number game
#
# Create a new Flask web app that will have a GET and a POST request handler.
# They can be both in one handler, or each in a separate handler (it doesn't matter).
#
# In the GET handler you'll do the following things:
#   Check if there's a cookie with the name "secret_number".
#   If there isn't any such cookie, create a new cookie with this name.
#   The new cookie should store a random number between 1 and 30.
#
# The POST handler should do the following:
#   Get the secret_number cookie.
#   Get the user's guess from the HTML form.
#   Compare the guess and the secret_number
#   If the guess is the same as the secret number, set a new random number in the cookie and return the user a
#   result.html page with a congrats message.
#   If not, return the user the result.html page with a message saying whether the guess was too big or too small.
#
###

import random
from flask import Flask, render_template, request, make_response

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
        return render_template("result_error.html", message=message)
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
    app.run()
