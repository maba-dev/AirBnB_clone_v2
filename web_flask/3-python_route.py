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


@app.route('/c/<text>', strict_slashes=False)
def variable(text):
    """Display a variable"""
    return 'C %s' % text


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def variable_python(text='is cool'):
    """Display a variable"""
    return 'Python %s' % text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
