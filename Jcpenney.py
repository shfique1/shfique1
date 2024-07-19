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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import random
 
def get_driver():
 
    
 
    try:
 
        print(f"Running on: local")
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("start-maximized")
        options.add_argument("--ignore-certificate-errors")
        #options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-notifications")
        options.add_experimental_option("prefs", {
         "profile.default_content_setting_values.notifications": 2
         })

#chrome_options.add_argument("--disable-dev-shm-usa
        #options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        options.add_argument("--enable-logging")
        options.add_argument("--v=1")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--disable-infobars')




 
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        print("Chrome is running and reachable.")
 
        return driver
    except Exception as e:
 
        print("Chrome is not running:", e)
 
driver = get_driver()
driver.get('https://www.jcpenney.com/g/men/view-all-mens-brands?id=cat100290093&page=25')
#time.sleep(2)
#driver.execute_script("window.scrollTo(0, 700)")
def random_delay(min_delay=1, max_delay=3):
    time.sleep(random.uniform(min_delay, max_delay))


# Function to scrape data from a single product page
def scrape_product():
    try:
        # XPath selectors for the product details
        title_xpath = "//h1[@id='productTitle-false']"
        actual_price_xpath = '//*[@id="contentContainer"]/section/section[3]/div[2]/div[1]/section[2]/div/div/section/div/div/span[1]'  
        #price_july_xpath = '//*[@id="contentContainer"]/section/section[3]/div[2]/div[1]/section[2]/section/div/div/div[1]'  
        Material_xpath = '//*[@id="productDescriptionContainer"]/div[1]/div[1]'  
        #color_boxes_xpath = '//*[@id="productOptionsColorList"]'  
        #color_name_xpath = '//*[@id="display-color-text-false"]/div/span[2]'  
        random_delay()
        # Extract information
        title1 = driver.find_element(By.XPATH, title_xpath)
        driver.execute_script("arguments[0].scrollIntoView();", title1)
        #title = WebDriverWait.until(EC.element_to_be_clickable((By.XPATH, title_xpath))).text
        title = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, title_xpath))
        ).text
        print(title)
        
        actual_price1 = driver.find_element(By.XPATH, actual_price_xpath)
        driver.execute_script("arguments[0].scrollIntoView();", actual_price1)
        #actual_price = WebDriverWait.until(EC.element_to_be_clickable((By.XPATH, actual_price_xpath))).text
        actual_price = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, actual_price_xpath))
        ).text
        print(actual_price)
        #price_july1 = driver.find_element(By.XPATH, price_july_xpath)
        #driver.execute_script("arguments[0].scrollIntoView();", price_july1)
        #price_july = WebDriverWait.until(EC.element_to_be_clickable((By.XPATH, price_july_xpath))).text

        material1 = driver.find_element(By.XPATH, Material_xpath)
        driver.execute_script("arguments[0].scrollIntoView();", material1)
        #description = WebDriverWait.until(EC.element_to_be_clickable((By.XPATH, description_xpath))).text
        material = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, Material_xpath))
        ).text
        



        # Extract available colors
        #color_elements = driver.find_elements(By.XPATH, color_boxes_xpath)
        colors = []
        colours = driver.find_elements(By.CSS_SELECTOR,'.pAB7b.ZJnQ-')

        for colour in colours:
            clist = colour.get_attribute('outerHTML')
            col = clist.split('data-for=')[-1].split('style=')[0]
            #print(col)
            colors.append(col)
            #.click()
            #WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, color_name_xpath)))
            





        return {
            "Title": title,
            "Actual Price": actual_price,
            #"Price for July": price_july,
            "Description": material,
            "Available Colors": ", ".join(colors)
        }
    except NoSuchElementException:
        return None


# Function to iterate through all product images on a page
def scrape_page():
    products = []
    

    image_xpath = "//Li[@class='pAB7b D2LxB gQ4Qt QLk4z false RQ2ya false']"
    wait = WebDriverWait(driver, 20)  
    images = wait.until(EC.presence_of_all_elements_located((By.XPATH, image_xpath)))
    #image_elements = driver.find_elements(By.XPATH, image_xpath)
    #driver.execute_script("window.scrollTo(0, 500)")
    #Iterate through all the images and click it one by one 
    random_delay() 
    for index in range(len(images)):
            # Re-fetch the images
            try:
                images = wait.until(EC.presence_of_all_elements_located((By.XPATH, image_xpath)))
                # Scroll into view
                driver.execute_script("arguments[0].scrollIntoView();", images[index])
                # Click the image
                ActionChains(driver).move_to_element(images[index]).click().perform()
                wait.until(EC.staleness_of(images[index]))  # Wait until the element is no longer attached to the DOM
                product_data = scrape_product()
                if product_data:
                    products.append(product_data)
                driver.back()
            except (NoSuchElementException, TimeoutException):

                print("time out or element not found lets continue")
                continue        
        #image_element.click()
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//body')))
        #time.sleep(2) 
        #driver.back()  # Go back to the main page
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, image_xpath)))
    
    return products
# Start scraping
all_products = scrape_page()

# Save to CSV if there is data
if all_products:
    df = pd.DataFrame(all_products)
    df.to_csv('scraped_products25.csv', index=False)
    print("Data saved to scraped_products.csv")
else:
    print("No data scraped.")
driver.quit()