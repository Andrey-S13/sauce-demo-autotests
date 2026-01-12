"""iframe - (inline frame) это встроенный HTML-документ в другой (баннер, яндекс-карта на сайте и т.д) """

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)  # Чтобы автоматически не закрывался браузер
# g = Service()  # Управляет процессом ChromeDriver (остановка / запуск), передача доп. парам. в него

driver = webdriver.Chrome() # Внутри можно передать (options=options, service=g)

driver.get("https://www.lambdatest.com/selenium-playground/iframe-demo/")
driver.maximize_window()
time.sleep(3)

iframe = driver.find_element(By.XPATH, "//iframe[@id='iFrame1']")
driver.switch_to.frame(iframe)  # Обратно выключить driver.switch_to.default_content()

text = "'Новый текст добавлен'"
input_text_field = driver.find_element(By.XPATH, "//div[@id='__next']/div/div[2]")
input_text_field.send_keys(text)
value_input_text_field = input_text_field.text
time.sleep(2)
print("Текст " + text + " - введен")

input_text_field.click()
input_text_field.send_keys(Keys.COMMAND + 'a')

editing_panel_click_bold = driver.find_element(By.XPATH, "//button[@title='Bold']")
editing_panel_click_bold.click()
print("Текст выделяется жирным")
time.sleep(1)

new_input_text_field = driver.find_element(By.XPATH, "//div[@id='__next']/div/div[2]/b")
value_new_input_text_field = new_input_text_field.text
print(value_new_input_text_field)

assert value_input_text_field == value_new_input_text_field # проверка, что текст остался весь
print("Редактирование успешно")