import schedule
import time
from datetime import date

from checker import check_availability
from driver import make_driver
from fill_form import fill_form
from models import Customer
from common.get_session import get_session

def check_form_availability():
    driver = make_driver()
    session = get_session()
    new_driver = check_availability(driver)
    if new_driver:
        fill_form(new_driver, session.query(Customer).first())

schedule.every(1).minutes.do(check_form_availability)

while True:
    schedule.run_pending()
    time.sleep(1)
