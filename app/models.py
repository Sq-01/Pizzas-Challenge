from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Restaurant(db.Model , SerializerMixin):
    __tablename__ = 'restaurants'

    serialize_rules = ('-restaurant_pizzas.restaurant',)

    id = db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String)
    address =db.Column(db.String)

    restaurant_pizzas = db.relationship('RestaurantPizza' , backref='restaurant')

    def __repr__(self):
        return f'restaurant name is {self.name} and address is {self.address}'

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    serialize_rules = ('-restaurant_pizzas.pizza',)

    id = db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String)
    ingredients =db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurant_pizzas = db.relationship('RestaurantPizza' , backref='pizza')

    def __repr__(self):
        return f'pizza name is {self.name} and ingredients are {self.ingredients}'

class RestaurantPizza(db.Model , SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    serialize_rules = ('-pizza.restaurant_pizzas','-restaurant.restaurant_pizzas',)

    id = db.Column(db.Integer, primary_key=True)
    pizza_id =db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id =db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('price')
    def validate_price(self, key, price):
        if 30 < price < 1:
            raise ValueError("Must be a value between 1 and 30")
        return price

    def __repr__(self):
        return f'restaurantpizza price is {self.price}'

