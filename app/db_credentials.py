from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


load_dotenv() 

DB_USER = os.getenv("DB_USER")
DB_PWD = os.getenv("DB_PWD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_DEBUG_MODE = False

def get_engine(db_user=DB_USER, db_pwd=DB_PWD, db_host=DB_HOST, db_name=DB_NAME, db_debug_mode=DB_DEBUG_MODE):
    # conn_str = f"mysql://{db_user}:{db_pwd}@{db_host}/{db_name}"
    conn_str = f"mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}/{db_name}"
    print(conn_str)
    
    return create_engine(conn_str, echo=DB_DEBUG_MODE)



def get_session():
    engine = get_engine()


    Session = sessionmaker(bind=engine)
    #SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return Session()

   