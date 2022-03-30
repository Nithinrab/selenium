import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver= webdriver.Chrome(ChromeDriverManager().install())
print("Test Case Started")
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(1)
driver.find_element_by_name("email").send_keys("nithin")
time.sleep(1)
driver.find_element_by_name("pass").send_keys("455555")
time.sleep(1)
driver.find_element_by_name("login").click()
time.sleep(50)
driver.close()
print("test is sucesfully")