#!/usr/bin/python3
<<<<<<< HEAD
"""This is the place class"""
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity, place_amenity
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import models


class Place(BaseModel, Base):
    """Represents a Place for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table places.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store places.
        city_id (sqlalchemy String): The place's city id.
        user_id (sqlalchemy String): The place's user id.
        name (sqlalchemy String): The name.
        description (sqlalchemy String): The description.
        number_rooms (sqlalchemy Integer): The number of rooms.
        number_bathrooms (sqlalchemy Integer): The number of bathrooms.
        max_guest (sqlalchemy Integer): The maximum number of guests.
        price_by_night (sqlalchemy Integer): The price by night.
        latitude (sqlalchemy Float): The place's latitude.
        longitude (sqlalchemy Float): The place's longitude.
        reviews (sqlalchemy relationship): The user-Review relationship.
        amenities (sqlalchemy relationship): The user-Amenity relationship.
        amenity_ids (list): id list of all linked amenities

    """

    __tablename__ = "places"

    if getenv('HBNB_TYPE_STORAGE') == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(128))
        number_rooms = Column(Integer, default=0)
        number_bathrooms = Column(Integer, default=0)
        max_guest = Column(Integer, default=0)
        price_by_night = Column(Integer, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship('Amenity', secondary=place_amenity,
                                 back_populates='place_amenities',
                                 viewonly=False)
        amenity_ids = []
    else:
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Get a list of all linked Reviews.
            """

            review_list = []

            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    review_list.append(review)

            return review_list

        @property
        def amenities(self):
            """Get and Set linked Amenities.
            """

            amenity_list = []

            for amenity in models.storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)

            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """Adding an Amenity.id to the amenity_ids
            """

            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
=======
""" Place Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ This class defines the Place model for the database table 'places'.
    """
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

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")

        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """ Returns list of reviews.id """
            var = models.storage.all()
            listb = []
            result = []
            for key in var:
                review = key.replace('.', ' ')
                review = shlex.split(review)
                if (review[0] == 'Review'):
                    listb.append(var[key])
            for elem in listb:
                if (elem.place_id == self.id):
                    result.append(elem)
            return (result)

        @property
        def amenities(self):
            """ Returns list of amenity ids """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """ Appends amenity ids to the attribute """
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
>>>>>>> ffd5afe39459aa2a177d9fda6929c411a38840d4
