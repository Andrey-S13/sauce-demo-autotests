import time

from selenium import webdriver  # инструмент для автоматизации браузера
from selenium.webdriver.common.by import By  # поиск элементов на странице
from selenium.webdriver.support.wait import WebDriverWait  # явное ожидание элементов
from selenium.webdriver.support import expected_conditions as EC  # условное ожидание элементов
from selenium.webdriver.chrome.options import Options  # настройки браузера Chrome


class SauceDemoSmokeTest:
    """Класс для Smoke теста по покупке товара в интернет магазине Sauce Demo"""

    def __init__(self):
        """
        Конструктор класса. Вызывается при СОЗДАНИИ объекта
        Инициализирует пустые переменные.
        """
        self.driver = None  # хранение браузера
        self.selected_product_key = None  # хранение выбранного товара (1-6)
        self.selected_product_name = None  # хранение выбранного товара (имя)
        self.selected_product_price = None  # хранение цены выбранного товара

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
        self.driver.implicitly_wait(3)  # ждем элементы до 3 секунд
        self.driver.maximize_window()  # на весь экран

        print("Настройка браузера инициализирована")
        return self.driver

    def select_product(self):
        """
        Приветствие и выбор товара
        """
        print("-" * 20)  # разделитель текста
        print("Приветствую тебя в нашем интернет - магазине.")
        print(f"Выбери один из следующих товаров и укажи его номер: 1 - Sauce Labs Backpack, " 
        f"2 - Sauce Labs Bike Light, 3 - Sauce Labs Bolt T-Shirt, 4 - Sauce Labs Fleece Jacket, "
        f"5 - Sauce Labs Onesie, 6 - Test.allTheThings() T-Shirt (Red)")
        product_key = int(input("\nВведите номер товара от 1 до 6: "))
        self.selected_product_key = product_key  # НОМЕР сохраняем в переменной класса
        print(f"Номер товара: {self.selected_product_key}")
        print("-" * 20)

    def select_item(self):
        """Выбор товара через введенное число"""
        # (// div[@ data-test='inventory-item-name'])[1]
        selected_item = self.driver.find_element(By.XPATH, f"(//div[@data-test='inventory-item-name'])[{self.selected_product_key}]")
        self.selected_product_name = selected_item.text
        print(f"Выбран товар: {self.selected_product_key} - {self.selected_product_name}")
        print("-" * 20)

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
        1. Добавление товара в корзину
        2. Определение цены товара
        3. Проверки:
            3.1 Смена кнопки на Remove
            3.2 Счетчик корзины +1
        """
        # Добавление товара в корзину
        button_add_item = self.driver.find_element(By.XPATH, f"(//button[@class='btn btn_primary btn_small btn_inventory '])[{self.selected_product_key}]")
        button_add_item.click()

        product_name = self.selected_product_name
        print(f"Товар '{self.selected_product_name}' добавлен в корзину")

        # цена товара на витрине (для дальнейших проверок в корзине и на финально странице)
        price_inventory = self.driver.find_element(By.XPATH, f"(//div[@class='inventory_item_price'])[{self.selected_product_key}]")
        price_inventory_text = price_inventory.text
        self.selected_product_price = price_inventory_text
        print(f"Цена товара на главной странице: {price_inventory_text}")
        print("-" * 20)  # разделитель текста
        time.sleep(2)

        # Проверки
        try:
            # Cмена названия кнопки на Remove
            """          
            1) двойные скобки, чтобы система не думала, что у нас два аргумента
            ((внешние скобки - вызов метода, внутренние - один кортеж-аргумент))
            (
                EC.visibility_of_element_located((By.ID, ID_remove))
            )
            2) XPATH: находим по имени товара -> поднимаемся до inventory-item-name -> опускаемся к кнопке Remove
            """

            remove_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, f"(//div[@data-test='inventory-item-description'])"
                                                            f"[{self.selected_product_key}]//"
                                                            f"button[contains(@id, 'remove')]"))
            )

            # Проверяем текст кнопки
            assert remove_button.text == "Remove"
            print(f"1. Отображается 'Remove' для товара '{self.selected_product_name}'")

            # Счетчик корзины
            cart_badge = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
            )
            # Проверяем текст счетчика
            actual_badge_text = cart_badge.text

            assert actual_badge_text == "1"
            print(f"2. Значок корзины +{cart_badge.text}")
            print("-" * 20)  # разделитель текста

            return True

        except:
            print("Ошибка при добавлении товара")

            return False

    def verify_product_in_cart(self):
        """Проверка товара в корзине"""
        product_key = self.selected_product_key
        product_name = self.selected_product_name
        price_inventory_text = self.selected_product_price

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
                EC.presence_of_element_located((By.XPATH, f"//div[@class='inventory_item_name' and text()='{self.selected_product_name}']"))
            )
            assert cart_product_name.text == product_name
            print(f"Название товара в корзине корректно: {self.selected_product_name}")

            # цена товара в корзине
            """
            XPATH: находим по имени > поднимаемся до cart_item > опускаемся к цене
            """
            price_cart_inventory = self.driver.find_element(By.XPATH, f"//div[@class='inventory_item_name' and text()='{self.selected_product_name}']/"
                                                                      f"ancestor::div[@class='cart_item']//"
                                                                      f"div[@class='inventory_item_price']")
            print(f"Цена в корзине: {price_cart_inventory.text}")

            # сверка цены
            value_price_cart_inventory = price_cart_inventory.text

            assert value_price_cart_inventory == price_inventory_text
            print(f"Цена товара в корзине не отличается")
            print("-" * 20)  # разделитель текста

            return True

        except Exception as e:
            print(f"Ошибка при проверке корзины: {e}")

            return False

    def checkout_page(self):
        """Страница просмотра выбранных товаров"""
        checkout_button = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn_action.btn_medium.checkout_button")
        checkout_button.click()
        time.sleep(1)
        print("Отладка. Нажатие на 'Checkout'")

        url_information_page = "https://www.saucedemo.com/checkout-step-one.html"
        current_url_after_checkout = self.driver.current_url

        assert current_url_after_checkout == url_information_page
        print(f"Current url: {url_information_page}")

    def add_personal_data_page(self):
        """Заполнение данных для оформления заказа"""
        # имя
        first_name = self.driver.find_element(By.ID, "first-name")
        first_name.send_keys("Andrey")
        # фамилия
        last_name = self.driver.find_element(By.ID, "last-name")
        last_name.send_keys("Suvorov")
        # почтовый индекс
        Postal_code = self.driver.find_element(By.ID, "postal-code")
        Postal_code.send_keys("123456")
        time.sleep(1)
        print("Контактные данные заполнены")

    def click_continue(self):
        """подтвердить заполнение персональных данных"""
        Continue_button = self.driver.find_element(By.ID, "continue")
        Continue_button.click()
        time.sleep(1)
        print("Кнопка 'Continue' нажата")

        url_overview_page = "https://www.saucedemo.com/checkout-step-two.html"
        current_url_after_continue = self.driver.current_url

        assert current_url_after_continue == url_overview_page
        print("Переход на страницу 'Checkout: Overview' выполнен")
        print("-" * 20)  # разделитель текста
        time.sleep(2)

    def check_overview_page(self):
        """проверка заказа"""
        # Сравниваем по товарам на витрине
        overview_inventory = self.driver.find_element(By.CLASS_NAME, 'inventory_item_name')
        name_overview_inventory = overview_inventory.text

        assert name_overview_inventory == self.selected_product_name
        print(f"Название товара идентично другим вкладкам ({name_overview_inventory})")

        # Сравниваем по товарам в корзине

        price_overview_inventory = self.driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
        value_price_overview_inventory = price_overview_inventory.text

        assert value_price_overview_inventory == self.selected_product_price
        print(f"Цена идентична другим вкладкам ({value_price_overview_inventory})")

    def check_total_price(self):
        """Сверка финальной цены после автоматических расчетов"""
        # преобразование стоимости в тип float
        value_price_overview_inventory_int = self.selected_product_price.replace('$', '')  # цена без $
        value_price_overview = float(value_price_overview_inventory_int)
        print("Отладка. Цена товара: " + str(value_price_overview))

        # итоговая стоимость в разделе "Price Total"
        item_total_price = self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label")
        value_item_total = item_total_price.text
        value_item_total_number = value_item_total.replace('Item total: $', '')
        print("Отладка. Цена всех товаров: " + value_item_total_number)
        # налоги в разделе "Price Total"
        item_total_tax = self.driver.find_element(By.CLASS_NAME, "summary_tax_label")
        value_item_tax = item_total_tax.text
        value_item_tax_number = value_item_tax.replace('Tax: $', '')
        print("Отладка. Налог: " + value_item_tax_number)

        # сравнение итоговой цены заказа с карточкой товара
        assert float(value_price_overview) == float(value_item_total_number)
        print("Итоговая стоимость товара правильная: " + str(value_item_total_number))

        # подсчет окончательной стоимости заказа
        total_price_order = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        valut_total_price_order = total_price_order.text
        finish_price_order_number = valut_total_price_order.replace('Total: $', '')

        finish_price_order_number_float = float(finish_price_order_number)
        # сумма стоимости товара и налога
        formula_finish_price = float(value_item_total_number) + float(value_item_tax_number)

        # добавляем округделие до сотых в проверке
        assert round(formula_finish_price, 2) == round(finish_price_order_number_float, 2)
        print("Итоговая цена правильная: " + value_item_total_number + " + " +
              value_item_tax_number + " = " + finish_price_order_number)

    def finish_order_click(self):
        """закрыть страницу с заказом"""
        finish_button = self.driver.find_element(By.ID, "finish")
        finish_button.click()
        print("Кнопка 'finish' нажата")
        print("-" * 20)  # разделитель текста
        time.sleep(2)

        complete_message = self.driver.find_element(By.XPATH, "//h2[text()='Thank you for your order!']")
        current_massage = complete_message.text

        assert current_massage == "Thank you for your order!"
        time.sleep(2)
        print("Сообщение 'Thank you for your order!'")
        print("-" * 20)  # разделитель текста

    def turn_back_home_page(self):
        """переход обратно на домашнюю страницу"""
        back_home_button = self.driver.find_element(By.ID, "back-to-products")
        back_home_button.click()
        page_url = "https://www.saucedemo.com/inventory.html"
        current_page_url = self.driver.current_url

        assert page_url == current_page_url
        time.sleep(2)
        print("Домашняя страница")

        print("=" * 20)  # разделитель текста
        print("Smoke тест пройден")


if __name__ == "__main__":
    """
    Запускаем код напрямую из файла или python current_name_file.py 
    Если через импорт, программа не запустится!
    """
    # создаем объект (объект.метод)
    test = SauceDemoSmokeTest()
    # используем методы класса (наши тесты)
    test.select_product()
    test.setup_browser()
    test.authorization()
    test.select_item()
    test.add_product_in_cart()
    test.verify_product_in_cart()
    test.checkout_page()
    test.add_personal_data_page()
    test.click_continue()
    test.check_overview_page()
    test.check_total_price()
    test.finish_order_click()
    test.turn_back_home_page()