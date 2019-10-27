###
#
# Les 16 - Flask Home Page with Jinja Templates
#
# Create a new Flask web app which will serve as your personal website. It should have the following pages:
#    Index page (/), where you say hello to the visitors
#    About me page (/about)
#    Portfolio page (/portfolio): contains links to sub-pages with your front-end projects
#
# The Portfolio page should have links to the HTML&CSS pages (projects) that you've created in the front-end
# part of this course:
#    Fakebook (/portfolio/fakebook)
#    Boogle (/portfolio/boogle)
#    Hair Salon (/portfolio/hair-salon)
#
# Create a separate handler (and URL route) for each of these pages.
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
