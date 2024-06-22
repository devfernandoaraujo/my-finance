from flask import Flask
from app.routes.home_routes import home_routes
from app.routes.test_routes import test_routes
#from extensions import db, migrate
#from config import Config

def create_app():
    app = Flask(__name__)
    
    # Register the blueprints
    app.register_blueprint(home_routes)
    app.register_blueprint(test_routes)

    return app