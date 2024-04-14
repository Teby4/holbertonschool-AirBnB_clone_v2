#!/usr/bin/python3
"""task 1"""
from flask import Flask

app = Flask(import_name=__name__)

@app.route(rule='/', strict_slashes=False)
def hellohbnb():
    return "Hello HBNB!"

@app.route(rule='/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
