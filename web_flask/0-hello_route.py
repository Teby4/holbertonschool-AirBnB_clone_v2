#!/usr/bin/python3
"""task 0"""
from flask import Flask

app = Flask(import_name=__name__)


@app.route(rule='/', strict_slashes=False)
def hellohbnb():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
