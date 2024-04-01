#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from os import getenv
from sqlalchemy.orm import relationship, backref
from models.amenity import Amenity

place_amenity = Table(
    'place_amenity',
    Base,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)
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

    amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
    reviews = relationship("Review", backref="place", cascade="delete")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        class Place(BaseModel):
            @property
            def reviews(self):
                from models.review import Review
                from models import storage
                reviews_list = [] 
                for i in storage.all():
                    if i.place_id == self.id:
                        reviews_list.append(i)
                return reviews_list

            @property
            def amenities(self):
                from models.amenity import Amenity
                from models import storage
                ammenity_list = [] 
                for i in Amenity.all():
                    if amenity.id in self.ids_amenity:
                        ammenity_list.append(i)
                return ammenity_list

            @amenities.setter
            def amenitie(self, value):
                """Setter for amenities"""
                if isinstance(value, Amenity):
                    self.amenity_ids.append(value.id)

            