# Python standard libraries
import json
import os
import sqlite3
import requests
import logging

# Third-party libraries
from flask import Flask, redirect, request, url_for, render_template
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user
)
from oauthlib.oauth2 import WebApplicationClient
from google.oauth2 import id_token
from google.auth.transport import requests

# Internal imports
from db import init_db_command
from user import User

# Configuration
with open("secret.txt", "r") as f:
    secret_lines = f.readlines()
secret_list = [l.rstrip('\n') for l in secret_lines]
GOOGLE_CLIENT_ID = secret_list[0] or None
GOOGLE_CLIENT_SECRET = secret_list[1] or None
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

# Flask app setup
app = Flask(__name__)
app.secret_key = os.urandom(24)

# User session management setup
# https://flask-login.readthedocs.io/en/latest
login_manager = LoginManager()
login_manager.init_app(app)

# Naive database setup
try:
    init_db_command()
except sqlite3.OperationalError:
    # Assume it's already been created
    pass

# OAuth 2 client setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)

# Flask-Login helper to retrieve a user from our db


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


@app.route("/login/callback", methods=["POST", "GET"])
def callback():
    json_data = request.json
    try:
        token = json_data["id_token"]
        idinfo = id_token.verify_oauth2_token(token,
                                              requests.Request(),
                                              GOOGLE_CLIENT_ID)
        print(idinfo)
    except ValueError as e:
        print(e)

    # idinfo = id_token.verify_oauth2_token(token,
    #                                       requests.Request(),
    #                                       CLIENT_ID)
    return render_template("callback.html")


@ app.route("/logout")
@ login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
