#!/usr/bin/python3
"""task 2"""
from flask import Flask

app = Flask(import_name=__name__)


@app.route(rule='/', strict_slashes=False)
def hellohbnb():
    return "Hello HBNB!"


@app.route(rule='/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route(rule='/c/<text>', strict_slashes=False)
def ctext(text):
    text = text.replace('_', ' ')
    return "C {}".format(text)

@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def pytext(text):
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
