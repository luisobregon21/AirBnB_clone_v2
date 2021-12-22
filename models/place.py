#!/usr/bin/python3
""" Place Module for HBNB project """
import os
import models
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey, String, Float, Column, Integer
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref='place',
                               cascade='all, delete, delete-orphan')
    else:
        @property
        def reviews(self):
            """return list of Review instances with place_id
            equals to self.id(Place instance)"""
            reviewlist = []
            for reviews in models.storage.all(Review).values():
                if self.id == reviews.place_id:
                    reviewlist.append(reviews)
            return reviewlist
