#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """hello_route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """hbnb"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """c_route"""
    return "C {}".format(text.Replace("_", " "))



if __name__ == "__main__":
    app.run()
