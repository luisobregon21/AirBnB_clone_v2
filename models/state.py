#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade='all, delete, delete-orphan')
    else:
        @property
        def cities(self):
            '''
        Getter attribute cities that returns the list of City
        instances with state_id equals to the current State.id
        '''

        cities_in_state = []
        for city in models.storage.all(City).values():
            if self.id == city:
                print("HERE IS THE FUCKING CITY: ", city)
                cities_in_state.append(city)
        print("\n\n\nThis is the LIST:", cities_in_state, "\n\n")
        return cities_in_state
