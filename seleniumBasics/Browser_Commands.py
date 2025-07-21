import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://demo.automationtesting.in/Register.html"

driver  = webdriver.Chrome()
driver.get(URL)
driver.implicitly_wait(5)
pageTitle = driver.title
print(pageTitle)
driver.maximize_window()
time.sleep(3)
driver.refresh()
time.sleep(5)
ele_text = driver.find_element(By.XPATH, "//div/h1[contains(text()='Automation Demo Site ']").text
print(ele_text)
driver.quit()

#C:\Users\P N Babu\PycharmProjects\Project2025

