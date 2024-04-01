#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref


class Amenity(BaseModel, Base):
    __tablename__ = 'users'
    name = Column(String(128), nullable=False)
    
    place_amenities = relationship("Place", secondary="place_amenity", viewonly = False)