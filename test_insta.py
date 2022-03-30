import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver= webdriver.Chrome(ChromeDriverManager().install())
username=input("enter user name")
password=input("enter password")
print("Test Case Started")
driver.maximize_window()
driver.get("https://www.instagram.com/")
time.sleep(1)
driver.find_element_by_name("username").send_keys(username)
time.sleep(1)
driver.find_element_by_name("password").send_keys(password)
time.sleep(1)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(50)
driver.close()
print("test is sucesfully")