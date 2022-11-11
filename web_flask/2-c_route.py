#!/usr/bin/python3
"""Starts a Flask web application
    - the web application will be listening on 0.0.0.0, port 80

    Routes:
            - /: displays "Hello HBNB!"
            - /hbnb: displays "HNBN"
            - /c/<text>: displays "C" followed by the value of the text
"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hnbn():
    """displays 'HBNB' """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is(text):
    """displays what c is!"""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
