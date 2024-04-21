
#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    # Define cities relationship outside of conditional blocks
    cities = relationship("City", cascade='all, delete', backref="state")

    # Optionally, conditionally set cascade parameter
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Getter method that returns the list of City objects"""
            from models import storage
            city_objs = []
            all_cities = storage.all("City")
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_objs.append(city)
            return city_objs
