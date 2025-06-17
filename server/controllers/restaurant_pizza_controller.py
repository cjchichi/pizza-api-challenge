from flask import request, jsonify
from server.app import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant

def register_restaurant_pizza_routes(app):
    @app.route('/restaurant_pizzas', methods=['POST'])
    def create_restaurant_pizza():
        data = request.get_json()

        try:
            price = data['price']
            pizza_id = data['pizza_id']
            restaurant_id = data['restaurant_id']

            restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
            db.session.add(restaurant_pizza)
            db.session.commit()

            pizza = Pizza.query.get(pizza_id)
            restaurant = Restaurant.query.get(restaurant_id)

            result = {
                "id": restaurant_pizza.id,
                "price": restaurant_pizza.price,
                "pizza_id": restaurant_pizza.price_id,
                "restaurant_id": restaurant_pizza.restaurant_id,
                "pizza": {
                    "id":pizza.id,
                    "name": pizza.name,
                    "ingredients": pizza.ingredients
                },
                "restaurant": {
                    "id":restaurant.id,
                    "name": restaurant.name,
                    "address":restaurant.address
                }
            }

            return jsonify(result), 201

        except ValueError as e:
            return jsonify({"errors": [str(e)]}), 400

        except Exception:
            return jsonify({"errors": ["Invalid data"]}), 400