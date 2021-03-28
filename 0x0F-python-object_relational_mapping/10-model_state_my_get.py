#!/usr/bin/python3
'''
Script that prints the State object with the name passed as
argument from the database
'''

from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session
from sys import argv


if __name__ == "__main__":
    user_name = argv[1]
    password = argv[2]
    data_base = argv[3]
    st_argv = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user_name, password, data_base),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)
    f_query = State.name == st_argv
    state = session.query(State).filter(f_query).all()

    if bool(state) is True:
        print("{}".format(state[0].id))  # list [[id, name], ]
    else:
        print("Not found")
    session.close()
