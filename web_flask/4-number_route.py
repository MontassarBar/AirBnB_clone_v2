#!/usr/bin/python3
'''script that starts a Flask web application'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    '''display “Hello HBNB!”'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''display “HBNB”'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    ''' display “C ” followed by the value of the text variable
    and replace underscore "_" symbols with a space'''
    text2 = text.replace("_", " ")
    return 'C %s' % text2


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    '''display “Python ”, followed by the value of the text variable
    and replace underscore "_" symbols with a space'''
    text3 = text.replace("_", " ")
    return 'python %s' % text3


@app.route('/number/<int:n>', strict_slashes=False)
def n_isnum(n):
    '''display “n is a number” only if n is an integer'''
    return '%d is a number' % n


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
