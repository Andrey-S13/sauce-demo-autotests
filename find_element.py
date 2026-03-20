"""
Тесты надо проходить отдельно ! Иначе ошибка "AssertionError
"
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
base_url = "https://www.saucedemo.com/"
driver.get(base_url)
driver.maximize_window()

'''
Негативное тестирование - тест 1 
Проверка неправильного логина
'''

login_standard_user = "standard_use"
password_all = "secret_sauce"


user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input Login")
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Click Login Password")

warring_test = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warring_test = warring_test.text
assert value_warring_test == "Epic sadface: Username and password do not match any user in this service"
print("Good test")

driver.refresh()
time.sleep(1)

#
# '''
# Негативное тестирование - тест 2
# Проверка пустого пароля
# '''
#
# login_standard_user = "standard_user"
# password_all = ""
#
#
# user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
# user_name.send_keys(login_standard_user)
# print("Input Login")
# password = driver.find_element(By.XPATH, "//input[@id='password']")
# password.send_keys(password_all)
# print("Input Password")
# button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
# button_login.click()
# print("Click Login Password")
#
# warring_test_password = driver.find_element(By.XPATH, "//h3[@data-test='error']")
# value_warring_test_password = warring_test_password.text
# assert value_warring_test_password == "Epic sadface: Password is required"
# print("Good test")
