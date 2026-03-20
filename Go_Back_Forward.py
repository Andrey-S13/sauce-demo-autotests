import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--guest")
driver = webdriver.Chrome(options=chrome_options)
base_url = "https://www.saucedemo.com/"
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"


user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input Login")
time.sleep(1)
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Click Login Password")

# Нажимаем на меню-бургер
menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
menu.click()
time.sleep(1)
print("Click burger-menu")

# Нажимаем на пункт в меню
link_about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
link_about.click()
time.sleep(1)
print("Click link_about")

# Переход вперед / назад в браузере

driver.back()
print("Go back")
time.sleep(1)
driver.forward()
print("Go forward")
time.sleep(1)test_1.py