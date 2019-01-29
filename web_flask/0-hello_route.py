#!/usr/bin/python3
""" Imports an instance of flask from __init__.py and creates a route """


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ function to handle the default / route

        Returns:
                a generic string
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
