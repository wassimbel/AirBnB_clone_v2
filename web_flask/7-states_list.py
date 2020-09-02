#!/usr/bin/python3
""" module - starts a Flask web application: """
from models import storage
from flask import FLASK, render_template


app = FLASK(__name__)

@app.teardown_appcontext
def down():
    """ After each request you must remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states():
    """display a HTML page: (inside the tag BODY) """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
