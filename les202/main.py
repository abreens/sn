###
#
# Homework 20.2 - GitHub login
#
###

import json

from flask import Flask, render_template, request, redirect, url_for, make_response
from requests_oauthlib import OAuth2Session
import os


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/github/login")
def github_login():
    # prepare the GitHub OAuth session
    github = OAuth2Session(os.environ.get("GITHUB_CLIENT_ID"))
    # GitHub authorization URL
    authorization_url, state = github.authorization_url("https://github.com/login/oauth/authorize")
    # redirect user to GitHub for authorization
    response = make_response(redirect(authorization_url))
    # for CSRF purposes
    response.set_cookie("oauth_state", state, httponly=True)
    return response


@app.route("/github/callback")
def github_callback():
    github = OAuth2Session(os.environ.get("GITHUB_CLIENT_ID"), state=request.cookies.get("oauth_state"))
    token = github.fetch_token("https://github.com/login/oauth/access_token",
                               client_secret=os.environ.get("GITHUB_CLIENT_SECRET"),
                               authorization_response=request.url)
    response = make_response(redirect(url_for('profile')))  # redirect to the profile page
    response.set_cookie("oauth_token", json.dumps(token), httponly=True)
    return response


@app.route("/profile")
def profile():
    if request.cookies.get("oauth_token"):
        github = OAuth2Session(os.environ.get("GITHUB_CLIENT_ID"), token=json.loads(request.cookies.get("oauth_token")))
        github_profile_data = github.get('https://api.github.com/user').json()
        return render_template("profile.html", github_profile_data=github_profile_data)
    else:
        return render_template("index.html")


@app.route("/github/logout")
def logout():
    response = make_response(redirect(url_for('index')))  # redirect to the index page
    response.set_cookie("oauth_token", expires=0)  # delete the oauth_cookie to logout
    return response


if __name__ == '__main__':
    app.run()