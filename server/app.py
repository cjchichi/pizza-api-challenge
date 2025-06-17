from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

from server.controllers.restaurant_controller import register_restaurant_routes
register_restaurant_routes(app)
from server.controllers.pizza_controller import register_pizza_routes
register_pizza_routes(app)
from server.controllers.restaurant_pizza_controller import register_restaurant_pizza_routes
register_restaurant_pizza_routes(app)