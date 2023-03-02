import os

from dotenv import load_dotenv
from selenium import webdriver

def make_driver() -> webdriver.Firefox:
    """
    Creates and returns a new headless Firefox WebDriver instance.
    """
    load_dotenv()
    data_url = os.environ.get('DATA_URL')

    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')

    driver = webdriver.Firefox()
    driver.get(data_url)

    return driver
