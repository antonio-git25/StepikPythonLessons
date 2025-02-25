import time #for time sleep option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service   #for chrome webdriver fix problem with closing
from selenium.webdriver.common.by import By

from faker import Faker


# #For firefox
# driver = webdriver.Firefox()
# driver.get('https://www.saucedemo.com/')
# driver.maximize_window()
# time.sleep(5)
# driver.close()

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# g = Service()
# driver = webdriver.Chrome(options=options, service=g)
# driver.get('https://www.saucedemo.com/')
# driver.maximize_window()
#
# #username = driver.find_element(By.ID,"user-name")
# #username = driver.find_element(By.NAME, "user-name")
# #username = driver.find_element(By.XPATH, '//*[@id="user-name"]')
# username = driver.find_element(By.XPATH, "//input[@name='user-name']")
# password = driver.find_element(By.XPATH, "//input[@name='password']")
# button_login = driver.find_element(By.ID, 'login-button')
#
# username.send_keys("standard_user")
# password.send_keys("secret_sauce")
# button_login.click()



faker = Faker("en_US")
name = faker.first_name() + str(faker.random_int())
print(name)

# time.sleep(5)
# driver.close()



