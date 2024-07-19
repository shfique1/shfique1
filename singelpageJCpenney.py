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

def get_driver():
 
    
 
    try:
 
        print(f"Running on: local")
        options = webdriver.ChromeOptions()
        #options.add_argument("--incognito")
        options.add_argument("start-maximized")
 
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        print("Chrome is running and reachable.")
 
        return driver
    except Exception as e:
 
        print("Chrome is not running:", e)


driver = get_driver()
driver.get('https://www.jcpenney.com/g/men/view-all-mens-brands?id=cat100290093')
#time.sleep(9)
#driver.execute_script("window.scrollTo(0, 700)")
#time.sleep(1)
#web_element = driver.find_element(By.XPATH,'//*[@id="main-content"]/div[2]/div[2]/div[1]/h1')
# print(f"WEB ELEMENT IS:{web_element}")
#print('-----------------------------------------------------------------------------------------------------------')
#web_text = web_element.get_attribute('innerText')
# print('TEXT IS:',web_text)
#time.sleep(2)
#button = driver.find_element(By.XPATH,'//*[@id="navigation-target-reviews"]/div/button')
#print(button)
#button.click()
wait = WebDriverWait(driver, 10)
first_image_xpath = '//*[@id="gallery-product-list"]/div[2]/div/ul/li[1]/div/div/div/div/div[1]/div[2]/a/div/div/div/img' 
wait.until(EC.element_to_be_clickable((By.XPATH, first_image_xpath)))
# Extract data for each product
products = []
product_container_xpath = '//*[@id="gallery-product-list"]/div[2]/div/ul '
product_elements = driver.find_elements(By.XPATH, product_container_xpath)
for product in product_elements:
    try:
        # Click the product image to load details
        product.find_element(By.XPATH, first_image_xpath).click()
        
        # Extract the details
        name = driver.find_element(By.XPATH, '//*[@id="productTitle-false"]').text  # Replace with actual XPath
        price = driver.find_element(By.XPATH, '//*[@id="contentContainer"]/section/section[3]/div[2]/div[1]/section[2]/section/div/div/div[1]').text  # Replace with actual XPath
        color = driver.find_element(By.XPATH, '//*[@id="display-color-text-false"]/div/span[2]').text  # Replace with actual XPath
        description = driver.find_element(By.XPATH, '//*[@id="productDescriptionContainer"]/div[1]/div[1]/text()').text  # Replace with actual XPath
        
        # Append the data to the products list
        products.append({
            'Name': name,
            'Price': price,
            'Color': color,
            'Description': description
        })
        
        # Go back to the previous page to continue with the next product
        driver.back()
        wait.until(EC.element_to_be_clickable((By.XPATH, first_image_xpath)))
    
    except NoSuchElementException as e:
        print(f"Error: {e}")
        continue
# Close the driver
driver.quit()

# Create a DataFrame and save it to a CSV file
df = pd.DataFrame(products)
df.to_csv('products.csv', index=False)