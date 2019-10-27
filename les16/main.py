###
#
# Les 16 - Flask Home Page with Jinja Templates
#
# Use Jinja to improve the HTML templates in your Homepage web app. Then deploy your homepage to Heroku (via GitHub).
#
###

import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    some_text = "Message from the handler."
    current_year = datetime.datetime.now().year

    # Connect handler to /index.html
    return render_template("index.html", some_text=some_text, current_year=current_year)


@app.route("/about")
def about_me():
    # Connect handler to /about/about_me.html
    return render_template("about_me.html")


@app.route("/portfolio")
def portfolio():
    # Connect handler to /portfolio/portfolio.html
    return render_template("/portfolio.html")


if __name__ == '__main__':
    app.run()
