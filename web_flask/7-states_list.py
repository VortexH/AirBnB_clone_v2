#!/usr/bin/python3
"""
Contains the route for delivering a list of states using an HTML file
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def deliver_states_html():
    """ Gets the list of states located within the db or file storage

        Returns:
            an html file that contains a list of states contained
            the storage medium
    """

    states_dict = storage.all(State)




if __name__ == "__main__":
    app.run(host='0.0.0.0')
