#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ This class defines the City model for the database table 'cities'.
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
     places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
