#!/usr/bin/python3
"""
City relationship
"""

import sys
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    data_base = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user_name, password, data_base),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    state = State(name='California')
    state.cities = [City(name='San Francisco')]

    session.add(new_state)
    session.commit()
    session.close()
