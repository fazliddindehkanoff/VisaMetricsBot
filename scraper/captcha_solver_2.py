import re
import random
import time
import os
import urllib

import pydub
import speech_recognition as sr

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Define constants for user agents and Firefox options
USER_AGENT_LIST = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
)   

FIREFOX_OPTIONS = webdriver.FirefoxOptions()
FIREFOX_OPTIONS.add_argument("--no-sandbox")
FIREFOX_OPTIONS.add_argument("--disable-setuid-sandbox")
FIREFOX_OPTIONS.add_argument("--disable-dev-shm-using")
FIREFOX_OPTIONS.add_argument("--disable-extensions")
FIREFOX_OPTIONS.add_argument("--disable-gpu")
FIREFOX_OPTIONS.add_argument("start-maximized")
FIREFOX_OPTIONS.add_argument("disable-infobars")
FIREFOX_OPTIONS.add_argument("--disable-blink-features=AutomationControlled")

def get_driver():
    """Initialize the Firefox driver with random user agent."""
    user_agent = random.choice(USER_AGENT_LIST)
    FIREFOX_OPTIONS.add_argument(f"user-agent={user_agent}")
    driver = webdriver.Firefox(options=FIREFOX_OPTIONS)
    driver.implicitly_wait(5)
    return driver

def solve_recaptcha(driver):
    """Solve reCAPTCHA using audio challenge."""
    driver.get("https://www.google.com/recaptcha/api2/demo")

    frames = driver.find_elements(By.TAG_NAME, "iframe")
    recaptcha_control_frame = None
    recaptcha_challenge_frame = None

    for frame in frames:
        if re.search('reCAPTCHA', frame.get_attribute("title")):
            recaptcha_control_frame = frame
            
        if re.search('recaptcha challenge', frame.get_attribute("title")):
            recaptcha_challenge_frame = frame

    # Press tab key multiple times to focus on the checkbox
    tab_times = 14
    body_tag = driver.find_elements(By.TAG_NAME, "body")[-1]
    for _ in range(tab_times):
        delay_time = random.choice((0.3, 0.4, 0.5, 0.75, 1))
        time.sleep(delay_time)
        body_tag.send_keys(Keys.TAB)

    # Click on the checkbox to activate reCAPTCHA
    driver.switch_to.frame(recaptcha_control_frame)
    driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border").click()

    driver.switch_to.default_content()
    driver.switch_to.frame(recaptcha_challenge_frame)
    driver.find_element(By.ID, "recaptcha-audio-button").click()

    # Download and convert the audio file
    src = driver.find_element(By.ID, "audio-source").get_attribute("src")
    path_to_mp3 = os.path.normpath(os.path.join(os.getcwd(), "sample.mp3"))
    path_to_wav = os.path.normpath(os.path.join(os.getcwd(), "sample.wav"))
    urllib.request.urlretrieve(src, path_to_mp3)

    try:
        sound = pydub.AudioSegment.from_mp3(path_to_mp3)
        sound.export(path_to_wav, format="wav")
        sample_audio = sr.AudioFile(path_to_wav)
    except Exception as e:
        print("[ERR] Unable to convert audio file: ", e)
        return None

    # Convert the audio to text using Google Voice Recognition
    r = sr.Recognizer()
    with sample_audio as source:
        audio = r.record(source)
    key = r.recognize_google(audio)

    # Submit the reCAPTCHA response
    driver.switch_to.default_content()
    driver.switch_to.frame(recaptcha_challenge_frame)
    audio_response = driver.find_element(By.ID, "audio-response")
    audio_response.send_keys(key.lower())
    audio_response.send_keys(Keys.ENTER)
    return key.lower()

print(solve_recaptcha())