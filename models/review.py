#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base import BaseModel
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""
