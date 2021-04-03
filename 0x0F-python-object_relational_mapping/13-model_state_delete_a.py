#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter
a from the database
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session


if __name__ == "__main__":

    user_name = sys.argv[1]
    password = sys.argv[2]
    data_base = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user_name, password, data_base),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    query = session.query(State).filter(State.name.like('%a%')).all()

    for data in query:
        session.delete(data)

    session.commit()
    session.close()
