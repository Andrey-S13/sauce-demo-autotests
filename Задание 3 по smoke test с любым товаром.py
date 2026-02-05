import time
from selenium import webdriver  # инструмент для автоматизации браузера
from selenium.webdriver.common.by import By  # поиск элементов на странице
from selenium.webdriver.common import keys  # инструменты взаимодействия с элементами на странице
from selenium.webdriver.support.wait import WebDriverWait  # явное ожидание элементов
from selenium.webdriver.support import expected_conditions as EC  # условное ожидание элементов
from selenium.webdriver.chrome.options import Options  # настройки браузера Chrome


# def product_search():
#     """Поиск товара по введенному ключу"""
#
#     print("Приветствую тебя в нашем интернет - магазине")
#
#     # создаем новый список для перечисления в print
#     item_list = []
#     for key, value in products.items():
#         item_list.append(f"{key} - {value}")
#
#     print(f"Выбери один из следующих товаров и укажи его номер: {', '.join(item_list)}")
#
#     try:
#         key = int(input())
#
#         if key in products:
#             print(f"Выбран товар: {products[key]} ")
#             print("-" * 20)  # разделитель текста (здесь и далее)
#         else:
#             print("Товар не выбран или не найден")
#             print("-" * 20)
#
#     except ValueError:
#         print("Ошибка: введите число!")
#         print("-" * 20)



class SauceDemoSmokeTest:
    """Класс для Smoke теста по покупке товара в интернет магазине Sauce Demo"""

    # Словарь для поиска товара по введенному ключу
    products = {
        1: "Sauce Labs Backpack",
        2: "Sauce Labs Bike Light",
        3: "Sauce Labs Bolt T-Shirt",
        4: "Sauce Labs Fleece Jacket",
        5: "Sauce Labs Onesie",
        6: "Test.allTheThings() T-Shirt (Red)"
    }

"""
Добавить методы для преобразования словаря в lowercase + "-" + фразы

add-to-cart-sauce-labs-backpack - значение ID для добавления в корзину
remove-sauce-labs-backpack -  # значение ID для добавления в корзину
"""



    def __init__(self):
        """
        Конструктор класса. Вызывается при СОЗДАНИИ объекта
        Инициализирует пустые переменные.
        """
        self.driver = None  # хранение браузера
        self.selected_product_key = None  # хранение выбранного товара (1-6)
        self.selected_product_name = None  # хранение выбранного товара (имя)





    # ++++++++++++++++++++++++++++++++
    # ________________________________

    # ++++++++++++++++++++++++++++++++
    # ________________________________


    def setup_browser(self):
        """Настройка браузера"""
        chrome_options = Options()
        chrome_options.add_argument('--incognito')  # нет всплывающих окон "пароля" / "перевода стр"
        self.driver = webdriver.Chrome(options=chrome_options)
        url_authorisation = "https://www.saucedemo.com/"
        self.driver.get(url_authorisation)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        return self.driver

    def authorization(self):
        """Авторизация пользователя"""
        # Креды пользователя
        login = "standard_user"
        password = "secret_sauce"

        # Ввод логина
        user_name = self.driver.find_element(By.ID, 'user-name')
        user_name.send_keys(login)
        print("Логин: " + login)

        # Ввод пароля
        user_password = self.driver.find_element(By.ID, 'password')
        user_password.send_keys(password)
        print("Пароль: " + password)

        # Нажатие на кнопку "логин" (вход)
        button_login = self.driver.find_element(By.ID, 'login-button')
        button_login.click()
        print("Попытка авторизоваться")
        print("-" * 20)  # разделитель текста
        time.sleep(2)

        # Проверка перехода на страницу с товарами
        url_inventory = "https://www.saucedemo.com/inventory.html"
        get_url = self.driver.current_url
        print("Current url: " + get_url)
        assert get_url == url_inventory
        print("Авторизованы >>> переход на страницу с товарами")

        return self
#
# '''Выбор товара'''
#
# # словарь для подстановки ID в XPATH
# items_id = {
#     1: "add-to-cart-sauce-labs-backpack",
#     2: "add-to-cart-sauce-labs-bike-light",
#     3: "add-to-cart-sauce-labs-bolt-t-shirt",
#     4: "add-to-cart-sauce-labs-fleece-jacket",
#     5: "add-to-cart-sauce-labs-onesie",
#     6: "add-to-cart-test.allthethings()-t-shirt-(red)"
# }
#
# # Поиск ID в локатор XPATH по выбранному ранее товару
# product_key = int(product)  # дубль переменной с выбранным ранее товаром
# if product_key in items_id:
#     ID = items_id[product_key]
#     print(f"Выбран товар: {products.get(product_key)}")
#     print(f"ID XPATH: {ID}")
#     print("-" * 20)
#
# # Добавление товара в корзину
# button_add_item = driver.find_element(By.XPATH, f"//button[@id='{ID}']")
# button_add_item.click()
# print(f"Добавлено в корзину: {ID}")
# print("-" * 20)  # разделитель текста
# time.sleep(2)
#
#
# class ContinueSmokeTestPurchaseItem:
#     """Создание класса для повторяющихся механик после добавления товара в корзину"""
#
#     def __init__(self, driver, product_key, products, items_id):  # Осознанный костыль по использованию словарей вне Класса!!!
#         self.driver = driver  # возможность поиска элементов на странице
#         self.product_key = product_key
#         self.products = products
#         self.items_id = items_id
#
#     def get_product_name_in_cart_format(self):
#         """Получить имя товара в формате, используемом в корзине"""
#         # Получаем название товара из словаря
#         product_name = self.items_id[self.product_key]
#         # Преобразуем в формат, используемый в ID (для возможного использования)
#         formatted_name = product_name.replace("add-to-cart-", "").replace("s"[0], "S").replace("-", "")
#         return formatted_name
#
#
#     # def check_product_in_cart(self):
#     #     """Проверка добавления нужного товара в корзину"""
#     #     try:
#     #         # Первая проверка - кнопка Remove
#     #         ID_button_remove = self.get_remove_id()
#     #         print(f"ID: {ID_button_remove}")
#     #
#     #         # Локатор кнопки Remove
#     #         remove_button = WebDriverWait(self.driver, 10).until(
#     #             EC.visibility_of_element_located(By.XPATH, f"//button[@id='{ID_button_remove}']")
#     #         )
#     #
#     #         # Проверяем текст кнопки
#     #         actual_text = remove_button.text
#     #         assert actual_text == "Remove"
#     #         print(f"Отображается 'Remove' для товара '{self.products[self.product_key]}'")
#     #
#     #         # Вторая проверка - счетчик корзины
#     #         cart_badge = WebDriverWait(self.driver, 10).until(
#     #             EC.visibility_of_element_located(By.CLASS_NAME, "shopping_cart_badge")
#     #         )
#     #         actual_badge_text = cart_badge.text
#     #         assert actual_badge_text == "1"
#     #         print(f"Значок корзины +{cart_badge.text}")
#     #
#     #         return True
#     #
#     #     except:
#     #         print("Ошибка при добавлении товара")
#     #         return False
#
#     def check_product_in_cart(self):
#         """Проверка добавления нужного товара в корзину с отладкой"""
#         try:
#             print("\n🔍 Начинаем проверку корзины...")
#
#             # Сначала проверим текущее состояние страницы
#             print(f"Текущий URL: {self.driver.current_url}")
#
#             # Дадим немного времени на обновление страницы
#             time.sleep(1)
#
#             # Первая проверка - кнопка Remove
#             ID_button_remove = self.get_remove_id()
#             print(f"Ищем кнопку с ID: {ID_button_remove}")
#
#             # Пробуем найти элемент разными способами
#             try:
#                 # Быстрая попытка
#                 remove_button = self.driver.find_element(By.ID, ID_button_remove)
#                 print(f"Кнопка найдена через find_element, текст: '{remove_button.text}'")
#             except:
#                 print("Кнопка не найдена сразу, используем WebDriverWait...")
#                 remove_button = WebDriverWait(self.driver, 10).until(
#                     EC.presence_of_element_located((By.ID, ID_button_remove))
#                 )
#                 print(f"Кнопка найдена после ожидания, текст: '{remove_button.text}'")
#
#             # Проверяем текст кнопки
#             if remove_button.text == "Remove":
#                 print(f"✓ Кнопка 'Remove' найдена для товара '{self.products[self.product_key]}'")
#             else:
#                 print(f"✗ Неверный текст кнопки: '{remove_button.text}' вместо 'Remove'")
#                 return False
#
#             # Вторая проверка - счетчик корзины
#             print("\n🔍 Проверяем счетчик корзины...")
#
#             # Проверяем все элементы с классом shopping_cart_badge
#             badges = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
#             print(f"Найдено элементов с классом shopping_cart_badge: {len(badges)}")
#
#             if len(badges) == 0:
#                 print("✗ Значок корзины не найден!")
#                 # Делаем скриншот для отладки
#                 self.driver.save_screenshot("debug_no_badge.png")
#                 print("Скриншот сохранен как debug_no_badge.png")
#                 return False
#
#             cart_badge = badges[0]
#             badge_text = cart_badge.text
#             print(f"Текст значка: '{badge_text}'")
#
#             if badge_text == "1":
#                 print(f"✓ Счетчик корзины корректен: {badge_text}")
#             else:
#                 print(f"✗ Неверный счетчик: '{badge_text}' вместо '1'")
#                 return False
#
#             print("\n✅ Все проверки пройдены успешно!")
#             return True
#
#         except Exception as e:
#             print(f"\n❌ Критическая ошибка: {type(e).__name__}: {e}")
#             import traceback
#             traceback.print_exc()
#             return False
#
#     def verify_product_in_cart(self):
#         """Проверка товара в корзине"""
#         try:
#             # переход в корзину
#             cart_link = WebDriverWait(self.driver,10).until(
#                 EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
#             )
#             cart_link.click()
#             print("Переход в корзину выполнен")
#
#             # проверка url корзины
#             WebDriverWait(self.driver, 10).until(
#                 EC.url_to_be("https://www.saucedemo.com/cart.html")
#             )
#
#             # проверка названия товара
#             cart_product_name = WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_element_located(By.CLASS_NAME, ["inventory_item_name"])
#             )
#             assert cart_product_name.text == products[product_key]
#             print(f"Название товара в корзине корректно: {products[product_key]}")
#
#             return True
#
#         except Exception as e:
#             print(f"Ошибка при проверке корзины: {e}")
#             return False
#
#
#
# Запуск теста

print("Запуск автоматизированного тестирования Sauce Demo")
print("-" * 20)

# Создаем экземпляр класса
test = SauceDemoSmokeTest(product_search)
# test.run()  # Вызываем основной метод, который вызывает все остальные
# )
#
# # Выполняем проверку
# if test_framework.check_product_in_cart():
#     print("=" * 60)
#     print("Тест пройден успешно!")
# else:
#     print("=" * 60)
#     print("Тест не пройден!")
#
# print("=" * 60)



"""
1. Запускаем программу
2. Программа спрашивает: "Какой товар тестируем? (1-6)"
3. Пользователь вводит число (например, 3)
4. Программа запоминает: "тестируем товар №3"
5. Открывается браузер
6. Автоматически вводится логин/пароль
7. Автоматически добавляется товар №3 в корзину
8. Проверяется, что товар добавился
9. Браузер закрывается
10. Программа говорит: "Тест пройден!" или "Ошибка!"
"""