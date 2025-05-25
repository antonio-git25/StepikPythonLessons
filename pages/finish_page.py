from datetime import time
import datetime
import time #for time sleep option

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Finish_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    #Methods
    def finish(self):
        with allure.step("finish"):
            self.get_current_url()
            self.assert_url("https://www.saucedemo.com/checkout-complete.html")
            self.get_screenshot()
