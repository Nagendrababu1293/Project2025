import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver =webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/dropdown")
wait = WebDriverWait(driver, 10)

dd_list = Select(driver.find_elements(By.XPATH,"//select[@id = 'dropdown']"))
options =dd_list.options
for option in options:
    if option.text == 'Option 1':
        option.click()
        print(option.is_selected())
        #print(option.text)

""" dd.select_by_visible_text("Option 2")
# time.sleep(5)
# 
# dd.select_by_index(1)
# time.sleep(5)
# """"""
# dd.select_by_value("2")
# time.sleep(10)

"""

# driver.find_elements(By.)