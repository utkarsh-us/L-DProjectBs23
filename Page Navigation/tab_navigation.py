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
driver.switch_to.new_window('tab')

# get window handles 
window1 = driver.current_window_handle
print(window1)
#new window new url 
driver.get("https://books.toscrape.com/")

# List all the window handles currently available
windows2 = driver.window_handles



# Close the current Widnows 
driver.close()  

