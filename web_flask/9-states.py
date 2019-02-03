#!/usr/bin/python3
"""
Contains the route for delivering a list of states using an HTML file
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def deliver_all_states_or_a_single_state(id=None):
    """ Delivers only states that exist in the database or
        a specific state with certain cities

        Returns:
            an html file that either contains only states
            or a specific state and its cities
    """
    state_instance_list = list(storage.all("State").values())
    sorted_state_instance_list = sorted(
        state_instance_list, key=lambda k: k.name)

    return render_template(
        '9-states.html',
        sorted_state_instance_list=sorted_state_instance_list, id=id
    )


@app.teardown_appcontext
def close_session(func):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
