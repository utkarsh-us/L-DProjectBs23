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
driver.get("https://en.wikipedia.org/wiki/Main_Page")

#click on a link 
driver.switch_to.new_window('window')

#new window new url 
driver.get("https://books.toscrape.com/")

# Close the current Widnows 
driver.close()  

