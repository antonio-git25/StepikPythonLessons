from datetime import time
import datetime
import time #for time sleep option
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_page():
    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name, login_password):
        username = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        button_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='login-button']")))

        # Login in market
        print("Market authentification")
        username.send_keys(login_name)
        password.send_keys(login_password)
        button_login.click()
        time.sleep(3)