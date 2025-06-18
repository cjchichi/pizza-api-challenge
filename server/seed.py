# from server.app import app, db
# from server.models.restaurant import Restaurant
# from server.models.pizza import Pizza
# from server.models.restaurant_pizza import RestaurantPizza

# with app.app_context():
#     db.session.query(RestaurantPizza).delete()
#     db.session.query(Pizza).delete()
#     db.session.query(Restaurant).delete()

#     r1 = Restaurant(name="Dominos Pizza", address="123 Main St")
#     r2 = Restaurant(name="Pizza-inn", address="456 Elm St")

#     p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese")
#     p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

#     # rp1 = RestaurantPizza(price=10, restaurant=r1, pizza=p1)
#     # rp2 = RestaurantPizza(price=12, restaurant=r2, pizza=p2)
#     # rp3 = RestaurantPizza(price=8, restaurant=r2, pizza=p1)

#     rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
#     rp2 = RestaurantPizza(price=12, restaurant_id=r2.id, pizza_id=p2.id)
#     rp3 = RestaurantPizza(price=8, restaurant_id=r2.id, pizza_id=p1.id)

#     db.session.add_all([r1, r2, p1, p2, rp1, rp2, rp3])
#     db.session.commit()


import sys
import os

# Add parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server.app import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    # Clear existing data
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    # Create restaurants
    r1 = Restaurant(name="Dominos Pizza", address="123 Main St")
    r2 = Restaurant(name="Pizza-Inn", address="456 Elm St")

    # Create pizzas
    p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    # Create associations
    rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=12, restaurant_id=r2.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=8, restaurant_id=r2.id, pizza_id=p1.id)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()
