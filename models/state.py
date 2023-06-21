#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.engine import storage_type
from models.city import City
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel):
    """ State class/ table model"""

    __tablename__ = 'States'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ''

        @property
        def cities(self):
            """Returns the list of 'City' instances with 'state_id' equals to the current"""

            cities = list()

            for _id, city in models.storage.all(City).items():
                if city.state_id == self.id:
                    cities.append(city)
            
            return cities
