from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route('/login')
def login():
    return "LogIn"

@auth.route('/sign-up')
def sign_up():
    return "SignUp"

@auth.route('/logout')
def logout():
    return "LogOut"