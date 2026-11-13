import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv();

DB_ADDRESS = os.environ["SQLITE_ADDRESS"]

engine = create_engine(f"sqlite:///{DB_ADDRESS}", connect_args={
    'check_same_thread': False
})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()