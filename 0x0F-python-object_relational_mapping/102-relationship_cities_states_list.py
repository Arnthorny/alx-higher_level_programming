#!/usr/bin/python3
"""
A script that lists all City objects from the database hbtn_0e_101_usa
Format: <city id>: <city name> -> <state name>
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
    query = session.query(City).order_by(City.id)
    results = query.all()

    for city in results:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
