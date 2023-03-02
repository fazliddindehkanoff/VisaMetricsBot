from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import Select, WebDriverWait

from Scraper.captcha_solver import captcha_solver
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)

def check_availability():
    user_living_place = "Andijan"
    driver.get("https://uz-appointment.visametric.com/uz/appointment-form")

    country_elem = driver.find_element(By.ID, "country").find_elements(By.TAG_NAME, "option")[2].click()
    visiting_country = driver.find_element(By.ID, "visitingcountry").find_elements(By.TAG_NAME, "option")[1].click()
    cities = Select(driver.find_element(By.ID, "city"))
    values = [option.text for option in cities.options]

    if user_living_place in values:
        cities.select_by_visible_text(user_living_place)

    office = driver.find_element(By.ID, "office").find_elements(By.TAG_NAME, "option")[1].click()
    officetype = driver.find_element(By.ID, "officetype").find_elements(By.TAG_NAME, "option")[1].click()
    totalPerson = driver.find_element(By.ID, "totalPerson").find_elements(By.TAG_NAME, "option")[1].click()

    available_day_info = driver.find_element(By.ID, "availableDayInfo").find_element(By.TAG_NAME, "div").text
    
    if available_day_info != "Sana mavjud emas":
        fill_form()
    
    return available_day_info != "Sana mavjud emas"

def fill_form():
    first_name = "Samandar"
    last_name = "Sa'dullayev"
    birth_date = datetime(2002,3,22).strftime("%Y-%m-%d")
    passport_number = 4625204 
    passport_valid_date = datetime(2032,5,2).strftime("%d-%m-%Y")
    email = "test@gmail.com"
    phone_number = "+998905512460"
    order_by = "increase"
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, "btnAppCountNext").click()
    driver.find_element(By.ID, "name1").send_keys(first_name)
    driver.find_element(By.ID, "surname1").send_keys(last_name)
    driver.find_element(By.ID, "localname1").send_keys(first_name+" "+last_name)
    driver.find_element(By.ID, "nationality1").find_elements(By.TAG_NAME, "option")[1].click()
    birthdays = Select(driver.find_element(By.ID, "birthday1"))
    values = [option.text for option in birthdays.options]
    driver.find_element(By.ID, "birthday1").find_elements(By.TAG_NAME, "option")[values.index(birth_date.split("-")[2])].click()
    birthmonths = Select(driver.find_element(By.ID, "birthmonth1"))
    values = [option.text for option in birthmonths.options]
    driver.find_element(By.ID, "birthmonth1").find_elements(By.TAG_NAME, "option")[values.index(birth_date.split("-")[1])].click()
    birthyears = Select(driver.find_element(By.ID, "birthyear1"))
    values = [option.text for option in birthyears.options]
    driver.find_element(By.ID, "birthyear1").find_elements(By.TAG_NAME, "option")[values.index(birth_date.split("-")[0])].click()
    driver.find_element(By.ID, "passport1").send_keys(passport_number)
    date_input = driver.find_element(By.ID, "passportExpirationDate1")
    driver.execute_script("arguments[0].value = arguments[1];", date_input, passport_valid_date)
    driver.find_element(By.ID, "email1").send_keys(email)
    driver.find_element(By.ID, "phone1").send_keys(phone_number)
    # next page
    driver.find_element(By.ID, "btnAppPersonalNext").click()
    # next page apply
    btn = driver.find_element(By.ID, "btnAppPreviewNext")
    driver.execute_script("arguments[0].scrollIntoView();", btn)
    wait.until(EC.visibility_of_element_located((By.ID, 'btnAppPreviewNext')))
    btn.click()
    # check agree to personal info
    driver.find_element(By.ID, "personalapproveTerms").click()
    # next to final page
    driver.find_element(By.ID, "btnCreditCard").click()
    # starting date
    today = datetime.today().date()
    starting_journey = today + timedelta(days=10)
    date_input = driver.find_element(By.ID, "flightDate").find_element(By.TAG_NAME, "input")
    driver.execute_script("arguments[0].value = arguments[1];", date_input, starting_journey.strftime("%d-%m-%Y"))
    ending_journey = today + timedelta(days=20)
    date_input = driver.find_element(By.ID, "travelenddate").find_element(By.TAG_NAME, "input")
    driver.execute_script("arguments[0].value = arguments[1];", date_input, ending_journey.strftime("%d-%m-%Y"))
    # go to the final stage 
    if order_by == "increase":
        element = driver.find_element(By.ID, "tarihGoster")
        driver.execute_script("arguments[0].style.display = 'block';", element)
        date = driver.find_element(By.XPATH, "//div[@id='datepicker']")
        date.click()
        days = driver.find_element(By.XPATH, "//div[@class='datepicker-days']").find_elements(By.XPATH, "//td[@class='day']")
        days = [day.text for day in days]
        date.find_element(By.XPATH, "//div[@class='datepicker-days']").find_element(By.XPATH, f"//td[text()='{days[0]}']").click()
        my_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'noPrime')]")))
        my_button.click()
    driver.find_element(By.ID, "btnAppCalendarNext").click()
    # solve captcha 
    code = captcha_solver()
    driver.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{code}'")
    # kill :)
    driver.find_element(By.ID, "btnAppServicesNext").click()
    # link of file
    print(driver.find_elements(By.TAG_NAME, "a")[-1].get_attribute("href"))

print(check_availability())
driver.quit()
