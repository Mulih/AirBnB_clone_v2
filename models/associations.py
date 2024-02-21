#!/usr/bin/python3
from sqlalchemy import Table, Column, Integer, ForeignKey
from models.base_model import Base

place_amenity = Table('place_amenity', Base.metadata,
        Column('place_id', Integer, ForeignKey('place.id')),
        Column('amenity_id', Integer, ForeignKey('amenities.id'))
)
