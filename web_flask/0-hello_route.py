#!/usr/bin/python3
"""
This script starts a Flask web application.

The web application listens on 0.0.0.0, port 5000, and includes a route
that displays "Hello HBNB!".

Routes:
    /: display "Hello HBNB!"
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display "Hello HBNB!" when accessing the root URL."""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
