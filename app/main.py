from flask import Flask
from routes.home_routes import home_routes
from routes.test_routes import test_routes

app = Flask(__name__)

# Registering the blueprints Routes
app.register_blueprint(home_routes)
app.register_blueprint(test_routes)

if __name__ == '__main__':
    app.run(debug=True)