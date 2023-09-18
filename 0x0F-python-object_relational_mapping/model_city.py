#!/usr/bin/python3
"""
Python file that contains the class definition of a City
"""
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects import mysql
from model_state import Base


class City(Base):
    """
    This class inherits from Base and links to the MySQL table `cities`

    Attributes:
        id(int): Represents a column of an auto-generated, unique integer.
        name(str): Represents a column of a string with maximum 128 char.
    """
    __tablename__ = 'cities'

    id = Column('id', mysql.INTEGER(11), primary_key=True,
                autoincrement=True, nullable=False)

    name = Column('name', String(128), nullable=False)

    state_id = Column('state_id', mysql.INTEGER(11),
                      ForeignKey('states.id'), nullable=False)
