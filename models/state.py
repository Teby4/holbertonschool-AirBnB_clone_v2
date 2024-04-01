#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        class State(BaseModel):

            @property
            def cities(self):
                from models.city import City
                from models import storage
                list_cities = []
                for i in storage.all():
                    if i.state_id == self.id:
                        list_cities.append(i)
                return list_cities
