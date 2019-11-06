###
#
# Les 18 - Database
#
###

from flask import Flask, render_template, request, redirect, url_for
from models import User, db

app = Flask(__name__)
db.create_all() # create (new) tables in the database


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("user-name")
    email = request.form.get("user-email")

    # create a User object
    user = User(name=name, email=email)

    # save the user object into a database
    db.add(user)
    db.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
