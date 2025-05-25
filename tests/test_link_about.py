import datetime
from random import randint
import time #for time sleep option

import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service   #for chrome webdriver fix problem with closing
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


@allure.description("test_link_about")
def test_link_about():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    #options.add_argument("--headless") #open driver without visual browser
    #driver = webdriver.Chrome(executable_path='C:\\Users\\Antonio\\PycharmProjects\\ResourceDriver\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=Service())

    print("Start Test")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_menu_about()


    print("Finish Test!")
    time.sleep(3)
    driver.close()



