import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(1)

# Всплывающее уведомление только с кнопкой ОК

# button_click_arlert = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
# button_click_arlert.click()
# time.sleep(1)
# print("button_click_arlert")
#
# driver.switch_to.alert.accept()  # если нужна кнопка отмена - dismiss
# time.sleep(2)
#
# result_text = driver.find_element(By.XPATH, "//p[@id='result']")
# value_result_text = "You successfully clicked an alert"
# assert value_result_text == result_text.text
# print("OK")

# Всплывающее уведомление с кнопками ОК и Отмена

# button_click_confirm = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
# button_click_confirm.click()
# time.sleep(1)
# print("button_click_confirm")

# driver.switch_to.alert.dismiss()  # отклонение (1)
# print("dismiss")
#
# result_text = driver.find_element(By.XPATH, "//p[@id='result']")
# value_result_text = "You clicked: Cancel"
# assert value_result_text == result_text.text
# print("OK")

# driver.switch_to.alert.accept()  # подтверждение (2)
# print("accept")
#
# result_text = driver.find_element(By.XPATH, "//p[@id='result']")
# value_result_text = "You clicked: Ok"
# assert value_result_text == result_text.text
# print("OK")

# Всплывающее уведомление с кнопками ОК и Отмена + текст

button_click_promt = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
button_click_promt.click()
time.sleep(1)
print("button_click_promt")

text = "test123"
driver.switch_to.alert.send_keys(text)
time.sleep(1)

# driver.switch_to.alert.dismiss()  # отклонение (1)
# print("dismiss")
#
# result_text = driver.find_element(By.XPATH, "//p[@id='result']")
# value_result_text = "You entered: null"  # f"You entered: {text}"
# print(value_result_text)
# assert value_result_text == result_text.text
# print("OK")

print(driver.switch_to.alert.text)
# I am a JS prompt

driver.switch_to.alert.accept()  # подтверждение (2)
print("accept")

result_text = driver.find_element(By.XPATH, "//p[@id='result']")
value_result_text = f"You entered: {text}"
print(value_result_text)
assert value_result_text == result_text.text
print("OK")