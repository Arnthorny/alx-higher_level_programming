#!/usr/bin/python3
"""
A script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City


if (__name__ == '__main__'):

    args = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(*args))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    calif = State(name="California")
    calif.cities.append(City(name="San Francisco"))

    session.add(calif)
    session.commit()
    session.close()
