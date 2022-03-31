import time

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
driver  = webdriver.Chrome(ChromeDriverManager().install())

print("test passed")
driver.maximize_window()
driver.get("https://www.linkedin.com/home")
driver.find_element_by_name("session_key").send_keys("@gmail.com")
driver.find_element_by_name("session_password").send_keys("xyz")
driver.find_element_by_class_name("sign-in-form__submit-button").click()
driver.find_element_by_class_name("primary-action-new").click()
time.sleep(200)

driver.close()
print("Test case completed.")