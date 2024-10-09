from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # You need to import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to the webpage
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Code for Scraping
## Static Locators
CSS_Locator_1 = 'div#mp-tfa'
CSS_Locator_2 = 'div#mp-itn'
CSS_Locator_3 = 'div#mp-dyk'
CSS_Locator_4 = 'div#mp-otd'

## Locator List 
locator_list = [CSS_Locator_1, CSS_Locator_2, CSS_Locator_3, CSS_Locator_4]

## Link Dictionary
link_dictionary = {}

## Loop Through Locators
for locator in locator_list:
    try:
        # Wait for the element to load
        time.sleep(2)  # Add a delay to ensure page is loaded

        # Locate the element using the CSS selector
        div_element = driver.find_element(By.CSS_SELECTOR, locator)

        # Create a list to hold link info
        info_list = []
        
        # Loop through all anchor tags within the located div
        for link in div_element.find_elements(By.TAG_NAME, 'a'):
            info_dict = {
                'title': link.get_attribute('title'),
                'text': link.text,
                'href': link.get_attribute('href')
            }
            info_list.append(info_dict)
        
        # Add the collected info to the dictionary
        link_dictionary[locator] = info_list

    except Exception as e:
        print(f"Error with locator {locator}: {e}")

# Print the scraped data
print(link_dictionary)

# Rest of your code
time.sleep(20)  # For demonstration purposes

# Close the driver when done
driver.quit()
