#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ as env


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')

    if env.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """filestorage relationship between state and city"""
            lst = [val for key, val in models.storage.all(models.City).items()
                   if val.state_id == self.id]
            return lst
