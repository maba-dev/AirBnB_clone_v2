#!/usr/bin/python3
"""Start Flask web App"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Display Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """Display HBNB """
    return 'HBNB'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
