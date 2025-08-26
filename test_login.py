from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Deschide Chrome
driver = webdriver.Chrome()

# Mergi pe site demo
driver.get("https://the-internet.herokuapp.com/login")

# Introdu username și password
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Așteaptă 2 secunde
time.sleep(2)

# Verifică mesaj succes
success_text = driver.find_element(By.ID, "flash").text
print(success_text)

# Închide browserul
driver.quit()
