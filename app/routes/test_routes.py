from flask import Blueprint, render_template

test_routes = Blueprint("test_routes", __name__)

@test_routes.route('/test')
def test():
    return "Test route is working!"