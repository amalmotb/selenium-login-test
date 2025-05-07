from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch the Chrome browser
driver = webdriver.Chrome()

# Navigate to the OrangeHRM demo login page
driver.get("https://opensource-demo.orangehrmlive.com/")

# Wait for 2 seconds to allow the page to load
time.sleep(2)

# Enter the username ("Admin") into the username input field
driver.find_element(By.NAME, "username").send_keys("Admin")

# Enter the password ("admin123") into the password input field
driver.find_element(By.NAME, "password").send_keys("admin123")

# Click the login button to attempt login
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Wait for 3 seconds to observe the result after logging in
time.sleep(3)

# Pause the script until the user presses Enter, then close the browser
input("Press Enter to close the browser...")
driver
