from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://jqueryui.com/droppable/") 

iframe_elemenet = driver.find_element(By.CSS_SELECTOR, 'iframe.demo-frame')

driver.switch_to.frame(iframe_elemenet)

action = ActionChains(driver=driver)

source_element = driver.find_element(By.ID, 'draggable')

target_element = driver.find_element(By.ID, 'droppable')

action.drag_and_drop(source_element, target_element).perform()



