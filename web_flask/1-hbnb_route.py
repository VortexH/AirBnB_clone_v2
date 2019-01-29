#!/usr/bin/python3
""" Routing definitions for handling different urls """


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def say_hello():
    """ Returns a string

        Returns:
            "Hello, HBNB!"

    """

    return "Hello, HBNB!"


@app.route('/hbnb', strict_slashes=False)
def print_hbnb():
    """ Returns HBNB

        Returns:
            "HBNB"

    """

    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
