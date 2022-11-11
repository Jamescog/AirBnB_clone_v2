#!/usr/bin/python3
"""Starts a Flask web application
    - the web application will be listening on 0.0.0.0, pot 5000

    Routes:
            - /: display "Hello HBNB!"
            - /hbnb: display "HBNB"
            - /c/<text>: display "C" followed by the value of text
            - /python/(<text>): display "Python" followed by the value of text
            - /number/<n>: displays "n is a number" only if n is an interger
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route('/hnbn', strict_slashes=False)
def hbnb():
    """display 'HNBN' """
    return "HNBN"


@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
    """displays what c is"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is(text='is cool'):
    """displays what python is"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_int(n):
    """dispy if and only if it is int"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
