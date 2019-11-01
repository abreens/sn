###
#
# Les 16 - Flask Home Page with Jinja Templates
#
# Use Jinja to improve the HTML templates in your Homepage web app. Then deploy your homepage to Heroku (via GitHub).
#
###

import datetime

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():

    # PLAYGROUND - Jinja variables
    some_text = "Message from the handler."
    current_year = datetime.datetime.now().year

    cities = ["Boston", "Vienna", "Paris", "Berlin"]

    # Connect handler to /index.html
    return render_template("index.html", some_text=some_text, current_year=current_year, cities=cities)


@app.route("/about", methods=["GET", "POST"])
def about_me():

    if request.method == "GET":
        # Connect handler to /about/about_me.html
        return render_template("about_me.html")

    elif request.method == "POST":
        contact_name = request.form.get("contact-name")
        contact_email = request.form.get("contact-email")
        contact_message = request.form.get("contact-message")

        print(contact_name)
        print(contact_email)
        print(contact_message)

        return render_template("success.html")


@app.route("/portfolio")
def portfolio():
    # Connect handler to /portfolio/portfolio.html
    return render_template("/portfolio.html")


if __name__ == '__main__':
    app.run(debug=True)
