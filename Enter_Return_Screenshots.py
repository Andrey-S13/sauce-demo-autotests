import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Импорт Keys, для имитации нажатия клавиши клавиатуры
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Создаем и настраиваем опции
chrome_options = Options()
chrome_options.add_argument("--guest")

# Передаем опции в драйвер
driver = webdriver.Chrome(options=chrome_options)
base_url = "https://www.saucedemo.com/"
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

'''
BACKSPACE - имитация удаления
'''

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input Login")
# time.sleep(1)
# user_name.send_keys(Keys.BACKSPACE * 5)  # остается "standard"
# time.sleep(1)
# print("Remove a part of login")
# user_name.send_keys("_user")
# time.sleep(1)
# print("Return a part of login again")

'''
send_keys() - проверка изменения данных и возвращение их обратно
'''

# password = driver.find_element(By.XPATH, "//input[@id='password']")
# password.send_keys(password_all)
# print("Input Password")
# button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
# button_login.click()
# print("Click Login Password")

'''
ENTER/RETURN - имитация нажатия
'''

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")
password.send_keys(Keys.RETURN)  # Клавиша ввода, имитация нажатия ENTER
time.sleep(1)
filter = driver.find_element(By.XPATH, "//select[@data-test='product-sort-container']")  # Открываем выпадашку
filter.click()
print("Click Filter")
time.sleep(1)

filter.send_keys(Keys.DOWN)
print("Next Filter")
time.sleep(1)
filter.send_keys(Keys.RETURN)
print("Choose new Filter")
time.sleep(1)


'''
Комбинация клавиш
'''

# user_name.send_keys(Keys.CONTROL + 'f')  - имитируем нажатие 'ctrl + f'
# В данном примере мы активируем поиск по странице в браузере


"""
save_screenshot()
Создание скриншотов + уникальное название каждого скриншота

driver.save_screenshot(f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
"""

now_date = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
name_screenshot = "screenshot_" + now_date + ".png"
# driver.save_screenshot("C:\\Users\\User\\PycharmProjects\\python_selenium\\Screenshots\\" + name_screenshot)  # после всего теста появится скриншот с финальной страницей
driver.save_screenshot(f"Screenshots/{name_screenshot}")  # Решение 2