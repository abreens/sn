###
#
# Les 17 - Flask application with Jinja templates, HTTP requests and Cookies
#
###

import datetime

from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route("/")
def index():

    some_text = "Message from the handler."
    current_year = datetime.datetime.now().year

    cities = ["Boston", "Vienna", "Paris", "Berlin"]

    # Connect handler to /index.html
    return render_template("index.html", some_text=some_text, current_year=current_year, cities=cities)


@app.route("/about", methods=["GET", "POST"])
def about_me():
    if request.method == "GET":
        user_name = request.cookies.get("user_name")
        return render_template("about_me.html", name=user_name)

    elif request.method == "POST":
        contact_name = request.form.get("contact-name")
        contact_email = request.form.get("contact-email")
        contact_message = request.form.get("contact-message")

        print(contact_name)
        print(contact_email)
        print(contact_message)

        response = make_response(render_template("success.html"))
        response.set_cookie("user_name", contact_name)

        return response


@app.route("/portfolio")
def portfolio():
    # Connect handler to /portfolio/portfolio.html
    return render_template("/portfolio.html")


if __name__ == '__main__':
    app.run()
