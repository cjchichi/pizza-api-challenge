from flask import jsonify
from server.models.restaurant import Restaurant

def register_restaurant_routes(app):
    @app.route('/restaurants/<int:id>', methods=['GET'])
    def get_restaurants(id):
        restaurants = Restaurant.query.get(id)
        if not restaurant:
            return jsonify({"error":"Restaurant not found"}), 404

        pizzas = [
            {
                "id":restaurant_pizza.pizza.id,
                "name":restaurant_pizza.pizza.name,
                "ingredients": restaurant_pizza.pizza.ingredients
            }
            for rp in restaurant.restaurant_pizzas
        ]
        data = {
            "id":restaurant.id,
            "name":restaurant.name,
            "address":restaurant.address,
            "pizzas":pizzas
        }

        return jsonify(data), 200

    @app.route('/restaurants/<int:id>', methods=['DELETE'])
    def delete_restaurant(id):
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            return jsonify({"error": "Restaurant not found"}), 404

        db.session.delete(restaurant)
        db.session.commit()

        return '', 204