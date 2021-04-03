#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects,
contained in the database
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
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

    query = session.query(City).order_by(City.id).all()

    for city in query:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
