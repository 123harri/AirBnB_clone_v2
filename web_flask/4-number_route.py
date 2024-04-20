#!/usr/bin/python3
"""
This script starts a Flask web application.

The web application listens on 0.0.0.0, port 5000, and includes five routes:
- `/`: Displays "Hello HBNB!"
- `/hbnb`: Displays "HBNB"
- `/c/<text>`: Displays "C " followed by the value of the text variable,
  replacing underscore _ symbols with a space.
- `/python/<text>`: Displays "Python " followed by the value of the text variable,
  replacing underscore _ symbols with a space. The default value of text is "is cool".
- `/number/<n>`: Displays "n is a number" only if n is an integer.

The option strict_slashes=False is used in the route definitions.
"""

from flask import Flask, escape

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
def display_c_text(text):
    """Display "C " followed by the value of the text variable."""
    return 'C {}'.format(escape(text).replace('_', ' '))


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text):
    """Display "Python " followed by the value of the text variable."""
    return 'Python {}'.format(escape(text).replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Display "n is a number" only if n is an integer."""
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
