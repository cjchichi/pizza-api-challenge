# # from flask import request, jsonify
# # from server.app import db
# # from server.models.restaurant_pizza import RestaurantPizza
# # from server.models.pizza import Pizza
# # from server.models.restaurant import Restaurant

# # def register_restaurant_pizza_routes(app):
# #     @app.route('/restaurant_pizzas', methods=['POST'])
# #     def create_restaurant_pizza():
# #         data = request.get_json()

# #         try:
# #             price = data['price']
# #             pizza_id = data['pizza_id']
# #             restaurant_id = data['restaurant_id']

# #             if not (1 <= price <= 30):
# #                 return jsonify({"errors": ["Price must be between 1 and 30" ]}), 400
            
# #             pizza = Pizza.query.get(pizza_id)
# #             restaurant = Restaurant.query.get(restaurant_id)

# #             restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
# #             db.session.add(restaurant_pizza)
# #             db.session.commit()

# #             if not pizza or not restaurant:
# #                 return jsonify({"errors": ["Invalid pizza_id or restaurant_id"]}), 400

# #             # pizza = Pizza.query.get(pizza_id)
# #             # restaurant = Restaurant.query.get(restaurant_id)

# #             result = {
# #                 "id": restaurant_pizza.id,
# #                 "price": restaurant_pizza.price,
# #                 "pizza_id": restaurant_pizza.pizza_id,
# #                 "restaurant_id": restaurant_pizza.restaurant_id,
# #                 "pizza": {
# #                     "id":pizza.id,
# #                     "name": pizza.name,
# #                     "ingredients": pizza.ingredients
# #                 },
# #                 "restaurant": {
# #                     "id":restaurant.id,
# #                     "name": restaurant.name,
# #                     "address":restaurant.address
# #                 }
# #             }

# #             return jsonify(result), 201

# #         except (KeyError, TypeError):
# #             return jsonify({"errors": ["Invalid data"]}), 400

# #         except ValueError as e:
# #             return jsonify({"errors": [str(e)]}), 400

# #         except Exception:
# #             return jsonify({"errors": ["Invalid data"]}), 400

# from flask import request, jsonify
# from server.app import db
# from server.models.restaurant_pizza import RestaurantPizza
# from server.models.pizza import Pizza
# from server.models.restaurant import Restaurant

# def register_restaurant_pizza_routes(app):
#     @app.route('/restaurant_pizzas', methods=['POST'])
#     def create_restaurant_pizza():
#         data = request.get_json()

#         try:
#             price = data['price']
#             pizza_id = data['pizza_id']
#             restaurant_id = data['restaurant_id']

#             if not (1 <= price <= 30):
#                 return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

#             pizza = Pizza.query.get(pizza_id)
#             restaurant = Restaurant.query.get(restaurant_id)

#             if not pizza or not restaurant:
#                 return jsonify({"errors": ["Invalid pizza_id or restaurant_id"]}), 400

#             restaurant_pizza = RestaurantPizza(
#                 price=price,
#                 pizza_id=pizza_id,
#                 restaurant_id=restaurant_id
#             )
#             db.session.add(restaurant_pizza)
#             db.session.commit()

#             result = {
#                 "id": restaurant_pizza.id,
#                 "price": restaurant_pizza.price,
#                 "pizza_id": restaurant_pizza.pizza_id,
#                 "restaurant_id": restaurant_pizza.restaurant_id,
#                 "pizza": {
#                     "id": pizza.id,
#                     "name": pizza.name,
#                     "ingredients": pizza.ingredients
#                 },
#                 "restaurant": {
#                     "id": restaurant.id,
#                     "name": restaurant.name,
#                     "address": restaurant.address
#                 }
#             }

#             return jsonify(result), 201

#         except (KeyError, TypeError):
#             return jsonify({"errors": ["Invalid data"]}), 400

#         except ValueError as e:
#             return jsonify({"errors": [str(e)]}), 400

#         except Exception:
#             return jsonify({"errors": ["Invalid data"]}), 400


from server.app import app, db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from flask import request

def register_restaurant_pizza_routes(app):
    @app.route('/restaurant_pizzas', methods=['POST'])
    def create_restaurant_pizza():
        data = request.get_json()

        price = int(data.get('price'))
        pizza_id = int(data.get('pizza_id'))
        restaurant_id = int(data.get('restaurant_id'))

        if not (1 <= price <= 30):
            return { "errors": ["Price must be between 1 and 30"] }, 400

        pizza = db.session.query(Pizza).filter(Pizza.id == pizza_id).first()
        restaurant = db.session.query(Restaurant).filter(Restaurant.id == restaurant_id).first()

        if not pizza or not restaurant:
            return { "errors": ["Invalid pizza_id or restaurant_id"] }, 400

        rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(rp)
        db.session.commit()

        return {
            "id": rp.id,
            "price": rp.price,
            "pizza_id": rp.pizza_id,
            "restaurant_id": rp.restaurant_id,
            "pizza": {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            },
            "restaurant": {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
            }
        }, 201
