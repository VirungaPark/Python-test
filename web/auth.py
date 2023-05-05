import functools
from flask import g, redirect, request, url_for
import requests
from functools import wraps
import os

try:
    AUTH_URL = os.environ['AUTH_URL']
except:
    raise Exception("Please set the environment variable AUTH_URL to point to the authentication service.")

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view

def verify_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        access_token = request.cookies.get('access_token')
        if access_token:
            auth_res = requests.get(f"{AUTH_URL}/verify-token", json={'access_token': access_token})
            if auth_res.status_code == '200':
                username = auth_res['username']
                print(f"Access Token for user {username} is valid")
                return f(*args, **kwargs)
        return redirect(url_for('auth.login'))
    return decorated_function