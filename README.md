# Flask Code Challenge - Pizza Restaurants
This is a simple flask API application housing routes to various restaurants, pizzas and restaurant_pizzas.

# Installation
```
# clone the repo
$ git clone <repo>
```

```
# navigate to directory
$ cd <directory>
```

```
# create virtual environment and install dependancies
$ pip install pipenv
$ pipenv shell

```
# Usage
To use this  project:
```
# Navigate to restaurant directory
$ cd restaurant

# Run the flask application
$ flask run
```

```
# Navigate to various url routes on your browser
$ http://127.0.0.1:5000/restaurants/pizzas/restaurant_pizzas/
```
## Features
The different routes consist of different contents and functionality:
1. Restaurant route consists of a list of available restaurants with a GET method to retrieve the restaurants and even a specific restaurant through its id. You can also delete a specific restaurant.
2. Pizzas route consists of a list of available pizzas and GET method to retrieve the list of pizzas available.
3. Restaurant_Pizzas route carries out POST methods on the route where you can send data to the server.

# Technologies Used
```
flask - For the backend logic of the system
python - Programming language used for the designing of the application

```
# LICENSE

LICENSE [MIT](LICENSE)