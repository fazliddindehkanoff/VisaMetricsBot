from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def check_availability(driver: webdriver.Firefox):
    user_living_place = "Andijan"
    driver.find_element(By.ID, "country").find_elements(By.TAG_NAME, "option")[2].click()
    driver.find_element(By.ID, "visitingcountry").find_elements(By.TAG_NAME, "option")[1].click()
    cities = Select(driver.find_element(By.ID, "city"))
    values = [option.text for option in cities.options]

    if user_living_place in values:
        cities.select_by_visible_text(user_living_place)

    driver.find_element(By.ID, "office").find_elements(By.TAG_NAME, "option")[1].click()
    driver.find_element(By.ID, "officetype").find_elements(By.TAG_NAME, "option")[1].click()
    driver.find_element(By.ID, "totalPerson").find_elements(By.TAG_NAME, "option")[1].click()

    available_day_info = driver.find_element(By.ID, "availableDayInfo").find_element(By.TAG_NAME, "div").text


    if available_day_info != "Sana mavjud emas":
        return driver
    
    return False