#!/usr/bin/python3
''' starts flash app '''

# importing Flask task
from flask import Flask
from flask import render_template

# instance of the class
app = Flask(__name__)


# route to tell what URL should trigger the function
@app.route('/', strict_slashes=False)
def hello_hbnb():
    ''' prints hello hbnb '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' prints HBNB'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_txt(text):
    ''' prints C followed by value of txt '''
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    ''' prints python followed by text'''
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    ''' prints python followed by text'''
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    ''' returns html page '''
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    ''' returns html page '''
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
