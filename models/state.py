#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import os
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'

    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", passive_deletes=True, backref="state")

    @property
    def cities(self):
        """ Finds the instances of City whose state_id matches the id in State

            Returns:
                a list of city instances

        """
        city_instances = []
        for city_nameid, city_instance in models.storage.all(City).items():
            if city_instance.state_id == self.id:
                city_instances.append(city_instance)

        return city_instances
