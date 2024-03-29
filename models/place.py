#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Int, Float, ForeignKey

class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Int(128), nullable=False, default=0)
    number_bathrooms = Column(Int(128), nullable=False, default=0)
    max_guest = Column(Int(128), nullable=False, default=0)
    price_by_night = Column(Int(128), nullable=False, default=0)
    latitude = Column(Float(128), nullable=False)
    longitude = Column(Float(128), nullable=False)
    amenity_ids = []
