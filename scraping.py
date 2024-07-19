import time
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

def get_driver():
 
    
 
    try:
 
        print(f"Running on: local")
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("start-maximized")
 
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        print("Chrome is running and reachable.")
 
        return driver
    except Exception as e:
 
        print("Chrome is not running:", e)
 
driver = get_driver()
driver.get('https://www.adidas.com/us/argentina-24-messi-home-jersey/IX7790.html')
time.sleep(2)
driver.execute_script("window.scrollTo(0, 700)")
time.sleep(1)
web_element = driver.find_element(By.XPATH,'//*[@id="main-content"]/div[2]/div[2]/div[1]/h1')
# print(f"WEB ELEMENT IS:{web_element}")
print('-----------------------------------------------------------------------------------------------------------')
web_text = web_element.get_attribute('innerText')
# print('TEXT IS:',web_text)
time.sleep(2)
button = driver.find_element(By.XPATH,'//*[@id="navigation-target-reviews"]/div/button')
print(button)
button.click()