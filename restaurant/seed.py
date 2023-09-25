# seed.py
from random import randint, choice as rc
from faker import Faker
from app import app
from models import db, Pizza, Restaurant, Restaurant_Pizza

pizza_types = [
    "Margherita Pizza",
    "Pepperoni Pizza",
    "Hawaiian Pizza",
    "Meat Lovers' Pizza",
    "Veggie Pizza",
    "BBQ Chicken Pizza",
    "Buffalo Chicken Pizza",
    "White Pizza",
    "Four Cheese Pizza (Quattro Formaggi)",
    "Supreme Pizza",
    "Neapolitan Pizza",
    "Sicilian Pizza",
    "Chicago Deep-Dish Pizza",
    "California Pizza",
    "Mediterranean Pizza",
    "Pesto Pizza",
    "Breakfast Pizza",
    "Seafood Pizza",
    "Taco Pizza",
    "Dessert Pizza"
]

kenyan_restaurants = [
    "Nyama Choma Joint",
    "Swahili Restaurant",
    "Indian Curry House",
    "Chinese Cuisine",
    "Italian Pizzeria",
    "Japanese Sushi Bar",
    "Ethiopian Restaurant",
    "Burger Joint",
    "Seafood Restaurant",
    "Vegetarian Cafe",
    "Fast Food Outlet",
    "Fine Dining Restaurant",
    "Barbecue Grill",
    "Cafeteria",
    "Nairobi Street Food Stall",
    "Fusion Cuisine Restaurant",
    "Mediterranean Eatery",
    "African Buffet",
    "Coffee Shop",
    "Dessert Parlor",
    "Food Truck",
    "Vegetable and Fruit Market Stall",
    "Food Court",
    "Local Kenyan Diner",
    "International Cuisine Restaurant",
    "Health Food Cafe",
    "Bakery and Pastry Shop",
    "Tea House",
    "Brewpub",
    "Wine Bar",
    "Food Delivery Service",
    "Hotel Restaurant",
    "Rooftop Dining",
    "Sports Bar and Grill",
    "Vegetarian and Vegan Restaurant"
]

kenyan_restaurants = [
    "Nyama Choma Joint",
    "Swahili Restaurant",
    "Indian Curry House",
    "Chinese Cuisine",
    "Italian Pizzeria",
    "Japanese Sushi Bar",
    "Ethiopian Restaurant",
    "Burger Joint",
    "Seafood Restaurant",
    "Vegetarian Cafe",
    "Fast Food Outlet",
    "Fine Dining Restaurant",
    "Barbecue Grill",
    "Cafeteria",
    "Nairobi Street Food Stall",
    "Fusion Cuisine Restaurant",
    "Mediterranean Eatery",
    "African Buffet",
    "Coffee Shop",
    "Dessert Parlor",
    "Food Truck",
    "Vegetable and Fruit Market Stall",
    "Food Court",
    "Local Kenyan Diner",
    "International Cuisine Restaurant",
    "Health Food Cafe",
    "Bakery and Pastry Shop",
    "Tea House",
    "Brewpub",
    "Wine Bar",
    "Food Delivery Service",
    "Hotel Restaurant",
    "Rooftop Dining",
    "Sports Bar and Grill",
    "Vegetarian and Vegan Restaurant"
]

addresses = [
    "123 Mombasa Road, Nairobi",
    "Westgate Mall, Mwanzi Road, Nrb 100",
    "789 Thika Highway, Thika",
    "101 Nairobi-Mombasa Highway, Machakos",
    "Good Italian, Ngong Road, 5th Avenuet",
    "567 Kilimani Rd, Nairobi",
    "599 Rd Double-Tree, Kilimani",
    "111 Nakuru-Nairobi Bypass, Nairobi",
    "222 Malindi Beach Road, Malindi",
    "Ngong Rd 506 Mnarani",
    "444 State House, Nairobi",
    "555 Kitale Street, Kitale",
    "666 Jeevanjee Gardens, Jevanjee",
    "QuickMart Lane, Afya Center, Nairobi",
    "5656 Nairobi West, Nairobi",
    "Ngong Lane, Ngong"
]

food_ingredients = [
    "flour", "water", "yeast", "salt", "tomato sauce",
    "cheese", "pepperoni", "lettuce", "tomato", "cucumber",
    "olive oil", "pasta", "garlic", "formaggi", "white vinegar",
    "dumplings", "honey", "eggs", "mayonnaise", "butter", " caramalised onions"
]

# Generates a list of fake ingredients
def generate_ingredients():
    return [rc(food_ingredients) for i in range(3)]

fake = Faker()

with app.app_context():
    db.create_all() 


    Pizza.query.delete()
    Restaurant.query.delete()
    Restaurant_Pizza.query.delete()

    pizza_list = []
    restaurant_list = []

    # Generates 70 pizzas
    for i in range(20):
        pizza = Pizza(
            name=rc(pizza_types),
            ingredients=generate_ingredients() 
        )
        pizza_list.append(pizza)

    db.session.add_all(pizza_list)
    db.session.commit() 

    # Generates 36 restaurants
    for i in range(36):
        restaurant = Restaurant(
            name=rc(kenyan_restaurants),
            address=rc(addresses)
        )
        restaurant_list.append(restaurant)

    db.session.add_all(restaurant_list)
    db.session.commit()  
    
    # Links pizzas and restaurants to the restaurant_pizza table
    for pizza in pizza_list:
        for restaurant in restaurant_list:
            price = randint(10, 50)  
            restaurant_pizza = Restaurant_Pizza(
                pizza=pizza,
                restaurant=restaurant,
                price=price
            )
            db.session.add(restaurant_pizza)

    db.session.commit()  
