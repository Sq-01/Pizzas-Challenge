from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():

    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()
    
    restaurants = []
    restaurants.append(Restaurant(name='Hilton Hotel' , address= 'Nairobi CBD'));
    restaurants.append(Restaurant(name='Villa Rosa Kempinski', address= 'Westlands'));
    db.session.add_all(restaurants)

    pizzas = []
    pizzas.append(Pizza(name='Hawaiian pizza', ingredients=" ham, cheese, pineapple"));
    pizzas.append(Pizza(name='Vegeterian pizza', ingredients=" mushrooms, cherry tomatoes, artichoke, bell pepper, olives"));
    pizzas.append(Pizza(name='Buffalo pizza', ingredients="  blue cheese,buffalo chicken, banana peppers, red onions"));
    pizzas.append(Pizza(name='BBQ Chicken Pizza', ingredients=" bbq sauce, mozzarella, chicken, red onions,cilantro"));

    db.session.add_all(pizzas)

    restaurant_pizza =[]
    restaurant_pizza.append(RestaurantPizza(price = 15, restaurant =restaurants[0], pizza=pizzas[3]))
    restaurant_pizza.append(RestaurantPizza(price = 30, restaurant =restaurants[1], pizza=pizzas[2]))
    restaurant_pizza.append(RestaurantPizza(price = 13, restaurant =restaurants[1], pizza=pizzas[0]))
    restaurant_pizza.append(RestaurantPizza(price = 27, restaurant =restaurants[0], pizza=pizzas[2]))
    restaurant_pizza.append(RestaurantPizza(price = 24, restaurant =restaurants[1], pizza=pizzas[1]))
    restaurant_pizza.append(RestaurantPizza(price = 17, restaurant =restaurants[0], pizza=pizzas[3]))
    restaurant_pizza.append(RestaurantPizza(price = 26, restaurant =restaurants[1], pizza=pizzas[2]))
    restaurant_pizza.append(RestaurantPizza(price = 7, restaurant =restaurants[1], pizza=pizzas[0]))
    restaurant_pizza.append(RestaurantPizza(price = 14, restaurant =restaurants[0], pizza=pizzas[2]))
    restaurant_pizza.append(RestaurantPizza(price = 24, restaurant =restaurants[1], pizza=pizzas[1]))

    db.session.add_all(restaurant_pizza)
    db.session.commit()