import time

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
driver  = webdriver.Chrome(ChromeDriverManager().install())

print("test passed")
driver.maximize_window()
driver.get("https://www.amazon.in/your-account")
driver.find_element_by_id("twotabsearchtextbox").send_keys("samsung m30s")
driver.find_element_by_id("nav-search-submit-button").click()
time.sleep(200)

driver.close()
print("Test case completed.")