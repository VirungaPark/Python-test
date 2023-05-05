from flask import Flask, request, make_response, redirect, render_template
from flask_jwt_extended import JWTManager
import os
import requests
from auth import verify_token

try:
    AUTH_URL = os.environ['AUTH_URL']
except:
    raise Exception("Please set the environment variable AUTH_URL to point to the authentication service.")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///web.db'
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'dev')
jwt = JWTManager(app)

@app.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        auth_res = requests.post(f"{AUTH_URL}/login", json={'username': username, 'password': password}).json()   
        res = make_response(redirect("/"))
        res.set_cookie("access_token", value=auth_res["access_token"], samesite="Lax") #, samesite='strict')
        return res
    else:
        return render_template("auth/login.html")

@app.route("/logout")
def logout():
    pass

@app.route("/admin")
#@verify_token
def admin():
    pass

@app.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        role = request.form["role"]