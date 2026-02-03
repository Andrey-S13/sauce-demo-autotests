import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

''' Settings '''

chrome_options = Options()
chrome_options.add_argument("--guest")  # Скрыть всплывающее уведомление о смене пароля
driver = webdriver.Chrome(options=chrome_options)
url_base = "https://www.saucedemo.com/"
driver.get(url_base)
# driver.maximize_window()  # Отображение на весь экран

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




# ____________________________________________________________________
# ____________________________________________________________________
# ____________________________________________________________________
# ____________________________________________________________________


"""Для 3 задания"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class SauceDemoTestFramework:
    """Фреймворк для тестирования интернет-магазина Sauce Demo"""

    def __init__(self):
        """Инициализация драйвера и словарей товаров"""
        self.driver = None

        # Полный словарь товаров с ID локаторов
        self.products = {
            1: {
                "name": "Sauce Labs Backpack",
                "add_button_id": "add-to-cart-sauce-labs-backpack",
                "remove_button_test": "remove-sauce-labs-backpack",
                "title_link_id": "item_4_title_link",
                "price": "$29.99"
            },
            2: {
                "name": "Sauce Labs Bike Light",
                "add_button_id": "add-to-cart-sauce-labs-bike-light",
                "remove_button_test": "remove-sauce-labs-bike-light",
                "title_link_id": "item_0_title_link",
                "price": "$9.99"
            },
            3: {
                "name": "Sauce Labs Bolt T-Shirt",
                "add_button_id": "add-to-cart-sauce-labs-bolt-t-shirt",
                "remove_button_test": "remove-sauce-labs-bolt-t-shirt",
                "title_link_id": "item_1_title_link",
                "price": "$15.99"
            },
            4: {
                "name": "Sauce Labs Fleece Jacket",
                "add_button_id": "add-to-cart-sauce-labs-fleece-jacket",
                "remove_button_test": "remove-sauce-labs-fleece-jacket",
                "title_link_id": "item_5_title_link",
                "price": "$49.99"
            },
            5: {
                "name": "Sauce Labs Onesie",
                "add_button_id": "add-to-cart-sauce-labs-onesie",
                "remove_button_test": "remove-sauce-labs-onesie",
                "title_link_id": "item_2_title_link",
                "price": "$7.99"
            },
            6: {
                "name": "Test.allTheThings() T-Shirt (Red)",
                "add_button_id": "add-to-cart-test.allthethings()-t-shirt-(red)",
                "remove_button_test": "remove-test.allthethings()-t-shirt-(red)",
                "title_link_id": "item_3_title_link",
                "price": "$15.99"
            }
        }

    def setup_browser(self):
        """Настройка браузера"""
        chrome_options = Options()
        chrome_options.add_argument("--guest")
        self.driver = webdriver.Chrome(options=chrome_options)
        return self.driver

    def select_product_interactively(self):
        """Интерактивный выбор товара пользователем"""
        print("=" * 60)
        print("ДОБРО ПОЖАЛОВАТЬ В ИНТЕРНЕТ-МАГАЗИН SAUCE DEMO")
        print("=" * 60)
        print("\nДоступные товары:")

        for key, product_info in self.products.items():
            print(f"{key} - {product_info['name']} ({product_info['price']})")

        print("-" * 60)

        while True:
            try:
                choice = input("Введите номер товара (1-6): ").strip()
                key = int(choice)

                if key in self.products:
                    selected_product = self.products[key]
                    print(f"\n✓ Выбран товар: {selected_product['name']}")
                    return selected_product
                else:
                    print("❌ Неверный номер. Пожалуйста, введите число от 1 до 6.")

            except ValueError:
                print("❌ Ошибка: пожалуйста, введите число.")

    def login(self, username="standard_user", password="secret_sauce"):
        """Авторизация пользователя"""
        print("\n" + "=" * 60)
        print("ШАГ 1: АВТОРИЗАЦИЯ")
        print("=" * 60)

        url = "https://www.saucedemo.com/"
        self.driver.get(url)

        # Ввод логина
        user_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        user_name.send_keys(username)
        print(f"✓ Введен логин: {username}")

        # Ввод пароля
        user_password = self.driver.find_element(By.ID, "password")
        user_password.send_keys(password)
        print(f"✓ Введен пароль: {'*' * len(password)}")

        # Клик по кнопке входа
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        print("✓ Кнопка входа нажата")

        # Проверка успешной авторизации
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://www.saucedemo.com/inventory.html")
        )
        print("✓ Успешная авторизация, переход на страницу товаров")

        return True

    def add_product_to_cart(self, product_info):
        """Добавление выбранного товара в корзину"""
        print("\n" + "=" * 60)
        print(f"ШАГ 2: ДОБАВЛЕНИЕ ТОВАРА В КОРЗИНУ")
        print("=" * 60)

        try:
            # Добавление товара в корзину
            add_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, product_info["add_button_id"]))
            )
            add_button.click()
            print(f"✓ Товар '{product_info['name']}' добавлен в корзину")

            # Проверка изменения кнопки на "Remove"
            remove_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, f"[data-test='{product_info['remove_button_test']}']")
                )
            )
            assert remove_button.text == "Remove"
            print("✓ Кнопка изменилась на 'Remove'")

            # Проверка счетчика корзины
            cart_badge = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
            )
            assert cart_badge.text == "1"
            print("✓ Счетчик корзины показывает 1 товар")

            return True

        except Exception as e:
            print(f"❌ Ошибка при добавлении товара: {e}")
            return False

    def verify_product_in_cart(self, product_info):
        """Проверка товара в корзине"""
        print("\n" + "=" * 60)
        print("ШАГ 3: ПРОВЕРКА КОРЗИНЫ")
        print("=" * 60)

        try:
            # Переход в корзину
            cart_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
            )
            cart_link.click()
            print("✓ Переход в корзину выполнен")

            # Проверка URL корзины
            WebDriverWait(self.driver, 10).until(
                EC.url_to_be("https://www.saucedemo.com/cart.html")
            )

            # Проверка названия товара
            cart_product_name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, product_info["title_link_id"]))
            )
            assert cart_product_name.text == product_info["name"]
            print(f"✓ Название товара в корзине корректно: {product_info['name']}")

            # Проверка цены товара
            # Находим контейнер товара и затем цену внутри него
            product_container = cart_product_name.find_element(
                By.XPATH, "./ancestor::div[@class='cart_item']"
            )
            cart_product_price = product_container.find_element(
                By.CLASS_NAME, "inventory_item_price"
            )
            assert cart_product_price.text == product_info["price"]
            print(f"✓ Цена товара в корзине корректна: {product_info['price']}")

            return True

        except Exception as e:
            print(f"❌ Ошибка при проверке корзины: {e}")
            return False

    def checkout_process(self, product_info):
        """Процесс оформления заказа"""
        print("\n" + "=" * 60)
        print("ШАГ 4: ОФОРМЛЕНИЕ ЗАКАЗА")
        print("=" * 60)

        try:
            # Начало оформления
            checkout_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "checkout"))
            )
            checkout_button.click()
            print("✓ Начало оформления заказа")

            # Заполнение информации
            self.driver.find_element(By.ID, "first-name").send_keys("Тест")
            self.driver.find_element(By.ID, "last-name").send_keys("Пользователь")
            self.driver.find_element(By.ID, "postal-code").send_keys("123456")
            print("✓ Информация для доставки заполнена")

            # Продолжение
            continue_button = self.driver.find_element(By.ID, "continue")
            continue_button.click()
            print("✓ Переход к обзору заказа")

            # Проверка на странице обзора
            WebDriverWait(self.driver, 10).until(
                EC.url_to_be("https://www.saucedemo.com/checkout-step-two.html")
            )

            # Проверка товара в обзоре
            overview_product = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, product_info["title_link_id"]))
            )
            assert overview_product.text == product_info["name"]
            print(f"✓ Товар в обзоре заказа: {product_info['name']}")

            # Проверка цены
            overview_container = overview_product.find_element(
                By.XPATH, "./ancestor::div[@class='cart_item']"
            )
            overview_price = overview_container.find_element(
                By.CLASS_NAME, "inventory_item_price"
            )
            assert overview_price.text == product_info["price"]

            # Проверка итоговой суммы
            item_total = self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label")
            expected_total = f"Item total: {product_info['price']}"
            assert item_total.text == expected_total
            print(f"✓ Итоговая сумма корректна: {product_info['price']}")

            # Завершение заказа
            finish_button = self.driver.find_element(By.ID, "finish")
            finish_button.click()
            print("✓ Завершение заказа")

            # Проверка успешного завершения
            complete_header = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
            )
            assert complete_header.text == "Thank you for your order!"
            print("✓ Заказ успешно оформлен!")

            return True

        except Exception as e:
            print(f"❌ Ошибка при оформлении заказа: {e}")
            return False

    def run_test(self):
        """Запуск полного тестового сценария"""
        try:
            # 1. Выбор товара
            selected_product = self.select_product_interactively()

            # 2. Настройка браузера
            self.setup_browser()

            # 3. Авторизация
            if not self.login():
                print("❌ Тест провален на этапе авторизации")
                return False

            # 4. Добавление товара в корзину
            if not self.add_product_to_cart(selected_product):
                print("❌ Тест провален на этапе добавления в корзину")
                return False

            # 5. Проверка корзины
            if not self.verify_product_in_cart(selected_product):
                print("❌ Тест провален на этапе проверки корзины")
                return False

            # 6. Оформление заказа
            if not self.checkout_process(selected_product):
                print("❌ Тест провален на этапе оформления заказа")
                return False

            print("\n" + "=" * 60)
            print("🎉 ТЕСТ УСПЕШНО ЗАВЕРШЕН! 🎉")
            print("=" * 60)
            print(f"Товар '{selected_product['name']}' успешно добавлен и оплачен.")

            # Пауза для просмотра результата
            time.sleep(3)

            return True

        except Exception as e:
            print(f"\n❌ КРИТИЧЕСКАЯ ОШИБКА: {e}")
            return False

        finally:
            if self.driver:
                self.driver.quit()
                print("\n✓ Браузер закрыт")


# Запуск теста
if __name__ == "__main__":
    print("🚀 Запуск автоматизированного тестирования Sauce Demo")
    print("=" * 60)

    test_framework = SauceDemoTestFramework()
    test_framework.run_test()