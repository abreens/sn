###
#
# Les 17 - HTTP requests & Cookies
#
# <TBC>
#
###

import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():

    # PLAYGROUND - Jinja variables
    some_text = "Message from the handler."
    current_year = datetime.datetime.now().year

    cities = ["Boston", "Vienna", "Paris", "Berlin"]

    # Connect handler to /index.html
    return render_template("index.html", some_text=some_text, current_year=current_year, cities=cities)


@app.route("/about", methods=["GET"])
def about_me():
    # Connect handler to /about/about_me.html
    return render_template("about_me.html")


@app.route("/portfolio")
def portfolio():
    # Connect handler to /portfolio/portfolio.html
    return render_template("/portfolio.html")


if __name__ == '__main__':
    app.run()
