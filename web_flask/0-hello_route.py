#!/usr/bin/python3
''' starts flash app '''

# importing Flask task
from flask import Flask

# instance of the class
app = Flask(__name__)


# route to tell what URL should trigger the function
@app.route('/', strict_slashes=False)
def hello_world():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
