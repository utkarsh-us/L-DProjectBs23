from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--headless')  # Headless mode (no UI)
options.add_argument('--disable-gpu')  # For headless compatibility

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


driver.get("https://books.toscrape.com/")

# Rest of your code

# Make sure to close the driver when done
driver.quit()
