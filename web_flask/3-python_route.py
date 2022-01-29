#!/usr/bin/python3
''' starts flash app '''

# importing Flask task
from flask import Flask

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
    if text:
        text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    ''' prints python followed by text'''
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
