#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
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
    result = session1.query(State.id, State.name).order_by(State.id).first()
    if result:
        print("{}: {}".format(*result))
    else:
        print("Nothing")

    session1.close()
