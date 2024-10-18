from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

# Initialize the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to the webpage
driver.get("https://jqueryui.com/datepicker/")

# Find Element 
iframe_element = driver.find_element(By.CSS_SELECTOR, 'iframe.demo-frame')

# Switch to frame 
driver.switch_to.frame(iframe_element)

# Change Element
input_element = driver.find_element(By.ID, 'datepicker')

# Click on the element 
input_element.click()

# Select the current date time 
NOW = datetime.now()
YEAR = NOW.year 
MONTH = NOW.month 
DAY = NOW.day

# Corrected XPath expression
Date_Path = f'//td[@data-month="{MONTH-1}" and @data-year="{YEAR}"]/a[text()="{DAY}"]'

date_element = driver.find_element(By.XPATH, Date_Path)

print(date_element.text)

input_element.clear()

input_element.send_keys(f'{MONTH}/{DAY}/{YEAR}')

input_element.click()
