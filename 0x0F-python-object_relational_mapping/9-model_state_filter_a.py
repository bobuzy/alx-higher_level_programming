#!/usr/bin/python3
"""
Module definition that lists all State objects that
contain the letter a from the database
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    all_states = session.query(State).filter(State.name.
                                         like('%a%')).order_by(State.id).all()

    for state in all_states:
        print("{}: {}".format(state.id, state.name))
    session.close()
