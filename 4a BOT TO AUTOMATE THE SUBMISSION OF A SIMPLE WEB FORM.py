from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Step 1: Launch browser
driver = webdriver.Chrome()   # ChromeDriver must be installed
driver.maximize_window()
# Step 2: Open sample web form
driver.get("https://www.w3schools.com/html/html_forms.asp")
time.sleep(3)
# Step 3: Locate input fields and enter data
first_name = driver.find_element(By.ID, "fname")
last_name = driver.find_element(By.ID, "lname")
first_name.clear()
last_name.clear()
first_name.send_keys("RPA")
last_name.send_keys("Student")
# Step 4: Submit the form
last_name.send_keys(Keys.RETURN)
time.sleep(2)
# Step 5: Close browser
driver.quit()
