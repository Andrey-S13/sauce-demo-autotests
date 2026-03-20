import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# url_demoqa = "https://demoqa.com/radio-button"
# driver.get(url_demoqa)
# driver.maximize_window()

"""Сайт https://demoqa.com/radio-button"""

# radio_button = driver.find_element(By.XPATH, "//label[@class='custom-control-label']")
# radio_button.click()
# time.sleep(1)
# print("radio_button clicked")
#
# message_element = driver.find_element(By.CSS_SELECTOR, "p.mt-3")
# full_text = message_element.text  # "You have selected Yes"
# print(full_text)
#
# choice_element = driver.find_element(By.CSS_SELECTOR, "p.mt-3 span")
# choice = choice_element.text  # "Yes"
# print(choice)
#
# assert "You have selected " in full_text
# assert choice == "Yes"
# print("Passed")

# '''
# Проверка, что чекбокс неактивен
# '''
# radio_button_disabled = driver.find_element(By.ID, "noRadio")  # Для "impressiveRadio" проверка не пройдет
# if radio_button_disabled.is_enabled() == False:
#     print("No clicked - Passed")
# else:
#     print("NO Passed")

"""Сайт https://testpages.herokuapp.com/pages/forms/html-form/"""

driver = webdriver.Chrome()
url_testpages = "https://testpages.herokuapp.com/pages/forms/html-form/"
driver.get(url_testpages)
driver.maximize_window()

radio_button = driver.find_element(By.XPATH, "//input[@value='rd1']")
radio_button_location = radio_button.location
driver.execute_script(f"window.scrollTo(0, {radio_button_location['y']})")
time.sleep(1)
radio_button.click()
time.sleep(1)
print("radio_button clicked")