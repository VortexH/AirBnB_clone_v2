#!/usr/bin/python3
"""
Contains the route for delivering a list of states using an HTML file
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def deliver_city_states_html():
    """ Gets the list of states located within the db or file storage

        Returns:
            an html file that contains a list of states contained
            the storage medium
    """

    state_instance_list = list(storage.all("State").values())
    sorted_state_instance_list = sorted(
        state_instance_list, key=lambda k: k.name)

    return render_template(
            '8-cities_by_states.html',
            sorted_state_instance_list=sorted_state_instance_list)


@app.teardown_appcontext
def close_session(func):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
