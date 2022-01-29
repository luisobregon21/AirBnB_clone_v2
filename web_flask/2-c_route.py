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
    ''' prints value of txt '''
    if text:
        text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
