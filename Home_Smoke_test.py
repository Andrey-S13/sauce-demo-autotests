import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

''' Settings '''

chrome_options = Options()
chrome_options.add_argument("--guest")  # Скрыть всплывающее уведомление о смене пароля
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
url_base = "https://www.saucedemo.com/"
driver.get(url_base)
# driver.maximize_window()  # Отображение на весь экран
# chrome_options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна

''' Authorization '''

login = "standard_user"
password = "secret_sauce"

user_name = driver.find_element(By.CLASS_NAME, "input_error.form_input")  # дан 1 class на креды
user_name.send_keys(login)
time.sleep(1)
print("1. Login: " + login)

user_password = driver.find_element(By.CSS_SELECTOR, "[data-test='password']")
user_password.send_keys(password)
time.sleep(1)
print("2. Password: " + password)

button_Login = driver.find_element(By.ID, "login-button")
button_Login.click()
time.sleep(1)
print("3. Click button_Login - OK")

url_inventory = "https://www.saucedemo.com/inventory.html"
get_url = driver.current_url
print("4. Current url is: " + get_url)
assert url_inventory == get_url
print("5. Current url_inventory - OK")

''' Inventory purchase #1 '''

inventory_purchase_one = driver.find_element(By.ID, "item_4_title_link")
value_inventory_purchase_one = inventory_purchase_one.text
print("6. " + value_inventory_purchase_one)

""" 
(//div[@class="inventory_item_price"])[4] - для поиска цены через порядковый номер
"""
price_inventory_purchase_one = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_inventory_purchase_one = price_inventory_purchase_one.text
print("7. " + value_price_inventory_purchase_one)

select_purchase_one = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
select_purchase_one.click()
time.sleep(1)

current_button_purchase_one = driver.find_element(By.XPATH, "//button[@data-test='remove-sauce-labs-backpack']")
current_button_purchase_one_name = current_button_purchase_one.text
assert current_button_purchase_one_name == "Remove"  # Проверка по изменению кнопки "Add" > "Remove"
print(f"8. '{value_inventory_purchase_one}' was added in a cart")

''' Inventory purchase #2 '''

inventory_purchase_two = driver.find_element(By.ID, "item_0_title_link")
value_inventory_purchase_two = inventory_purchase_two.text
print("9. " + value_inventory_purchase_two)

price_inventory_purchase_two = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
value_price_inventory_purchase_two = price_inventory_purchase_two.text
print("10. " + value_price_inventory_purchase_two)

select_purchase_two = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
select_purchase_two.click()
time.sleep(1)

inventories_cart = driver.find_element(By.XPATH, "//span[@data-test='shopping-cart-badge']")
current_inventories_cart = inventories_cart.text
assert current_inventories_cart == "2"  # Проверка по количеству товара в иконке корзины = 2 товара
print(f"11. added '{current_inventories_cart}' inventories in a cart")

''' Cart '''

cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_button.click()
# time.sleep(1)
print("12. Cart - OK")

''' Check inventory in a cart '''

cart_inventory_one = driver.find_element(By.ID, "item_4_title_link")
name_cart_inventory_one = cart_inventory_one.text
assert name_cart_inventory_one == value_inventory_purchase_one
print("13. The name of 'inventory_one' is the same")

price_cart_inventory_one = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_cart_inventory_one = price_cart_inventory_one.text
assert value_price_cart_inventory_one == value_price_inventory_purchase_one
print("14. The price of 'inventory_one' is the same $29.99")

cart_inventory_two = driver.find_element(By.ID, "item_0_title_link")
name_cart_inventory_two = cart_inventory_two.text
assert name_cart_inventory_two == value_inventory_purchase_two
print("15. The name of 'inventory_two' is the same")

price_cart_inventory_two = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_price_cart_inventory_two = price_cart_inventory_two.text
assert value_price_cart_inventory_two == value_price_inventory_purchase_two
print("16. The price of 'inventory_two' is the same $9.99")

''' Checkout '''

Checkout_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn_action.btn_medium.checkout_button")
Checkout_button.click()
time.sleep(1)
print("17. Checkout - OK")

url_information_page = "https://www.saucedemo.com/checkout-step-one.html"
current_url_after_checkout = driver.current_url
assert current_url_after_checkout == url_information_page
print("18. Information page - OK")

''' Information page '''

first_name = driver.find_element(By.ID, "first-name")
first_name.send_keys("Andrey")
last_name = driver.find_element(By.ID, "last-name")
last_name.send_keys("Suvorov")
Postal_code = driver.find_element(By.ID, "postal-code")
Postal_code.send_keys("123456")
time.sleep(1)
print("19. Information added")

''' Continue '''

Continue_button = driver.find_element(By.ID, "continue")
Continue_button.click()
time.sleep(1)
print("20. Continue - OK")

url_overview_page = "https://www.saucedemo.com/checkout-step-two.html"
current_url_after_continue = driver.current_url
assert current_url_after_continue == url_overview_page
print("21. Overview page - OK")

''' Overview '''

# Сравниваем по товарам на витрине
overview_inventory_one = driver.find_element(By.ID, "item_4_title_link")
name_overview_inventory_one = overview_inventory_one.text
assert name_overview_inventory_one == value_inventory_purchase_one
print("22. The name of 'inventory_one' is the same")

price_overview_inventory_one = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_overview_inventory_one = price_overview_inventory_one.text
assert value_price_overview_inventory_one == value_price_inventory_purchase_one
print("23. The price of 'inventory_one' is the same $29.99")

# Сравниваем по товарам в корзине
overview_inventory_two = driver.find_element(By.ID, "item_0_title_link")
name_overview_inventory_two = overview_inventory_two.text
assert name_overview_inventory_two == name_cart_inventory_two
print("24. The name of 'inventory_one' is the same")

price_overview_inventory_one = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_price_overview_inventory_two = price_overview_inventory_one.text
assert value_price_overview_inventory_two == value_price_cart_inventory_two
print("25. The price of 'inventory_one' is the same $9.99")

''' Price Total '''

value_price_overview_inventory_one_int = value_price_overview_inventory_one.replace('$', '')  # 29.99
# print(value_price_overview_inventory_one_int)
value_price_overview_inventory_two_int = value_price_overview_inventory_two.replace('$', '')  # 9.99
# print(value_price_overview_inventory_two_int)
value_price_overview_all_inventories = float(value_price_overview_inventory_one_int) + float(value_price_overview_inventory_two_int)
print("26. The price of all inventories is " + str(value_price_overview_all_inventories))  # 39.98

item_total = driver.find_element(By.CLASS_NAME, "summary_subtotal_label")
value_item_total = item_total.text
value_item_total_float = value_item_total.replace('Item total: $', '')

assert float(value_price_overview_all_inventories) == float(value_item_total_float)
print("27. Item total: " + str(value_item_total_float) + "- OK")  # 39.98

''' Finish '''

finish_button = driver.find_element(By.ID, "finish")
finish_button.click()
print("28. finish - OK")

complete_message = driver.find_element(By.XPATH, "//h2[text()='Thank you for your order!']")
current_massage = complete_message.text
assert current_massage == "Thank you for your order!"
time.sleep(1)
print("29. Complete_message - OK")

''' Back Home '''

back_home_button = driver.find_element(By.ID, "back-to-products")
back_home_button.click()
page_url = "https://www.saucedemo.com/inventory.html"
current_page_url = get_url
assert page_url == current_page_url
time.sleep(1)
print("30. Home page - OK")
