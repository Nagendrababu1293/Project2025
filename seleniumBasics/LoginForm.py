from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.NAME, 'username'))).send_keys("tomsmith")
wait.until(EC.presence_of_element_located((By.ID, 'password'))).send_keys("SuperSecretPassword!")
wait.until(EC.element_to_be_clickable((By.XPATH, '//i[@class="fa fa-2x fa-sign-in"]'))).click()

message = wait.until(EC.presence_of_element_located((By.XPATH, '//h4[@class="subheader"]'))).text

if "Welcome to the Secure Area. When you are done click logout below." in message:
    print("Login successfull")
else:
    print("Login failed")
driver.quit()
