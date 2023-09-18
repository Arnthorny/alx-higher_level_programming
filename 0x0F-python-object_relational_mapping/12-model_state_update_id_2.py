#!/usr/bin/python3
"""
A script that changes the name of a State object
from the database hbtn_0e_6_usa
Change the name of the State where id = 2 to New Mexico
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
    session = Session()
    # result = (session.query(State).filter(State.id == text(":id"))
    #         .params(id=2,))

    state_obj = session.get(State, 2)
    if state_obj:
        state_obj.name = "New Mexico"
    session.commit()
    session.close()
