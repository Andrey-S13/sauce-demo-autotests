import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")

driver.maximize_window()
time.sleep(3)

# Переключение между вкладками

# click_tab_button = driver.find_element(By.XPATH, "//button[@id='tabButton']")
# click_tab_button.click()
# print("click_tab_button")
# time.sleep(3)
# print(driver.current_url)
#
# header_tab_1 = driver.find_element(By.XPATH, "//h1[@class='text-center']")
# print(header_tab_1.text)
#
#
# driver.switch_to.window(driver.window_handles[1])
# time.sleep(1)
# print(driver.current_url)
# header_tab_2 = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']")
# print(header_tab_2.text)
#
# driver.switch_to.window(driver.window_handles[0])
# print(driver.current_url)
# time.sleep(1)


# Переключение между окнами

click_windowds_button = driver.find_element(By.XPATH, "//button[@id='windowButton']")
click_windowds_button.click()
print("click_windowds_button")
time.sleep(3)
print(driver.current_url)

header_window_1 = driver.find_element(By.XPATH, "//h1[@class='text-center']")
print(header_window_1.text)

windows_1 = driver.window_handles[0]
windows_2 = driver.window_handles[1]

driver.switch_to.window(windows_2)
print(driver.current_url)

header_window_2 = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']")
print(header_window_2.text)
time.sleep(1)

driver.close() # закроет текущую вкладку, если надо

driver.switch_to.window(windows_1)
print(driver.current_url)
print(header_window_1.text)


