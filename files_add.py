'https://omz-software.com/pythonista/docs/ios/faker.html'
'https://faker.readthedocs.io/en/master/providers/faker.providers.person.html'

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service

from faker import Faker

faker = Faker('ru_Ru')  # Экземпляр класса Faker для генерации случайных данных на русском

name = faker.name() + str(faker.random_int())
print(name)
# Ярополк Терентьевич Пахомов9921

date = faker.date_between(start_date='-30y', end_date='now')
print(date)
# 1996-08-26

random = faker.sentence()
print(random)
# Вариант лиловый плясать дьявол посвятить.

birthday = faker.date_of_birth()
print(birthday)
# 1925-05-03

url = faker.url()
print(url)
# http://www.zao.biz/


name = faker.first_name() + str(faker.random_int())
pswd = faker.password()
print(name)
print(pswd)

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)  # Чтобы автоматически не закрывался браузер
# g = Service()  # Управляет процессом ChromeDriver (остановка / запуск), передача доп. парам. в него

driver = webdriver.Chrome() # Внутри можно передать (options=options, service=g)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(3)

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(name)
print("Login - OK")

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(pswd)
print("Password - OK")

time.sleep(2)

