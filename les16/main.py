###
#
# Les 16 - Flask Home Page with Jinja Templates
#
# Use Jinja to improve the HTML templates in your Homepage web app. Then deploy your homepage to Heroku (via GitHub).
#
###

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    # Connect handler to /index.html
    return render_template("index.html")


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
