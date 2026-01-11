import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)  # Чтобы автоматически не закрывался браузер
# g = Service()  # Управляет процессом ChromeDriver (остановка / запуск), передача доп. парам. в него

driver = webdriver.Chrome() # Внутри можно передать (options=options, service=g)

driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
driver.maximize_window()
time.sleep(3)

# message = "Hello world"
# input_text_field = driver.find_element(By.XPATH, "//input[@id='user-message']")
# input_text_field.send_keys(message)
#
# button_get_value = driver.find_element(By.XPATH, "//button[@id='showInput']")
# button_get_value.click()
# time.sleep(3)
# print("1 Текст введен в поле и кнопка отправить нажата")
#
# your_message_field = driver.find_element(By.XPATH, "//p[@id='message']")
# value_your_message_field = your_message_field.text
# print("2 проверочный вывод на странице - ОК")
#
# assert value_your_message_field == message
# print("3 Значения верны")


num_1 = 567
input_text_field_1 = driver.find_element(By.XPATH, "//input[@id='sum1']")
input_text_field_1.send_keys(num_1)

num_2 = 433
input_text_field_2 = driver.find_element(By.XPATH, "//input[@id='sum2']")
input_text_field_2.send_keys(num_2)

button_get_sum = driver.find_element(By.XPATH, "//button[contains(text(), 'Get Sum')]")
button_get_sum.click()
time.sleep(3)
print("4 Текст введен в два поля и кнопка отправить нажата")

result_field = driver.find_element(By.XPATH, "//p[@id='addmessage']")
value_result_field = result_field.text
print("5 вывод результата на странице - ОК")

sum = num_1 + num_2  # 1000

assert value_result_field == str(sum)
print("6 Значения верны")
