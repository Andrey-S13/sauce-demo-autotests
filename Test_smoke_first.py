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

# # Нажимаем на пункт в меню
# link_about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
# link_about.click()
# time.sleep(1)
# print("Click link_about")

# Проверка соответствия урла (проверка 1)
'''
Пропущен блок - долгое ожидание. Найти причину (!)

# url_page_about = "https://saucelabs.com/"
# expected_url = driver.current_url
# assert url_page_about == expected_url
# time.sleep(1)
# print("Correct page")
'''
# driver.quit()
# print("\n✓ Браузер закрыт")

# Провекра соответствия проверочного слова (проверка 2)

# check_text_page_about = driver.find_element(By.XPATH, "//h1[@class='MuiTypography-root.MuiTypography-h1.css-152qxt']")
# current_text_page_about = check_text_page_about.text
# assert current_text_page_about == "Build apps users love with AI-driven quality"
# print("Correct page")

# driver.refresh()

# Переход на страницу назад

driver.back()
time.sleep(1)
print("Last page")


# Выход из аккаунта
menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
menu.click()
time.sleep(1)
print("Click burger-menu")
logout = driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']")
logout.click()
time.sleep(1)
print("Successful logout")

# Проверка через парсинг - страница авторизации

current_website_text = driver.find_element(By.XPATH, "//div[@class='login_logo']")
name_website_text = current_website_text.text
assert name_website_text == "Swag Labs"
print("Correct page")

# Подтверждение скриншотом

