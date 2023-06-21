#!/usr/bin/python3
"""This module defines the State class."""
import os
import models
from models.base_model import BaseModel, Base

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

from models.city import City
import shlex


class State(BaseModel, Base):
    """This class defines the State model for the database table 'states'.
    State inherits from BaseModel and Base (respect the order).
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """Returns the cities in this State."""
        val = models.storage.all()
        lista = []
        result = []
        for key in val:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lista.append(val[key])
        for elemt in lista:
            if (elemt.state_id == self.id):
                result.append(elemt)
        return (result)
