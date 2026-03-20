import time
from selenium import webdriver
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
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Click Login Password")


"""INFO Pruduct #1"""

product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

"""INFO price #1"""

price_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
price_product_1 = price_1.text
print(price_product_1)

"""click product #1"""

select_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("Select product 1")

"""click shopping cart"""

cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart.click()
print("Enter cart")

"""INFO cart Product 1"""

cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")  # по верстке совпало
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("INFO cart Product 1 GOOD ")

cart_cart_price_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_cart_price_product_1 = cart_cart_price_1.text
print(value_cart_price_product_1)
assert price_product_1 == value_cart_price_product_1
print("INFO cart Price 1 GOOD ")

"""click checkout"""

checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print("Click Checkout")

"""Select user INFO"""

first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys("Andrey")
print("Input first_name")

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys("Suv")
print("Input last_name")

postal_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
postal_code.send_keys("1234")
print("Input postal_code")
time.sleep(1)

"""click Continue"""

button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print("click Continue")
time.sleep(1)

"""INFO finish Product 1"""

finish_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")  # по верстке совпало
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print("INFO finish Product 1 GOOD ")

finish_price_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_finish_price_product_1 = finish_price_1.text
print(value_finish_price_product_1)
assert price_product_1 == value_finish_price_product_1  # эту стоимость можно разбить на несколько, если товар в корзине не один
print("INFO finish Price 1 GOOD ")


summary_price = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
value_summary_price = summary_price.text
print(value_summary_price)
time.sleep(1)

item_total = "Item total: " + value_finish_price_product_1
print(item_total)

assert value_summary_price == item_total
print("Total summary price GOOD")

# Input Login
# Input Password
# Click Login Password

# Sauce Labs Backpack
# $29.99
# Select product 1

# Enter cart
# Sauce Labs Backpack
# INFO cart Product 1 GOOD
# $29.99
# INFO cart Price 1 GOOD
# Click Checkout
# Input first_name
# Input last_name
# Input postal_code
# click Continue
# Sauce Labs Backpack
# INFO finish Product 1 GOOD
# $29.99
# INFO finish Price 1 GOOD
# Item total: $29.99
# Item total: $29.99
# Total summary price GOOD

"""
1.Авторизоваться в системе
2.В каталоге продукта выбрать требуемый товар
3.Перейти в корзину с товаром и подтвердить заказ
4.Внести данные по покупателю
5.Подтвердить заказ
6.Получение подтверждения что заказ взят в работу 
"""

'''
assert value_text_products == 'Products'
print('Заголовок корректен')   или print('Авторизация прошла успешно')

Локатор по совпадению текста
//div[contains(text(), 'Text 123')]

Если один локатор для цены. но по индексу можно найти другие поля с ценами
(//div[@class='inventory_item_price'])[1]
(//div[@class='inventory_item_price'])[2]
(//div[@class='inventory_item_price'])[3]

(//button[contains(text(), 'Add to cart')])[1] - совмещение поиска по названию кнопки и затем по индексу


Проверка в более сложном варианте (DNS магазин с фильтрами)

value_price = price.text
assert 10001 <= value_price <= 18000
print("фильтр отработал корректно")

assert название_товара_каталог == название_товара_корзина
assert цена_товара_каталог == цена_товара_корзина

assert название_товара_финал == название_товара_корзина
assert цена_товара_финал == цена_товара_корзина

assert цена_товара_всего == "Item total: " + цена_товара_финал
'''