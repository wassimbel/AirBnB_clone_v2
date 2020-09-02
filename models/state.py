#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """  return the list of City objects from storage
                 linked to the current State """
            c_list = {}
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    c_list.append(city)
            return c_list
