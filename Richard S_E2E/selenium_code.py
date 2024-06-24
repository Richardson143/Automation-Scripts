from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get('https://www.amazon.com')
element = driver.find_element(By.XPATH, "//a[text()='Try different image']")
element.click()
element = driver.find_element(By.XPATH, "//a[text()='Try different image']")
element.click()
driver.find_element(By.XPATH, "//textarea[@name='field-keywords'] | //input[@name='field-keywords']").send_keys("\ue009a")
driver.find_element(By.XPATH, "//textarea[@name='field-keywords'] | //input[@name='field-keywords']").send_keys(Keys.END)
driver.find_element(By.XPATH, "//textarea[@name='field-keywords'] | //input[@name='field-keywords']").send_keys("Iphone15pro max")
driver.find_element(By.XPATH, "//textarea[@name='field-keywords'] | //input[@name='field-keywords']").send_keys(Keys.ENTER)
element = driver.find_element(By.XPATH, "//button[text()='Add to cart']")
element.click()

driver.quit()
