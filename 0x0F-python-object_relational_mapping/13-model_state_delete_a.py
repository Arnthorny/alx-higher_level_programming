#!/usr/bin/python3
"""
A script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
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
    result = (session1.query(State).filter(State.name.contains('a')).all())

    for state in result:
        session1.delete(state)
    session1.commit()
    session1.close()
