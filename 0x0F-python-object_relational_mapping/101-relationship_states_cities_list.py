#!/usr/bin/python3
"""
A script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
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
    query = session.query(State).join(City).order_by(State.id, City.id)
    results = query.all()

    for state in results:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()
