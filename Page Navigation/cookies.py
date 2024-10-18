from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to the webpage
driver.get("https://www.rwth-aachen.de/go/id/a/?lidx=1")

# driver get cookies
time.sleep(10)
cookies = driver.get_cookies()
print("Cookies collected:", cookies)

# Close the current Widnows 
driver.close()  

