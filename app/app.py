#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)
api =Api(app)

@app.route('/')
def home():
    return ''

@app.route('/restaurants')
def get_restaurants(): #gets all restaurants
    restaurants =[]

    for restaurant in Restaurant.query.all():
        restaurant ={
            "name": restaurant.name,
            "address": restaurant.address
        }
        restaurants.append(restaurant)
        response = make_response(jsonify(restaurants),200)
    return response

@app.route('/restaurants/<int:id>', methods =['GET', 'DELETE'])
def get_restaurant_byID(id):

    if request.method =='GET':
        rest = Restaurant.query.filter_by(id=id).first()

        if rest == None:
            response = make_response(
                jsonify({
                    "error": "Restaurant not found"
                    }),
                404
            )
            return response
        else:

            rest_dict =rest.to_dict()

            response = make_response(
                jsonify(rest_dict),
                200
            )
            response.headers["Content-Type"] = "application/json"

            return response
        
    elif request.method =='DELETE':
        rest = Restaurant.query.filter_by(id=id).first()

        if rest == None:
            response = make_response(
                jsonify({
                    "error": "Restaurant not found"
                    }),
                404
            )
            return response
        else:
            db.session.delete(rest)
            db.session.commit()

            response = make_response(
                jsonify({
                    "": ""
                }),
                200
            )
            return response

 # use Flask-restful for pizza and restaurantpizza routes     
class Pizzas(Resource):
    def get(self): # all pizzas
        pizza = [pizz.to_dict() for pizz in Pizza.query.all()]

        response = make_response(jsonify(pizza),200)
        return response

api.add_resource(Pizzas, '/pizzas')

if __name__ == '__main__':
    app.run(port=5555)
