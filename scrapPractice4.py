import time
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




def get_driver():
    try:
        print(f"Running on: local")
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("start-maximized")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        print("Chrome is running and reachable.")
        return driver
    except Exception as e:
        print("Chrome is not running:", e)
        return None


def main():
    driver = get_driver()
    
    if driver is None:
        print("Driver setup failed. Exiting.")
        return

    try:
        # Open the website
        url = 'https://www.jcpenney.com/g/men/view-all-mens-brands?id=cat100290093'
        print(f"Navigating to {url}")
        driver.get(url)

        # Wait for the page to load and elements to be present
        wait = WebDriverWait(driver, 10)
    except Exception as e:
        print(f"An error occurred: {e}")