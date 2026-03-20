import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

"""Сайт https://www.saucedemo.com/"""

# chrome_options = Options()
# chrome_options.add_argument("--guest")
# driver = webdriver.Chrome(options=chrome_options)
# url_slider = "https://www.saucedemo.com/"
# driver.get(url_slider)
# driver.maximize_window()

''' Authorization '''

# login = "standard_user"
# password = "secret_sauce"
#
# user_name = driver.find_element(By.CLASS_NAME, "input_error.form_input")  # дан 1 class на креды
# user_name.send_keys(login)
# time.sleep(1)
# print("1. Login: " + login)
#
# user_password = driver.find_element(By.CSS_SELECTOR, "[data-test='password']")
# user_password.send_keys(password)
# time.sleep(1)
# print("2. Password: " + password)
#
# button_Login = driver.find_element(By.ID, "login-button")
# button_Login.click()
# print("3. Click button_Login - OK")
# time.sleep(3)
#
# dropdown_select = Select(driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))
'''
Вариант 1 - по видимой части (по названию значений из выпадающего списка)
'''
# dropdown_select.select_by_visible_text('Price (low to high)')
# time.sleep(2)


'''
Вариант 2 - выбор value значения в html разметке
'''
# dropdown_select.select_by_value('za')
# time.sleep(2)


'''
Сайт https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo  

Случай, когда нет удобного тега select
'''

chrome_options = Options()
chrome_options.add_argument("--guest")
driver = webdriver.Chrome(options=chrome_options)
url_select = "https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo"
driver.get(url_select)
driver.maximize_window()

dropdown_select = driver.find_element(By.XPATH, "//span[@aria-labelledby='select2-country-container']")  # //span[@class='select2-selection select2-selection--single']
dropdown_select.click()
time.sleep(4)

# click_country = driver.find_element(By.XPATH, "(//li[@class='select2-results__option'])[5]")
# click_country.click()
# time.sleep(2)

''' выбрать через ввод текста с нажатием Enter '''

input_country = driver.find_element(By.XPATH, "(//input[@class='select2-search__field'])[2]")
input_country.send_keys('India')
time.sleep(2)
input_country.send_keys(Keys.RETURN)
time.sleep(2)