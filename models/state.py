#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        from models.file_storage import FileStorage
        fs = FileStorage()
        return fs.get_cities_by_state