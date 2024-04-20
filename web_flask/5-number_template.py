#!/usr/bin/python3
"""
This script starts a Flask web application.

The web application listens on 0.0.0.0, port 5000, and includes six routes:
- `/`: Displays "Hello HBNB!"
- `/hbnb`: Displays "HBNB"
- `/c/<text>`: Displays "C " followed by the value of the text variable,
  replacing underscore _ symbols with a space.
- `/python/<text>`: Displays "Python " followed by the value of the text variable,
  replacing underscore _ symbols with a space. The default value of text is "is cool".
- `/number/<n>`: Displays "n is a number" only if n is an integer.
- `/number_template/<n>`: Displays a HTML page only if n is an integer.
  The HTML page contains an H1 tag with the text "Number: n".

The option strict_slashes=False is used in the route definitions.
"""

from flask import Flask, render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """Display "Python " followed by the value of the text variable."""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """Display "n is a number" only if n is an integer."""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numberandtemplate(n):
    """Display HTML page with an H1 tag containing the text "Number: n"."""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
