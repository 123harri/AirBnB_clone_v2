#!/usr/bin/python3
"""
This script starts a Flask web application.

The web application listens on 0.0.0.0, port 5000, and includes three routes:
- `/`: Displays "Hello HBNB!"
- `/hbnb`: Displays "HBNB"
- `/c/<text>`: Displays "C " followed by the value of the text variable,
  replacing underscore _ symbols with a space.

The option strict_slashes=False is used in the route definitions.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display "Hello HBNB!" when accessing the root URL."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Display "HBNB" when accessing the /hbnb URL."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Display "C " followed by the value of the text variable."""
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
