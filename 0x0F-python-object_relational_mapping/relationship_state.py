#!/usr/bin/python3
"""
Python file that contains the class definition of a
State and an instance Base = declarative_base()
"""
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import relationship, declarative_base
from model_state import Base


Base = declarative_base()


class State(Base):
    """
    This class inherits from Base and links to the MySQL table `states`

    Attributes:
        id(int): Represents a column of an auto-generated, unique integer.
        name(str): Represents a column of a string with maximum 128 char.
    """
    __tablename__ = 'states'

    id = Column('id', mysql.INTEGER(11), primary_key=True,
                autoincrement=True, nullable=False)

    name = Column('name', String(128), nullable=False)

    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")
