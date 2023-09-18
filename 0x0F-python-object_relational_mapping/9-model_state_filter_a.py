#!/usr/bin/python3
"""
A script that lists all State objects that
contain the letter `a` from the database hbtn_0e_6_usa
"""
import sys
import sqlalchemy
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if (__name__ == '__main__'):

    args = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(*args))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session1 = Session()
    result = (session1.query(State.id, State.name).order_by(State.id)
              .filter(State.name.contains('a')).all())
    for row in result:
        print("{}: {}".format(*row))

    session1.close()
