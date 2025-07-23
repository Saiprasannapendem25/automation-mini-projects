from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Correct full path to your ChromeDriver
chrome_driver_path = r"C:\Users\Pendem Sai prasanna\Desktop\Python-Workspace\GitPractice\chromedriver.exe"

# Setup Chrome service
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")

# Wait 5 seconds
time.sleep(5)

# Close browser
driver.quit()
