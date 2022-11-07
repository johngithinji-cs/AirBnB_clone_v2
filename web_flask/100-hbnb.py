#!/usr/bin/python3
""" Script to start a Flask web application. """

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """ Displays a HTML page. """
    states = storage.all('State').values()
    cities = storage.all('City').values()
    amenities = storage.all('Amenity').values()
    places = storage.all('Place').values()
    return render_template('100-hbnb_filters.html', **locals())


@app.teardown_appcontext
def closer(self):
    """ Removes the current SQLAlchemy Session. """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
