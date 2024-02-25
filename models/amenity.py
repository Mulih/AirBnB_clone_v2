#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.associations import place_amenity

place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', Integer, ForeignKey('places.id')),
    Column('amenity_id', Integer, ForeignKey('amenities.id')),
    extend_existing=True
)

class Amenity(BaseModel, Base):
    """Represents an Amenity for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table amenities.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Amenities.
        name (sqlalchemy String): The amenity name.
        place_amenities (sqlalchemy relationship): Place-Amenity relationship.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

    places = relationship("Place", secondary=place_amenity, back_populates="amenities")
