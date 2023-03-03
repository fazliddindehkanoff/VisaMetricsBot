from datetime import datetime, date

from models import Customer
from common.get_session import get_session

def register_customer(**kwargs):
    session = get_session()
    kwargs["birth_date"] = datetime.strptime(kwargs["birth_date"], "%Y-%m-%d").date()
    kwargs["passport_valid_date"] = datetime.strptime(kwargs["passport_valid_date"], "%Y-%m-%d").date()
    customer = Customer(**kwargs)

    session.add(customer)
    session.commit()

    return True