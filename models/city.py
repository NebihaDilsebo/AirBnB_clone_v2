#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models.place import Place
from models.base_model import BaseModel, Base
from os import getenv

class City(BaseModel, Base):
    """ This class defines the City model for the database table 'cities'.
    """
    __tablename__ = "cities"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        state_id = ''
        name = ''

