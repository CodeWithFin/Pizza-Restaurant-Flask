from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Pizza, Restaurant, Restaurant_Pizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return 'Index for Pizza/Restaurant API'

# Route for getting the restaurants
@app.route('/restaurants', methods = ['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_data = []
    # Loops throught the restaurants available and appends their data
    for restaurant in restaurants:
        restaurant_data.append({
            'id':restaurant.id,
            'name':restaurant.name,
            'address':restaurant.address
        })

    response_data = {
        'restaurants':restaurant_data
    }
    
    return jsonify(response_data), 200

# Route access a specific restaurant through its id
@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant_by_id(id):
    restaurant = Restaurant.query.get(id)
    if restaurant is None:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    restaurant_data = {
        'id':restaurant.id,
        'name':restaurant.name,
        'address':restaurant.address,
        'pizzas':[]
    }

    # Loops through the pizzas present on a restaurant based on an associated id
    pizzas = Pizza.query.join(Restaurant_Pizza).filter(Restaurant_Pizza.id == id).all()
    for pizza in pizzas:
        restaurant_data['pizzas'].append({
            'id':pizza.id,
            'name':pizza.name,
            'ingredients':pizza.ingredients
        })

    return jsonify(restaurant_data), 201

# This is a route for deleting a specific restaurant through its id
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant is None:
        return jsonify({'error': 'Restaurant not found'}), 404 
    try:
        Restaurant_Pizza.query.filter_by(id=id).delete()
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error'}), 500

# Displays a set of pizzas available through GET request
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizza_data = []
    for pizza in pizzas:
        pizza_data.append({
            'id':pizza.id,
            'name':pizza.name,
            'ingredients':pizza.ingredients
        })

    response_data = {
        'pizzas': pizza_data
    }

    return jsonify(response_data), 200

# Carries out POST method on restaurant_pizzas 
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if price is None or pizza_id is None or restaurant_id is None:
        return jsonify({'errors': ['Missing required fields']}), 400
    
    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    if pizza is None or restaurant is None:
        return jsonify({'errors': ['Invalid pizza or restaurant id']}), 400
    
    restaurant_pizza = Restaurant_Pizza(
        pizza_id = pizza_id,
        restaurant_id = restaurant_id,
        price = price
    )

    db.session.add(restaurant_pizza)

    try: 
        db.session.commit()
        return jsonify({
            'id':pizza.id,
            'name':pizza.name,
            'ingredients':pizza.ingredients
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'errors': ['An error occured Bonzo!']}), 500



if __name__ == '__main__':
    app.run(port=5555)