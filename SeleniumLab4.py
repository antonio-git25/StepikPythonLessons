import datetime
from random import randint
import time #for time sleep option
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service   #for chrome webdriver fix problem with closing
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver
from selenium.common.exceptions import NoSuchElementException


class Login_process():
    def __init__(self, driver):
        self.driver = driver


    def login(self, login_name, login_password):
        log_error = 0 #True
        username = driver.find_element(By.XPATH, "//input[@id='user-name']")
        password = driver.find_element(By.XPATH, "//input[@id='password']")
        button_login = driver.find_element(By.XPATH, "//input[@name='login-button']")
        # Login in market
        print("Market authentification")
        username.send_keys(login_name)
        time.sleep(1)
        password.send_keys(login_password)
        time.sleep(1)
        button_login.click()
        time.sleep(3)
        print(f"authorization under {login_name}")

        #Step: check correct login/password
        try:
            warning = driver.find_element(By.XPATH, "//h3[@data-test='error']")
            value_warn = warning.text
            assert value_warn == "Epic sadface: Sorry, this user has been locked out."
            print(warning.text)
            log_error = 1 #False for cancel logout
            driver.refresh()
            time.sleep(4)
        except NoSuchElementException:
            pass

        return log_error


    def check_auth(self):
        #Check authorization page
        time.sleep(2)
        text_products = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        value_text_products = text_products.text
        print(value_text_products)
        assert value_text_products == 'Products'
        print("GOOD")


    def logout(self):
        menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
        out = driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']")
        menu.click()
        time.sleep(2)
        out.click()
        time.sleep(3)
        print("logout")


#######################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("--headless") #open driver without visual browser
# driver = webdriver.Chrome(executable_path='C:\\Users\\Antonio\\PycharmProjects\\ResourceDriver\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
time.sleep(3)
print("Browser is started")


password = "secret_sauce"
user_mass = ["standard_user","locked_out_user","problem_user","performance_glitch_user","error_user","visual_user"]

test_1 = Login_process(driver)

#main process
for user in user_mass:
    marker=test_1.login(login_name = user, login_password = password)
    print(f"st={marker}")
    if marker == 0:
        test_1.check_auth()
        test_1.logout()
    elif marker == 1:
        pass
    time.sleep(2)
    print("next user checking")


print("complete!")
time.sleep(5)
driver.close()