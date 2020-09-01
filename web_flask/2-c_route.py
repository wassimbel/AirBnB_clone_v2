#!/usr/bin/python3
""" module - script that starts a Flask web application: """
from flask import Flask, escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """ return msg for specific route """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ return msg for specific route """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def variable(text):
    """  display C  followed by the value of the text
         variable (replace underscore _ symbols with a space ) """
    return 'C %s' % escape(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
