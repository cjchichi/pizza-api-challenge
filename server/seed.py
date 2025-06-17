from server.app import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    db.session.query(RestaurantPizza).delete()
    db.session.query(Pizza).delete()
    db.session.query(Restaurant).delete()

    r1 = Restaurant(name="Dominos Pizza", address="123 Main St")
    r2 = Restaurant(name="Pizza-inn", address="456 Elm St")

    p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    rp1 = RestaurantPizza(price=10, restaurant=r1, pizza=p1)
    rp2 = RestaurantPizza(price=12, restaurant=r2, pizza=p2)
    rp3 = RestaurantPizza(price=8, restaurant=r2, pizza=p1)

    db.session.add_all([r1, r2, p1, p2, rp1, rp2, rp3])
    db.session.commit()