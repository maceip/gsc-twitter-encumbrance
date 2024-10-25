import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random
import os
from dotenv import load_dotenv

#load_dotenv()


BASE_URL = "http://localhost:3000"
REGISTER_OR_LOGIN_ENDPOINT = f"{BASE_URL}/login"
CALLBACK_ENDPOINT = f"{BASE_URL}/callback"


PASSWORD = os.getenv("TWITTER_PASSWORD")
if not PASSWORD:
    raise ValueError("TWITTER_PASSWORD not found in .env file")

options = ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--no-first-run')
options.add_argument('--no-pings')
options.add_argument('--disable-first-run-ui')
options.add_argument('--disable-gaia-services')
options.add_argument('--single-process')
driver = uc.Chrome(headless=True, use_subprocess=False, browser_executable_path='/usr/bin/chromium', options=options)

url = "https://twitter.com/i/flow/login"
driver.get(url)

username = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'input[autocomplete="username"]')
    )
)
username.send_keys("grouchy_mev")
username.send_keys(Keys.ENTER)

password = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]'))
)
print('password')
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(5)

driver.get(REGISTER_OR_LOGIN_ENDPOINT)

time.sleep(5)
