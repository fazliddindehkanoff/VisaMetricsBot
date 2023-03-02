import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
db_name = os.environ.get('DB_NAME')

engine = create_engine(f'sqlite:///{db_name}.db', echo=True)
Session = sessionmaker(bind=engine)

def get_session():
    return Session()
