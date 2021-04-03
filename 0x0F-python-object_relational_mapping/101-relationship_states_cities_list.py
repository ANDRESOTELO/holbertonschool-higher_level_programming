#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects
"""

import sys
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
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

    query = session.query(State).order_by(State.id).all()
    for state in query:
        print("{}: {}".format(state.id, state.name))

        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
