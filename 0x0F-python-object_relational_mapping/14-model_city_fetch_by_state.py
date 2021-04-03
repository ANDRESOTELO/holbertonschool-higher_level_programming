#!/usr/bin/python3
"""
Script that prints all City objects from the database
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    data_base = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user_name, password, data_base),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    query = session.query(State, City).filter(State.id == City.state_id)
    .order_by(City.id).all()

    for data in query:
        print("{}: ({}) {}"
              .format(data.State.name, data.City.id, data.City.name))
    session.close()
