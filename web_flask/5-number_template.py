#!/usr/bin/python3
""" Routing definitions for handling different urls """


from flask import Flask, render_template

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


@app.route('/c/<text>', strict_slashes=False)
def display_text_after_c(text):
    """ Displays some text after the letter C

        Returns:
            a string with a letter C followed by some text
    """

    char_list = list(text)

    for i in range(len(char_list)):
        if char_list[i] == '_':
            char_list[i] = ' '

    text = ''.join(char_list)

    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display(text='is cool'):
    """ Displays some text after the word Python

        Returns:
            Python <text after the last forward slash>

    """

    char_list = list(text)

    for i in range(len(char_list)):
        if char_list[i] == '_':
            char_list[i] = ' '

    text = ''.join(char_list)

    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """ Displays a string with "<n> is a number"


        Returns:
            "<n> is a number"

    """

    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_html_template(n):
    """ Displays an html template

        Returns:
            html template

    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
