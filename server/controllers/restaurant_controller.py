
from flask import jsonify
from server.app import db
from server.models.restaurant import Restaurant

def register_restaurant_routes(app):
    @app.route('/restaurants', methods=['GET'])
    def get_all_restaurants():
        restaurants = db.session.query(Restaurant).all()
        result = [
            {
                "id": r.id,
                "name": r.name,
                "address": r.address
            }
            for r in restaurants
        ]
        return jsonify(result), 200

    @app.route('/restaurants/<int:id>', methods=['GET'])
    def get_restaurant_by_id(id):
        restaurant = db.session.query(Restaurant).get(id)
        if not restaurant:
            return jsonify({"error": "Restaurant not found"}), 404

        pizzas = [
            {
                "id": rp.pizza.id,
                "name": rp.pizza.name,
                "ingredients": rp.pizza.ingredients
            }
            for rp in restaurant.restaurant_pizzas
        ]
        data = {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address,
            "pizzas": pizzas
        }
        return jsonify(data), 200

    @app.route('/restaurants/<int:id>', methods=['DELETE'])
    def delete_restaurant(id):
        restaurant = db.session.query(Restaurant).get(id)
        if not restaurant:
            return jsonify({"error": "Restaurant not found"}), 404

        db.session.delete(restaurant)
        db.session.commit()
        return '', 204

