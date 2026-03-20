'''
Selenium - это инструмент для автоматизации тестирования веб-приложений.
Локатор - это "адрес" наешго элемента - кнопки, поля, чек-бокса и т.д., с помощью которого мы можем к нему обратиться
'''

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\python_selenium\\chromedriver.exe')  - до 4 версии selenium прописывалось так
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# user_name = driver.find_element(By.ID, "user-name")  # ID
# user_name = driver.find_element(By.NAME, "user-name")  # NAME
# user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")  # Full XPATH; * - обращается к любому id = user_name на странице. ОДИНАРНЫЕ кавычки внутри локатора
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")  # ID XPATH
# user_name = driver.find_element(By.XPATH, "//input[@data-test='username']")  # data-test XPATH
# user_name = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div[2]/h4")  # Password for all users XPATH
# user_name = driver.find_element(By.XPATH, "(//div[@class='form_group'])[2]")  # form_group XPATH
# user_name = driver.find_element(By.XPATH, "//h4[contains(text(), 'ccepted use')]")  # Accepted usernames are: XPATH - частичный поиск
# user_name = driver.find_element(By.NAME, "user-name")  # NAME
# user_name = driver.find_element(By.CSS_SELECTOR, ".input_error.form_input")  # Class - не забывать ставить точки в составном классе
user_name.send_keys("standard_user")

password = driver.find_element(By.CSS_SELECTOR, "#password")  # SCC_SELECTOR
password.send_keys("secret_sauce")

button_login = driver.find_element(By.XPATH, "//input[@value='Login']")
button_login.click()

'''
var = driver.find_element(By.ID, "Login")

var - переменная
driver - экземпляр класса библиотеки WebDriver, для возможности управлять браузеру
find_element() - метод для поиска локатора ПО, без уточнения его аргумента
By.ID - указание драйверу, по какому аргументу будет производиться поиск
Login - значение аргумента, по которому будет производиться поиск, берется в кавычки '' или ""

var.send_keys("user123")

send_keys() - метод для заполнения поля, внутри которого в кавычках мы указываем содержимое
Можно передавать значение в виде str, можно переменную

Локаторы:

# id
# name
# class_name
# xpath - универсальный. Можно обращаться по любому атрибуту. Можно из нескольких атрибутов составлять значение. Поиск по тексту и т.д. 
# lint_text
# tag_name
# css_selector

Из чего состоит локатор:

"//*[@id='user-name']"
"//input[@data-test='username']"
//*[@id="root"]/div/div[2]/div[2]/div/div[2]/h4 - локатор для заголовка "Password for all users"

// - начало локатора типа XPATH
* - тег локатора (с полем Login, к примеру, это input, для другого вместо звезды будет div и т.д.)

Если на странице два локатора одинаковых - для поля логин и пароль, можно делать так:
(//div[@class="form_group"])[1] - для логина
(//div[@class="form_group"])[2] - для пароля

"//h4|text()='Accepted usernames are:']"

//h4 - тег элемента
text() - метод по поиску текста на разметке нашей страницы
'Accepted usernames are:' - точное значение, помещенное между тегов (ищется только по ПОЛНОМУ совпадению текста)

"//h4[contains(text(), 'Accepted usernames are:')]"

contains() - метод поиска по части / точному значению
contains - ключевое слово, для создания контейнера, с помощью которого можно производить частичный поиск

1) Copy XPATH
2) Copy full XPATH
3) Кастомный XPATH

Первые два ненадежные и привязаны к верстке. Елси что-то меняется, локаторы по полному и частичному пути сбиваются.
Третий вариант - лучшее решение. Мы состовляем параметры сами (по какому тегу или какой путь зададим)

CSS_SELECTOR - отвечает за оформление на странице (шрифты, цвет и т.д.)
'''

time.sleep(3)
# driver.close()