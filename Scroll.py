import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Создаем и настраиваем опции
chrome_options = Options()
chrome_options.add_argument("--guest")
# Передаем опции в драйвер
driver = webdriver.Chrome(options=chrome_options) # Инициализируем браузер

base_url = "https://www.saucedemo.com/"
driver.get(base_url)
# driver.maximize_window()

login_standard_user = "standard_user"
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

'''
СКРОЛИНГ 

Изменяется в пикселях по двум осям перемещения мыши
"window.scrillTo(X, Y)"

1) Нужно, елси не виден какой-то элемент (в футере, к примеру). 
2) Делать скриншоты в нужном месте на странице
'''

# driver.execute_script('window.scrollTo(0, 150)')
# time.sleep(2)
# print("The page was scrolled")

# now_date = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
# name_screenshot = "screenshot_" + now_date + ".png"
# driver.save_screenshot(f"Screenshots/{name_screenshot}")

'''
Если нам надо навестись на элемент на странице, но мы не знаем, сколько нужно скролить
'''

'''
move_to_element
Перемещение курсора мыши над указанным элементом на странице
'''
# 1 Создали переменную и задаем, каким драйвером хотим управлять / браузером
action = ActionChains(driver)
# 2 Создали переменную, в которой будем хранить локатор данного элемента
Red_T_short = driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
# 3 Указать, что мы хотим делать: через переменную action куда именно хотим навестись и задали локатор
action.move_to_element(Red_T_short).perform()
time.sleep(3)

now_date = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
name_screenshot = "screenshot_" + now_date + ".png"
driver.save_screenshot(f"Screenshots/{name_screenshot}")


'''
2 проверки можно делать:
 - парсить надписи с экрана
 - проверка со скриншотами (через скролинг на определенное число пикселей или наведение через локатор)
'''