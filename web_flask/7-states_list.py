#!/usr/bin/python3
"""
Contains the route for delivering a list of states using an HTML file
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def deliver_states_html():
    """ Gets the list of states located within the db or file storage

        Returns:
            an html file that contains a list of states contained
            the storage medium
    """

    state_instance_list = list(storage.all("State").values())
    sorted_state_instance_list = sorted(
        state_instance_list, key=lambda k: k.name)

    close_session()

    return render_template(
            '7-states_list.html',
            sorted_state_instance_list=sorted_state_instance_list)


@app.teardown_appcontext
def close_session():
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
