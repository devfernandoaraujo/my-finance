from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route('/')
def home():
    print("Home route hit")
    return render_template('home/index.html')