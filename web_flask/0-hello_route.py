#!/usr/bin/python3
''' Minimal flash app '''

# importing Flask task
from flask import Flask

# instance of the class
app = Flask(__name__)

# route to tell what URL should trigger the function
@app.route('/')
def hello_world():
    return 'Hola senpai!'
