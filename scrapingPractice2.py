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
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import traceback
from selenium.webdriver.common.proxy import Proxy, ProxyType

def get_driver():
    try:
        print("Running on: local")
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("start-maximized")
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_experimental_option("useAutomationExtension", False)
        #options.add_argument("--disable-dev-shm-usage")
        #proxy = Proxy()
        #proxy.proxy_type = ProxyType.MANUAL
        #proxy.http_proxy = "your_proxy:port"
        #proxy.ssl_proxy = "your_proxy:port"

        #capabilities = webdriver.DesiredCapabilities.CHROME
        #proxy.add_to_capabilities(capabilities)
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        print("Chrome is running and reachable.")
        
        return driver
    except Exception as e:
        print("Chrome is not running:", e)
        traceback.print_exc()  # Prints the full traceback for better debugging

# Example usage
if __name__ == "__main__":
    driver = get_driver()
    if driver:
        try:
            driver.get('https://www.adidas.com/us')
            print(driver.title)
        except Exception as e:
            print("Error during navigation:", e)
            traceback.print_exc()
        finally:
            driver.quit()



try:
    #driver.get('https://example.com')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gl-carousel-system__item-0"]/div/section[1]/a/span/img')))
    print(driver.page_source)
finally:
    driver.quit()
#image_element = driver.find_element(By.XPATH ,'//*[@id="gl-carousel-system__item-0"]/div/section[1]/a/span/img')
#image_element.click()
#time.sleep(5)
