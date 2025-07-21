from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.qafox.com/selenium/selenium-practice/")
driver.maximize_window()




action = ActionChains(driver)