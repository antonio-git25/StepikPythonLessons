import datetime
from random import randint
import time #for time sleep option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service   #for chrome webdriver fix problem with closing
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import Login_page


class Test_2():
    def test_select_product(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        #options.add_argument("--headless") #open driver without visual browser
        #driver = webdriver.Chrome(executable_path='C:\\Users\\Antonio\\PycharmProjects\\ResourceDriver\\chromedriver.exe')
        driver = webdriver.Chrome(options=options, service=Service())
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()

        login = Login_page(driver)
        login.authorization(login_name="problem_user", login_password="secret_sauce")

        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print("select product")
        time.sleep(1)

        basket = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']")))
        basket.click()
        print("go to backet")
        time.sleep(2)

        text_basket = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        value_text_basket = text_basket.text
        assert value_text_basket == 'Your Cart'
        print("Your Cart")



test = Test_2()
test.test_select_product()