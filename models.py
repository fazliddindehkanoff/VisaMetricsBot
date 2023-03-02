import os

from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()
db_name = os.environ.get('DB_NAME')

Base = declarative_base()
metadata = Base.metadata
engine = create_engine(f'sqlite:///{db_name}.db', echo=True)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    nationality = Column(String)
    birth_date = Column(Date)
    passport_number = Column(Integer)
    passport_valid_date = Column(Date)
    email = Column(String)
    phone_number = Column(Integer)
    is_archived = Column(Boolean)
    ordered = Column(Boolean)
    plan = Column(String)
