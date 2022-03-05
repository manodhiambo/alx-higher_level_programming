#!/usr/bin/python3
"""script that creates the State “California” with the City “San Francisco”
   from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    nstate = "California"
    ncity = "San Francisco"

    newState = State(name=nstate)

    newCity = City(name=ncity, state=newState)

    session.add(newCity)

    session.commit()
