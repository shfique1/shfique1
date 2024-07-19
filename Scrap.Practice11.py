
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
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("start-maximized")
        options.add_argument("--ignore-certificate-errors")

 
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        print("Chrome is running and reachable.")
 
        return driver
    except Exception as e:
 
        print("Chrome is not running:", e)
 
driver = get_driver()
driver.get('https://www.jcpenney.com/g/men/view-all-mens-brands?id=cat100290093')
time.sleep(2)

#url = "http://example.com"

# Open the webpage
#driver.get(url)

# Wait until the images are loaded (adjust the selector to fit the actual page)
wait = WebDriverWait(driver, 10)
images = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//Li[@class='pAB7b D2LxB gQ4Qt QLk4z false RQ2ya false']")))

# Iterate through all images and click one by one
print("length of the list is ", len(images))
wait = WebDriverWait(driver, 20)  # Increased wait time to 20 seconds
images = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//Li[@class='pAB7b D2LxB gQ4Qt QLk4z false RQ2ya false']")))

    # Check if images are found
print("Number of images found: ", len(images))
if not images:
        print("No images found with the given XPath. Please check the XPath and ensure the elements are present.")

    # Iterate through all images and click one by one
for index in range(len(images)):
        # Re-fetch the images
        images = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//Li[@class='pAB7b D2LxB gQ4Qt QLk4z false RQ2ya false']")))

        # Scroll into view
        driver.execute_script("arguments[0].scrollIntoView();", images[index])
        
        # Click the image
        ActionChains(driver).move_to_element(images[index]).click().perform()
        
        # Add a wait to observe the click action
        wait.until(EC.staleness_of(images[index]))  # Wait until the element is no longer attached to the DOM
        
        # Navigate back
        driver.back()

        # Optionally, add a small delay
        import time
        time.sleep(2)  # Adjust the sleep time if necessary
    
    # Close the WebDriver
driver.quit()