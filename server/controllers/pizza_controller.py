from flask import jsonify
from server.models.pizza import Pizza

def register_pizza_routes(app):
    @app.route('/pizzas', methods=['GET'])
    def get_pizzas():
        pizzas = Pizza.query.all()

        pizza_list = []
        for pizza in pizzas:
            pizza_list.append({
                'id': pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients
            })

        return jsonify(pizza_list), 200