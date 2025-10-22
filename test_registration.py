from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start ChromeDriver
driver = webdriver.Chrome()

# Open your Kubernetes app (use the correct NodePort)
driver.get("http://localhost:30824/")  # <-- use the correct NodePort

time.sleep(2)

# Fill the form
driver.find_element(By.NAME, "full_name").send_keys("Test User")
driver.find_element(By.NAME, "email").send_keys("test_user@gmail.com")
driver.find_element(By.NAME, "username").send_keys("testuser123")
driver.find_element(By.NAME, "password").send_keys("password123")
driver.find_element(By.NAME, "confirm_password").send_keys("password123")
driver.find_element(By.NAME, "phone").send_keys("9876543210")
driver.find_element(By.NAME, "dob").send_keys("2000-01-01")
driver.find_element(By.NAME, "gender").send_keys("Male")
driver.find_element(By.NAME, "address").send_keys("Hyderabad, India")

# Submit the form
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(3)

print("Test Completed Successfully!")
driver.quit()
