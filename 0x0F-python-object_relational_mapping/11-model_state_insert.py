#!/usr/bin/python3
'''Script that adds the State object Louisiana to the database'''

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
    # New state object
    new_state = State(name='Louisiana')
    # Add new state
    session.add(new_state)

    newRow = session.query(State).filter(State.name == 'Louisiana')

    print('{}'.format(newRow[0].id))

    # Statement to update table
    session.commit()

    session.close()
