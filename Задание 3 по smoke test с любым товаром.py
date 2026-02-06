import time

from selenium import webdriver  # инструмент для автоматизации браузера
from selenium.webdriver.common.by import By  # поиск элементов на странице
from selenium.webdriver.support.wait import WebDriverWait  # явное ожидание элементов
from selenium.webdriver.support import expected_conditions as EC  # условное ожидание элементов
from selenium.webdriver.chrome.options import Options  # настройки браузера Chrome


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

    def __init__(self):
        """
        Конструктор класса. Вызывается при СОЗДАНИИ объекта
        Инициализирует пустые переменные.
        """
        self.driver = None  # хранение браузера
        self.selected_product_key = None  # хранение выбранного товара (1-6)
        self.selected_product_name = None  # хранение выбранного товара (имя)

    @classmethod  # декоратор для обозначения метода класса, а не объекта
    def select_product(cls):  # ссылка на сам класс
        """
        класс-метод можно вызвать БЕЗ создания объекта
        """
        print("Приветствую тебя в нашем интернет - магазине.")
        print(f"Выбери один из следующих товаров и укажи его номер: ")

        for key, value in cls.products.items():  # обращаемся к словарю класса (не объекта)
            print(f"{key} - {value}")  # показываем товар "1..", "2.." и т.д.

        while True:  # бесконечный цикл, пока не поймаем число
            try:
                product_key = int(input("Введите номер товара от 1 до 6: "))

                if product_key in cls.products:
                    product_name = cls.products[product_key]

                    print(f"Выбран товар: {product_key} - {product_name}")
                    print("-" * 20)

                    return product_key, product_name

                else:
                    print("Ошибка выбора номера товара")

            except ValueError:
                print("Ошибка ввода")

    def setup_browser(self):
        """Настройка браузера"""
        chrome_options = Options()
        chrome_options.add_argument('--incognito')  # нет всплывающих окон "пароля" / "перевода стр"

        # Создаем драйвер (открытие браузера с выбранными настройками)
        self.driver = webdriver.Chrome(options=chrome_options)

        # Открываем сайт
        url_authorisation = "https://www.saucedemo.com/"
        self.driver.get(url_authorisation)

        # Настройки ожидания
        self.driver.implicitly_wait(5)  # ждем элементы до 5 секунд
        self.driver.maximize_window()  # на весь экран

        print("Настройка браузера инициализирована")
        return self.driver

    def authorization(self):
        """Авторизация пользователя"""
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
        print("-" * 20)  # разделитель текста

        return self

    def add_product_in_cart(self):
        """
        1. Составление ID локатора для поиска элемента "add to cart" (добавить в корзину):
            1.1 Пробелы заменены на "-"
            1.2 Регистр lowercase
            1.3 Добавляется конструкция "add-to-cart-"

        2 Составление ID локатора для поиска элемента "remove-" (удалить из корзины):
            2.1 [см 1.1...]
            2.2 [см 1.2...]
            2.3 Добавляется конструкция "remove-"

        3. Добавление товара в корзину
        4. Проверки:
            4.1 Смена кнопки на Remove
            4.2 Счетчик корзины +1
        """
        # ID локатор "add-to-cart-"
        ID_add_product = self.products[self.selected_product_key]
        ID_add = f"add-to-cart-{ID_add_product.lower().replace(' ', '-')}"
        print(f"Отладка. Локатор ID_add: {ID_add}")

        # ID локатор "remove-"
        ID_add_product = self.products[self.selected_product_key]
        ID_remove = f"remove-{ID_add_product.lower().replace(' ', '-')}"
        print(f"Отладка. Локатор ID_remove: {ID_remove}")

        # Добавление товара в корзину
        button_add_item = self.driver.find_element(By.XPATH, f"//button[@id='{ID_add}']")
        button_add_item.click()
        print(f"Товар '{ID_add_product}' добавлен в корзину")
        print("-" * 20)  # разделитель текста
        time.sleep(2)

        # Проверки
        try:
            # Cмена названия кнопки на Remove

            # двойные скобки, чтобы система не думала, что у нас два аргумента
            # ((внешние скобки - вызов метода, внутренние - один кортеж-аргумент))
            remove_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, ID_remove))
            )
            # Проверяем текст кнопки
            actual_text_remove_button = remove_button.text
            assert actual_text_remove_button == "Remove"
            print(f"1. Отображается 'Remove' для товара '{product_name}'")

            # Счетчик корзины
            cart_badge = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
            )
            # Проверяем текст счетчика
            actual_badge_text = cart_badge.text
            assert actual_badge_text == "1"
            print(f"2. Значок корзины +{cart_badge.text}")

            return True

        except:
            print("Ошибка при добавлении товара")
            return False


    def verify_product_in_cart(self):
        """Проверка товара в корзине"""
        try:
            # переход в корзину
            cart_link = WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
            )
            cart_link.click()
            print("Переход в корзину выполнен")
            time.sleep(2)

            # проверка url корзины
            WebDriverWait(self.driver, 10).until(
                EC.url_to_be("https://www.saucedemo.com/cart.html")
            )
            print("Current url: https://www.saucedemo.com/cart.html")

            # проверка названия товара
            cart_product_name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name"))
            )
            assert cart_product_name.text == product_name
            print(f"Название товара в корзине корректно: {product_name}")

            # цена товара в корзине
            value_xpath = "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div"
            price_cart_inventory_one = self.driver.find_element(By.XPATH, {value_xpath})

            # цена товара на витрине
            price_number = product_key
            inventory_item_price = self.driver.find_element(By.CLASS_NAME, "inventory_item_price[price_number]")
            value_price_inventory = inventory_item_price.text

            # сверка цены
            value_price_cart_inventory_one = price_cart_inventory_one.text
            assert value_price_cart_inventory_one == value_price_inventory
            print(value_price_cart_inventory_one)

            print(f"Цена товара в корзине корректна: {value_price_cart_inventory_one}")

            return True

        except Exception as e:
            print(f"Ошибка при проверке корзины: {e}")
            return False



if __name__ == "__main__":
    """
    Запускаем код напрямую из файла или python current_name_file.py 
    Если через импорт, программа не запустится!
    """
    # Выбираем товар (класс.метод)
    product_key, product_name = SauceDemoSmokeTest.select_product()

    # создаем объект (объект.метод)
    test = SauceDemoSmokeTest()
    result_settings = test.setup_browser()
    result_authorization = test.authorization()
    # сохраняем значение переменной в атрибуте объекта (чтобы не падала ошибка KeyError: None)
    test.selected_product_key = product_key
    test.selected_product_name = product_name
    result_add_product = test.add_product_in_cart()
    result_verify_cart = test.verify_product_in_cart()





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