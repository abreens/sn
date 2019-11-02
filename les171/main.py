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

import datetime

from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route("/")
def index():
    # Connect handler to /index.html
    return render_template("index.html")

@app.route("/result")
def result():
    # Connect handler to /result.html
    return render_template("result.html")

if __name__ == '__main__':
    app.run(debug=True)
