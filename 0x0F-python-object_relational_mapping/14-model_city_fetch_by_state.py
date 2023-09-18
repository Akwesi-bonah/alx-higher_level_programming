#!/usr/bin/python3
"""
Cities in state
"""

from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    name = sys.argv[1]
    pwd = sys.argv[2]
    dbName = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(name, pwd, dbName),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in (session.query(State.name, City.id,
                                   City.name).filter(State.id == City.state_id)):
        print(instance[0] + ": (" + str(instance[1]) + ") " + instance[2])
