from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# Set Chrome options to use an existing Chrome profile
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('user-data-dir=C:/Users/YourUserName/AppData/Local/Google/Chrome/User Data/Default')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')

# Initialize the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to the webpage
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Rest of your code
time.sleep(20)
# Close the driver when done
driver.quit()
