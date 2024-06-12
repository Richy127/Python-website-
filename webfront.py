from flask import Blueprint, render_template

webfront = Blueprint('webfront',__name__, template_folder="C:\\Users\\conno\\.vscode\\templates\\", static_folder="C:\\Users\\conno\\.vscode\\static\\")

@webfront.route('/')

def index():
    #return"<h1>Welcome to FitFinder.CA</h1>"
    return render_template("index.html")

@webfront.route('/healthy')

def hello ():
    return render_template("healthy.html")

