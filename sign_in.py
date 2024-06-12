from flask import Blueprint, render_template

sign_in2 = Blueprint('sign_in', __name__)

@sign_in2.route('/login')
def login():
    return render_template("index.html")
    #return "<p>Login</p>"

@sign_in2.route('/logout')
def logout():
    return "<p>logout</p>"

@sign_in2.route('/sgin-up')
def sign_up():
    return "<p>Sign Up</p>"