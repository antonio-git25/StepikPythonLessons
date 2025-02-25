#Logim with negative scenario

import time #for time sleep option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service   #for chrome webdriver fix problem with closing
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless") #open driver without visual browser
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

log = 'standard_use'
passw = 'secret_sauce'

username = driver.find_element(By.XPATH, "//input[@id='user-name']")
password = driver.find_element(By.XPATH, "//input[@id='password']")
button_login = driver.find_element(By.XPATH, "//input[@name='login-button']")
username.send_keys(log)
print("Input login")
password.send_keys(passw)
print("Input password")
button_login.click()
print("Click login")
time.sleep(2)

#Epic sadface: Username and password do not match any user in this service
warning = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warn = warning.text
assert value_warn == "Epic sadface: Username and password do not match any user in this service"
print("Good negative")

get_url = driver.current_url
assert get_url == "https://www.saucedemo.com/"

driver.refresh()
time.sleep(1)
username = driver.find_element(By.XPATH, "//input[@id='user-name']")
#enter login again by keyword type imitation
username.send_keys(log)
time.sleep(1)
username.send_keys(Keys.BACKSPACE)
time.sleep(1)
username.send_keys(Keys.BACKSPACE)
time.sleep(1)
username.send_keys(Keys.RETURN)
time.sleep(1)

time.sleep(5)
driver.close()