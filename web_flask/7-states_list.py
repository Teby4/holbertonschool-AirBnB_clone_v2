#!/usr/bin/python3
"""task 2"""
from typing import Literal
from flask import Flask, render_template

app = Flask(import_name=__name__)


@app.route(rule='/', strict_slashes=False)
def hellohbnb() -> Literal['Hello HBNB!']:
    return "Hello HBNB!"


@app.route(rule='/hbnb', strict_slashes=False)
def hbnb() -> Literal['HBNB']:
    return "HBNB"


@app.route(rule='/c/<text>', strict_slashes=False)
def ctext(text) -> str:
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def pytext(text) -> str:
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route(rule='/number/<int:n>', strict_slashes=False)
def number(n) -> str:
    return "{} is a number".format(n)


@app.route(rule='/number_template/<int:n>', strict_slashes=False)
def ntemplate(n) -> str:
    return render_template('5-number.html', n=n)


@app.route(rule='/number_odd_or_even/<int:n>', strict_slashes=False)
def odoreven(n) -> str:
    if n % 2 == 0:
        oddoreven = "even"
    else:
        oddoreven = "odd"
    return render_template('6-number_odd_or_even.html', n=n,
                           oddoreven=oddoreven)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
