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









    # ++++++++++++++++++++++++++++++++
    # ________________________________

    # ++++++++++++++++++++++++++++++++
    # ________________________________
    #     # ++++++++++++++++++++++++++++++++
    #     # ________________________________
    #     # ++++++++++++++++++++++++++++++++
    #     # ________________________________
    #     # ++++++++++++++++++++++++++++++++
    #     # ________________________________
    #     # ++++++++++++++++++++++++++++++++
    #     # ________________________________
    #     # ++++++++++++++++++++++++++++++++
    #     # ________________________________

    # ++++++++++++++++++++++++++++++++
    # ________________________________
    #     # ++++++++++++++++++++++++++++++++
    #     # ________________________________
    #     # ++++++++++++++++++++++++++++++++
    #     # ________________________________
    #     # ++++++++++++++++++++++++++++++++
    #     # ________________________________
    #     # ++++++++++++++++++++++++++++++++
    #     # ________________________________
    #     # ++++++++++++++++++++++++++++++++
    #     # ________________________________
    # Импортируем нужные библиотеки
    import time  # для пауз (time.sleep)
    from selenium import webdriver  # основной инструмент для автоматизации браузера
    from selenium.webdriver.common.by import By  # для поиска элементов на странице
    from selenium.webdriver.support.wait import WebDriverWait  # для ожидания элементов
    from selenium.webdriver.support import expected_conditions as EC  # условия ожидания
    from selenium.webdriver.chrome.options import Options  # настройки браузера Chrome


    class SauceDemoTester:
        """
        Главный класс для тестирования сайта Sauce Demo.
        Здесь собраны ВСЕ методы для работы с сайтом.
        """

        # Словари с данными - доступны из ЛЮБОГО метода класса
        # Ключ (число) -> Название товара
        products = {
            1: "Sauce Labs Backpack",
            2: "Sauce Labs Bike Light",
            3: "Sauce Labs Bolt T-Shirt",
            4: "Sauce Labs Fleece Jacket",
            5: "Sauce Labs Onesie",
            6: "Test.allTheThings() T-Shirt (Red)"
        }

        # Ключ (число) -> ID кнопки "Add to cart" (добавить в корзину)
        items_id = {
            1: "add-to-cart-sauce-labs-backpack",
            2: "add-to-cart-sauce-labs-bike-light",
            3: "add-to-cart-sauce-labs-bolt-t-shirt",
            4: "add-to-cart-sauce-labs-fleece-jacket",
            5: "add-to-cart-sauce-labs-onesie",
            6: "add-to-cart-test.allthethings()-t-shirt-(red)"
        }

        # Ключ (число) -> ID кнопки "Remove" (удалить из корзины)
        remove_ids = {
            1: "remove-sauce-labs-backpack",
            2: "remove-sauce-labs-bike-light",
            3: "remove-sauce-labs-bolt-t-shirt",
            4: "remove-sauce-labs-fleece-jacket",
            5: "remove-sauce-labs-onesie",
            6: "remove-test.allthethings()-t-shirt-(red)"
        }

        def __init__(self):
            """
            Конструктор класса. Вызывается ПРИ СОЗДАНИИ объекта.
            Инициализирует пустые переменные.
            """
            self.driver = None  # здесь будет храниться браузер
            self.selected_product_key = None  # здесь будет номер выбранного товара (1-6)
            self.selected_product_name = None  # здесь будет название выбранного товара

        @classmethod
        def select_product(cls):
            """
            Статический метод для выбора товара.
            Вызывается ДО создания объекта класса.

            Работает так:
            1. Показывает список товаров
            2. Просит пользователя ввести номер
            3. Проверяет, что номер правильный
            4. Возвращает номер и название товара
            """
            print("=" * 60)
            print("ПРИВЕТСТВУЮ ТЕБЯ В НАШЕМ ИНТЕРНЕТ-МАГАЗИНЕ!")
            print("=" * 60)

            # Показываем список товаров в красивом формате
            print("\nДОСТУПНЫЕ ТОВАРЫ:")
            print("-" * 40)
            for номер, название in cls.products.items():  # проходим по всем товарам
                print(f"  {номер} - {название}")  # показываем "1 - Sauce Labs Backpack" и т.д.

            print("-" * 40)

            # Бесконечный цикл - будет спрашивать, пока пользователь не введет правильный номер
            while True:
                try:
                    # Просим ввести номер товара
                    ключ = int(input("ВВЕДИТЕ НОМЕР ТОВАРА (от 1 до 6): "))

                    # Проверяем, есть ли такой номер в словаре товаров
                    if ключ in cls.products:
                        название_товара = cls.products[ключ]  # получаем название по номеру
                        print(f"\n✅ ВЫБРАН ТОВАР: {название_товара}")
                        print("=" * 60)
                        return ключ, название_товара  # возвращаем номер и название
                    else:
                        # Если номера нет в списке (например, ввели 7 или 0)
                        print("❌ ТОВАРА С ТАКИМ НОМЕРОМ НЕТ! Попробуйте снова.")

                except ValueError:
                    # Если ввели не число (например, буквы)
                    print("❌ ОШИБКА: нужно ввести ЧИСЛО! Попробуйте снова.")

        def setup_browser(self):
            """
            Настраивает и запускает браузер Chrome.
            """
            print("\n🚀 ЗАПУСКАЮ БРАУЗЕР...")

            # Создаем настройки для Chrome
            chrome_options = Options()
            chrome_options.add_argument('--incognito')  # режим инкогнито
            chrome_options.add_argument('--disable-notifications')  # отключаем уведомления

            # Создаем драйвер (открываем браузер)
            self.driver = webdriver.Chrome(options=chrome_options)

            # Открываем сайт
            self.driver.get("https://www.saucedemo.com/")

            # Настройки ожидания
            self.driver.implicitly_wait(5)  # ждем элементы до 5 секунд
            self.driver.maximize_window()  # разворачиваем на весь экран

            print("✅ БРАУЗЕР ЗАПУЩЕН И НАСТРОЕН")
            return self.driver

        def authorization(self):
            """
            Авторизация на сайте.
            Вводит логин и пароль, нажимает кнопку входа.
            """
            print("\n🔐 ВХОД НА САЙТ...")

            # Данные для входа (фиксированные, как в задании)
            логин = "standard_user"
            пароль = "secret_sauce"

            # ШАГ 1: Находим поле для логина и вводим его
            поле_логина = self.driver.find_element(By.ID, 'user-name')
            поле_логина.send_keys(логин)
            print(f"   Введен логин: {логин}")
            time.sleep(0.5)  # небольшая пауза для наглядности

            # ШАГ 2: Находим поле для пароля и вводим его
            поле_пароля = self.driver.find_element(By.ID, 'password')
            поле_пароля.send_keys(пароль)
            print(f"   Введен пароль: {пароль}")
            time.sleep(0.5)

            # ШАГ 3: Находим кнопку "Login" и нажимаем ее
            кнопка_входа = self.driver.find_element(By.ID, 'login-button')
            кнопка_входа.click()
            print("   Нажата кнопка входа")
            time.sleep(1)  # ждем загрузки страницы

            # ШАГ 4: Проверяем, что мы на правильной странице
            правильный_url = "https://www.saucedemo.com/inventory.html"
            текущий_url = self.driver.current_url

            print(f"   Проверяем URL: {текущий_url}")

            if текущий_url == правильный_url:
                print("✅ АВТОРИЗАЦИЯ УСПЕШНА! Мы на странице с товарами.")
                return True
            else:
                print("❌ ОШИБКА: Не удалось перейти на страницу с товарами")
                return False

        def add_product_to_cart(self):
            """
            Добавляет выбранный товар в корзину.
            """
            print(f"\n🛒 ДОБАВЛЯЮ ТОВАР В КОРЗИНУ...")
            print(f"   Товар: {self.selected_product_name}")

            # Проверяем, что товар был выбран
            if self.selected_product_key is None:
                print("❌ ОШИБКА: товар не выбран!")
                return False

            # Получаем ID кнопки "Add to cart" для нашего товара
            id_товара = self.items_id.get(self.selected_product_key)

            if not id_товара:  # если ID не найден
                print(f"❌ ОШИБКА: не найден ID для товара {self.selected_product_key}")
                return False

            # Находим кнопку "Add to cart" по ID и нажимаем ее
            кнопка_добавить = self.driver.find_element(By.ID, id_товара)
            кнопка_добавить.click()

            print(f"✅ ТОВАР ДОБАВЛЕН В КОРЗИНУ")
            time.sleep(1)  # ждем обновления страницы
            return True

        def check_product_in_cart_ui(self):
            """
            Проверяет, что товар добавился в корзину.
            Делает две проверки прямо на странице с товарами.
            """
            print("\n🔍 ПРОВЕРЯЮ ДОБАВЛЕНИЕ ТОВАРА...")

            # ПРОВЕРКА 1: Появилась ли кнопка "Remove"?
            print("   1. Проверяю кнопку 'Remove'...")

            # Получаем ID кнопки "Remove" для нашего товара
            id_remove = self.remove_ids.get(self.selected_product_key)
            кнопка_remove = self.driver.find_element(By.ID, id_remove)

            # Смотрим текст на кнопке
            текст_на_кнопке = кнопка_remove.text

            if текст_на_кнопке == "Remove":
                print(f"      ✅ Кнопка 'Remove' найдена")
            else:
                print(f"      ❌ Ошибка: на кнопке текст '{текст_на_кнопке}' вместо 'Remove'")
                return False

            # ПРОВЕРКА 2: Появилась ли цифра "1" на иконке корзины?
            print("   2. Проверяю счетчик корзины...")

            # Ищем элемент с цифрой на иконке корзины
            счетчик_корзины = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            цифра_в_корзине = счетчик_корзины.text

            if цифра_в_корзине == "1":
                print(f"      ✅ В корзине 1 товар")
                return True
            else:
                print(f"      ❌ Ошибка: в корзине {цифра_в_корзине} товара(ов) вместо 1")
                return False

        def verify_product_in_cart_page(self):
            """
            Переходит в корзину и проверяет, что там лежит нужный товар.
            """
            print("\n📦 ПЕРЕХОЖУ В КОРЗИНУ ДЛЯ ПРОВЕРКИ...")

            # ШАГ 1: Находим иконку корзины и нажимаем на нее
            иконка_корзины = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
            иконка_корзины.click()
            print("   Перешел в корзину")
            time.sleep(1)

            # ШАГ 2: Проверяем URL страницы корзины
            правильный_url_корзины = "https://www.saucedemo.com/cart.html"
            текущий_url = self.driver.current_url

            if текущий_url == правильный_url_корзины:
                print("   ✅ Мы на правильной странице корзины")
            else:
                print(f"   ❌ Ошибка: неправильный URL корзины")
                return False

            # ШАГ 3: Находим название товара в корзине
            # Ждем появления элемента с названием товара (до 10 секунд)
            имя_товара_в_корзине = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name"))
            )

            # Получаем текст названия товара
            реальное_название = имя_товара_в_корзине.text
            ожидаемое_название = self.selected_product_name

            print(f"   Ожидаемое название: {ожидаемое_название}")
            print(f"   Реальное название:   {реальное_название}")

            # Сравниваем названия
            if реальное_название == ожидаемое_название:
                print("   ✅ Товар в корзине совпадает с выбранным!")
                return True
            else:
                print("   ❌ Ошибка: товар в корзине не совпадает!")
                return False

        def checkout(self):
            """
            Оформляет заказ (проходит все шаги до завершения).
            """
            print("\n💰 ОФОРМЛЯЮ ЗАКАЗ...")

            try:
                # ШАГ 1: Нажимаем кнопку "Checkout" в корзине
                print("   1. Начинаю оформление...")
                кнопка_checkout = self.driver.find_element(By.ID, "checkout")
                кнопка_checkout.click()
                time.sleep(1)

                # ШАГ 2: Заполняем форму с информацией
                print("   2. Заполняю данные...")

                # Имя
                поле_имени = self.driver.find_element(By.ID, "first-name")
                поле_имени.send_keys("Andrey")

                # Фамилия
                поле_фамилии = self.driver.find_element(By.ID, "last-name")
                поле_фамилии.send_keys("Suvorov")

                # Почтовый индекс
                поле_индекса = self.driver.find_element(By.ID, "postal-code")
                поле_индекса.send_keys("123456")

                time.sleep(0.5)
                print("      Данные заполнены")

                # ШАГ 3: Нажимаем "Continue"
                print("   3. Перехожу к оплате...")
                кнопка_continue = self.driver.find_element(By.ID, "continue")
                кнопка_continue.click()
                time.sleep(1)

                # ШАГ 4: Нажимаем "Finish" для завершения
                print("   4. Завершаю заказ...")
                кнопка_finish = self.driver.find_element(By.ID, "finish")
                кнопка_finish.click()
                time.sleep(1)

                # ШАГ 5: Проверяем сообщение об успешном заказе
                print("   5. Проверяю результат...")

                # Ищем сообщение "Thank you for your order!"
                сообщение_успеха = self.driver.find_element(
                    By.XPATH, "//h2[text()='Thank you for your order!']"
                )

                if сообщение_успеха.text == "Thank you for your order!":
                    print("      ✅ ЗАКАЗ УСПЕШНО ОФОРМЛЕН!")
                    return True
                else:
                    print("      ❌ Ошибка при оформлении заказа")
                    return False

            except Exception as e:
                print(f"      ❌ Ошибка: {e}")
                return False

        def run_smoke_test(self, номер_товара, название_товара):
            """
            Запускает ОСНОВНОЙ тест (как в вашем задании):
            1. Выбор товара (уже сделан)
            2. Запуск браузера
            3. Авторизация
            4. Добавление в корзину
            5. Проверка добавления
            """
            print("\n" + "=" * 60)
            print(f"🚀 ЗАПУСК SMOKE-ТЕСТА ДЛЯ ТОВАРА:")
            print(f"   {название_товара}")
            print("=" * 60)

            # Сохраняем выбранный товар в объекте
            self.selected_product_key = номер_товара
            self.selected_product_name = название_товара

            try:
                # ШАГ 1: Настройка браузера
                self.setup_browser()

                # ШАГ 2: Авторизация
                if not self.authorization():
                    print("\n❌ ТЕСТ ПРОВАЛЕН на этапе авторизации")
                    return False

                # ШАГ 3: Добавление товара
                if not self.add_product_to_cart():
                    print("\n❌ ТЕСТ ПРОВАЛЕН на этапе добавления в корзину")
                    return False

                # ШАГ 4: Проверка добавления
                if not self.check_product_in_cart_ui():
                    print("\n❌ ТЕСТ ПРОВАЛЕН на этапе проверки корзины")
                    return False

                # Если все шаги прошли успешно
                print("\n" + "=" * 60)
                print("🎉 SMOKE-ТЕСТ УСПЕШНО ПРОЙДЕН!")
                print("=" * 60)
                return True

            except Exception as e:
                # Если произошла какая-то ошибка
                print(f"\n❌ КРИТИЧЕСКАЯ ОШИБКА: {e}")
                return False

            finally:
                # Этот блок выполнится ВСЕГДА, даже если была ошибка
                if self.driver:
                    print("\n🛑 ЗАКРЫВАЮ БРАУЗЕР...")
                    self.driver.quit()
                    print("Браузер закрыт")


    # ============================================================================
    # ОСНОВНАЯ ПРОГРАММА - начинает выполнение отсюда
    # ============================================================================

    if __name__ == "__main__":
        """
        Этот блок выполняется ТОЛЬКО когда запускают этот файл напрямую.
        """

        print("\n" + "=" * 60)
        print("🤖 АВТОМАТИЗИРОВАННЫЙ ТЕСТЕР SAUCE DEMO")
        print("=" * 60)

        # ШАГ 1: Выбираем товар (работает САМ ПО СЕБЕ, без браузера)
        # Это статический метод, он вызывается у КЛАССА, а не у объекта
        номер_товара, название_товара = SauceDemoTester.select_product()

        # ШАГ 2: Создаем объект тестера
        # Теперь создаем реальный объект, который будет работать с браузером
        тестер = SauceDemoTester()

        # ШАГ 3: Запускаем тест
        # Передаем в тест выбранный номер и название товара
        успех = тестер.run_smoke_test(номер_товара, название_товара)

        # ШАГ 4: Показываем итоговый результат
        if успех:
            print("\n" + "🎊" * 30)
            print("ВСЕ ЗАДАНИЯ ВЫПОЛНЕНЫ УСПЕШНО!")
            print("🎊" * 30)
        else:
            print("\n" + "💥" * 30)
            print("ТЕСТ ЗАВЕРШЕН С ОШИБКАМИ!")
            print("💥" * 30)