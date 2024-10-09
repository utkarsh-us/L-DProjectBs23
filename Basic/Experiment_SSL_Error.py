from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Set Chrome options to use an existing Chrome profile
print("1")
chrome_options = Options()
chrome_options.add_argument('user-data-dir=C:/Users/YourUserName/AppData/Local/Google/Chrome/User Data/Default')

# Initialize the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

# Navigate to the webpage
driver.get("http://www.dummypoint.com/seleniumtemplate.html")

# Rest of your code

# Close the driver when done
driver.quit()
