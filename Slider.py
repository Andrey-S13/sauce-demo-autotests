import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

"""Сайт www.mvideo.ru"""

driver = webdriver.Chrome()
url_slider = "https://www.mvideo.ru/promo/vygodnye-ceny-na-tv-i-zvuk-hisense/f/tolko-v-nalichii=da"
driver.get(url_slider)
driver.maximize_window()

action = ActionChains(driver)  # Создали экземпляр класса ActionChains для взаимодейсвтия с мышью и передаем переменную
# driver, которая является экземпляром нашего браузера
time.sleep(3)  # загрузка сайта

name_price = driver.find_element(By.XPATH, "(//a[@class='filter-name'])[2]")
action.move_to_element(name_price).perform()
time.sleep(3) # прокрутка страницы до нужного локатора

'''
Ползунок пока удается двигать в одну сторону - требуется явное ожидание или что-то еще
'''

# price_left = driver.find_element(By.CSS_SELECTOR, "button[style*='left: 0px']")
# action.click_and_hold(price_left).move_by_offset(100,0).release().perform() # release - отпустить нышь + perform = сохранить наш результат
# time.sleep(5)
# print("Price right +100")

price_right = driver.find_element(By.CSS_SELECTOR, "button[style*='left: 298px']")
action.click_and_hold(price_right).move_by_offset(-80,0).release().perform() # release - отпустить нышь + perform = сохранить наш результат
time.sleep(5)
print("Price right -80")




# """Сайт https://www.schoolsw3.com"""
#
# driver = webdriver.Chrome()
# url_slider = "https://www.schoolsw3.com/howto/howto_js_rangeslider.php"
# driver.get(url_slider)
# driver.maximize_window()
#
# action = ActionChains(driver)  # Создали экземпляр класса ActionChains для взаимодействия с мышью и передаем переменную
# # driver, которая является экземпляром нашего браузера
# time.sleep(3)  # загрузка сайта
#
# price = driver.find_element(By.XPATH, "//input[@id='id2']")
# action.click_and_hold(price).move_by_offset(100,0).release().perform() # release - отпустить нышь + perform = сохранить наш результат
# time.sleep(5)
# print("Slider OK")
