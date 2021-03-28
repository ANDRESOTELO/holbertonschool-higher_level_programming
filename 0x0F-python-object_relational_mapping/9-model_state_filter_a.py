#!/usr/bin/python3
'''
Script that lists all State objects that contain the letter
a from the database
'''

from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session
from sys import argv


if __name__ == "__main__":
    user_name = argv[1]
    password = argv[2]
    data_base = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user_name, password, data_base),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)
    f_query = State.name.like('%a%')

    for state in session.query(State).filter(f_query).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
