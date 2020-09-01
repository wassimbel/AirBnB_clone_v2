#!/usr/bin/python3
""" module - script that starts a Flask web application: """
from flask import Flask, escape, render_template


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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def if_variable(text="is cool"):
    """ display Python , followed by the value of the
        text variable (replace underscore _ symbols with a space ) """
    return 'Python %s' % escape(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_int(n):
    """ display n is a number only if n is an integer """
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def ren_temp(n):
    """ display a HTML page only if n is an integer: """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """display a HTML page only if n is an integer:
       tag: Number: n is even|odd inside the tag BODY """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
