#!/usr/bin/python3
""" City Module for HBNB project """

import sqlalchemy
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = Column(String(60), nullable=False, fore)
    name = Column(String(128), nullable=False)
    __tablename__ = 'cities'