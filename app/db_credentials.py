from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os



def get_engine():
    # conn_str = f"mysql://{db_user}:{db_pwd}@{db_host}/{db_name}"
    # conn_str = f"mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}/{db_name}"
    conn_str = f"sqlite:///historias.db"
    print(conn_str)
    
    return create_engine(conn_str, echo=False)



def get_session():
    engine = get_engine()


    Session = sessionmaker(bind=engine)
    #SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return Session()

   