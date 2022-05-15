#!/usr/bin/python3
"""Start Flask web App"""
from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """ display “n is a number” only if n is an integer"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_HTML(n):
    """display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_even_odd(n):
    """ Number: n is even|odd” inside the tag BODY"""
    if n % 2 == 0:
        var = 'even'
    else:
        var = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, var=var)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
