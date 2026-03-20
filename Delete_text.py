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
login_user = "34532465"
password_all = "secret_sauce"


user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input Login")
time.sleep(1)
# password = driver.find_element(By.XPATH, "//input[@id='password']")
# password.send_keys(password_all)
# print("Input Password")
# button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
# button_login.click()
# print("Click Login Password")

'''
Clear() 
'''

# Способ 1
# user_name.clear()
# time.sleep(1)

# Способ 2
user_name.send_keys(Keys.CONTROL + 'a')  # Выделить все
time.sleep(1)
user_name.send_keys(Keys.DELETE)  # Очистить (справа от курсора, если без "выделить все")

time.sleep(1)
