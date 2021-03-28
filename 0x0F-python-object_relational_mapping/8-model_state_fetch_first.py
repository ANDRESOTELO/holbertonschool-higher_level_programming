#!/usr/bin/python3
'''Script that prints the first State object from the database'''

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

    '''Query to fetch only first state in the table'''
    firstState = session.query(State).first()

    '''If the table states is empty, print Nothing followed by a
    new line'''
    if firstState:
        print("{}: {}".format(firstState.id, firstState.name))
    else:
        print("Nothing")
    session.close()
