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
