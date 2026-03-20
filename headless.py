"""
Headless режим - это режим, в котором браузер запускается в фоновом режиме без отображения на экране.
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # браузер не закроется автоматически
options.add_argument("--headless")  # без открытия браузера
q = Service()
driver = webdriver.Chrome(options=options, service=q)
base_url = "https://www.saucedemo.com/"
driver.get(base_url)
driver.maximize_window()
time.sleep(3)

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input Login")

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")

click_button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
click_button_login.click()
print("Click Login Password")

header = driver.find_element(By.XPATH, "//span[@class='title']")
print(header.text)