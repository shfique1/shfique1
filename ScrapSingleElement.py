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
#driver.execute_script("window.scrollTo(0, 700)")
#element_xpath = '//*[@id="gallery-product-list"]/div[2]/div/ul/li[1]/div/div/div/div/div[1]/div[2]/a/div/div/div/img'

#tittle_xpath='//*[@id="productTitle-false"]'
#image_element = driver.find_element(By.XPATH, element_xpath)
#actions = ActionChains(driver)
#actions.move_to_element(image_element).perform()

# Click on the image element
#image_element.click()
#actions.move_to_element(image_element).perform()

#Product_name=driver.find_element(By.XPATH, tittle_xpath)
#actions.move_to_element(Product_name).perform()


#print(Product_name.text)

#ul_element = driver.find_element(By.XPATH, '//*[@id="productOptionsColorList"]')

# Find all <li> elements within the <ul>
#li_elements = ul_element.find_elements(By.TAG_NAME, "li")


#color_buttons = driver.find_elements(By.XPATH, color_buttons_xpath)

# Iterate through each color button, click it, and retrieve the color name
# Iterate through each color button, click it, and retrieve the color name
#image_xpath = '//*[@id="gallery-product-list"]/div[2]/div/ul'  
#image_elements = driver.find_elements(By.CLASS_NAME, 'pAB7b D2LxB gQ4Qt QLk4z false RQ2ya false')
#pAB7b D2LxB gQ4Qt QLk4z false RQ2ya false
#Class name which will help me to iterate through all the page 
    #driver.execute_script("window.scrollTo(0, 500)")
#element=driver.fin
driver.execute_script(script="window.scrollTo(0, 500);")
time.sleep(2)
images=driver.find_elements(By.CLASS_NAME,'pAB7b D2LxB gQ4Qt QLk4z false RQ2ya false')
print("number of product on this page is ",len(images))
for image in images:
    # Scroll the image into view
    driver.execute_script("arguments[0].scrollIntoView();", image)
    
    # Wait until the image is clickable
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'pAB7b D2LxB gQ4Qt QLk4z false RQ2ya false')))
    
    # Click the image
    image.click()
    driver.back()

#
driver.quit()