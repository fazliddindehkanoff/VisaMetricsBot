import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
# database credentials
username = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
database_name = os.environ.get("POSTGRES_DB")
port = os.environ.get("PORT")

engine = create_engine(f"postgresql://{username}:{password}@db:{port}/{database_name}")
Session = sessionmaker(bind=engine)

def get_session():
    return Session()
