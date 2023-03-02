import multiprocessing
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from captcha_solver import captcha_solver

def select_option_by_text(select_elem, text):
    """Select an option from a dropdown by text."""
    options = Select(select_elem).options
    for option in options:
        if option.text == text:
            option.click()
            break

def select_birthday(driver: webdriver.Firefox, date):
    """Select the birth date of the customer."""
    year, month, day = date.split('-')
    print(day, month, year)
    select_option_by_text(driver.find_element(By.ID, 'birthday1'), day)
    select_option_by_text(driver.find_element(By.ID, 'birthmonth1'), month)
    select_option_by_text(driver.find_element(By.ID, 'birthyear1'), year)

def fill_personal_info(driver: webdriver.Firefox, customer):
    """Fill the personal information section of the form."""
    driver.find_element(By.ID, 'name1').send_keys(customer.first_name)
    driver.find_element(By.ID, 'surname1').send_keys(customer.last_name)
    driver.find_element(By.ID, 'localname1').send_keys(customer.first_name + ' ' + customer.last_name)
    select_option_by_text(driver.find_element(By.ID, 'nationality1'), 'Uzbekistan')
    select_birthday(driver, customer.birth_date.strftime('%Y-%m-%d'))
    driver.find_element(By.ID, 'passport1').send_keys(customer.passport_number)
    driver.execute_script(
        f"arguments[0].value = '{customer.passport_valid_date.strftime('%d-%m-%Y')}';",
        driver.find_element(By.ID, 'passportExpirationDate1')
    )
    driver.find_element(By.ID, 'email1').send_keys(customer.email)
    driver.find_element(By.ID, 'phone1').send_keys(customer.phone_number)

def fill_form(driver: webdriver.Firefox, customer):
    """Fill the entire form."""
    p = multiprocessing.Process(target=captcha_solver)
    p.start()
    order_by = "increase"
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, 'btnAppCountNext').click()
    fill_personal_info(driver, customer)

    driver.find_element(By.ID, 'btnAppPersonalNext').click()
    driver.find_element(By.ID, 'btnAppPreviewNext').click()

    driver.find_element(By.ID, 'personalapproveTerms').click()
    driver.find_element(By.ID, 'btnCreditCard').click()

    starting_journey = datetime.today().date() + timedelta(days=10)
    ending_journey = starting_journey + timedelta(days=10)
    driver.execute_script(
        f"arguments[0].value = '{starting_journey.strftime('%d-%m-%Y')}';",
        driver.find_element(By.NAME, 'travelStartDate')
    )
    driver.execute_script(
        f"arguments[0].value = '{ending_journey.strftime('%d-%m-%Y')}';",
        driver.find_element(By.NAME, 'travelEndDate')
    )

    datepicker = driver.find_element(By.ID, 'tarihGoster')
    driver.execute_script("arguments[0].style.display = 'block';", datepicker)
    driver.find_element(By.XPATH, "//input[@class='form-control calendarinput']").click()
    days = driver.find_elements(By.XPATH, "//td[@class='day']")
    days_text = [day.text for day in days]
    print(days_text)
    input()
    day_to_click = days[0] if order_by == 'increase' else days[-1]
    day_to_click.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'noPrime')]"))).click()
    driver.find_element(By.ID, 'btnAppCalendarNext').click()

    p.join()
    code = p.result()
    print(code)

    while code == "ERROR_CAPTCHA_UNSOLVABLE":
        code = captcha_solver()

    driver.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{code}'")
    driver.find_element(By.ID, 'btnAppServicesNext').click()
    driver.quit()
