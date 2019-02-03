#!/usr/bin/python3
""" Methods to handle /hbnb_filters route """


from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def deliver_6_index_html():
    """ Renders 10-hbnb_filters.html in the browser """
    state_instance_list = list(storage.all("State").values())
    sorted_state_instance_list = sorted(
        state_instance_list, key=lambda k: k.name)

    amenity_list = list(storage.all("Amenity").values())
    sorted_amenity_list = sorted(amenity_list, key=lambda k: k.name)

    return render_template(
        '10-hbnb_filters.html',
        sorted_state_instance_list=sorted_state_instance_list,
        sorted_amenity_list=sorted_amenity_list
    )


@app.teardown_appcontext
def close_session(func):
    """ Closes a session """
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0")
