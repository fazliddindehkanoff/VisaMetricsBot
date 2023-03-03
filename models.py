import os

from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv

load_dotenv()

# database credentials
username = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
database_name = os.environ.get("POSTGRES_DB")
port = os.environ.get("PORT")

# creating connection to my database
Base = declarative_base()
metadata = Base.metadata
engine = create_engine(f"postgresql://{username}:{password}@db:{port}/{database_name}")

# Define ORM classes
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
    ordered = Column(Boolean)
    plan = Column(String)

    def __repr__(self):
        return f"Customer(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email})"

    @classmethod
    def get_all(cls):
        with engine.connect() as conn:
            query = cls.__table__.select()
            result = conn.execute(query)
            return [cls(**row) for row in result]
