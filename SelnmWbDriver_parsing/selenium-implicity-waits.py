from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
import random
import string
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
from unicodedata import digit


def impl_wait_1():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/expectations/1/index.html')
        element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
        time.sleep(3)
        print(browser.find_element(By.ID, 'result').text)


def impl_wait_test_1():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/expectations/3/index.html')
        WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, "btn"))).click()

        WebDriverWait(browser, 30).until(EC.title_is('345FDG3245SFD'))

        code = browser.find_element(By.ID, 'result').text
        print(code)


def impl_wait_test_2():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/expectations/4/index.html')
        WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, "btn"))).click()

        WebDriverWait(browser, 30).until(EC.title_contains('JK8HQ'))
        code = browser.title
        print(code)


def impl_wait_test_3():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/expectations/6/index.html')
        WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, "btn"))).click()

        locator = (By.CLASS_NAME, 'BMH21YY')
        element = WebDriverWait(browser, 30).until(EC.presence_of_element_located(locator))
        print(element.text)


def impl_wait_test_4():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/5.9/2/index.html')
        locator = (By.ID, 'qQm9y1rk')
        WebDriverWait(browser, 100).until(EC.presence_of_element_located(locator)).click()

        alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
        print(alert.text)
        alert.accept()


def impl_wait_test_5():
    with webdriver.Chrome() as browser:
        ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I',
                       'jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']

        browser.get('https://parsinger.ru/selenium/5.9/3/index.html')
        for ids in ids_to_find:
            print(f"id: {ids}")
            locator = (By.ID, ids)
            WebDriverWait(browser, 100).until(EC.visibility_of_element_located(locator)).click()

        alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
        print(alert.text)
        alert.accept()


def visible_text_test_1():
    with webdriver.Chrome() as browser:
        browser.get("https://parsinger.ru/selenium/5.9/4/index.html")
        browser.execute_script('closeAd()')
        if WebDriverWait(browser, 6).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "#ad .close"))):
            browser.execute_script('showSecretNumber()')
            print(WebDriverWait(browser, 6).until(EC.presence_of_element_located((By.ID, "message"))).text)

        # Извлечение значения из тега <p>
        message = browser.find_element(By.ID, "message").text
        print("Секретное сообщение:", message)


def visible_text_test_2():
    with webdriver.Chrome() as browser:
        browser.get("https://parsinger.ru/selenium/5.9/5/index.html")
        time.sleep(2)
        locator_ad = (By.ID, "ad_window")
        locator_close = (By.ID, "close_ad")
        answers = [""] * 9
        buttons = browser.find_elements(By.CLASS_NAME, 'box_button')
        for button in buttons:
            WebDriverWait(browser, 30).until(EC.element_to_be_clickable(button)).click()
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable(locator_close)).click()
            WebDriverWait(browser, 30).until(EC.invisibility_of_element_located(locator_ad))
            WebDriverWait(browser, 10).until(lambda x: button.text != "")
            idx = int(button.get_attribute("data-index"))
            answers[idx] = button.text
        print("-".join(answers))
        # F34S-FFS3-56FGH-LKJ0-2E9D-440D-4Q0D-230S-D120



def visible_text_test_3():
    with (webdriver.Chrome() as browser):
        browser.get("https://parsinger.ru/selenium/5.9/6/index.html")
        time.sleep(2)

        chk_box = browser.find_element(By.ID, "myCheckbox")
        check_but = browser.find_element(By.TAG_NAME, "button")
        result = browser.find_element(By.ID, "result")

        WebDriverWait(browser, 30).until(EC.element_to_be_selected(chk_box))
        check_but.click()
        print(result.text)


def visible_text_test_4():
    with (webdriver.Chrome() as browser):
        browser.get("https://parsinger.ru/selenium/5.9/7/index.html")
        time.sleep(2)

        table = browser.find_elements(By.CLASS_NAME, 'container')
        for line in table:
            chk_box = line.find_element(By.TAG_NAME, "input")
            check_but = line.find_element(By.TAG_NAME, "button")
            WebDriverWait(browser, 30).until(EC.element_to_be_selected(chk_box))
            check_but.click()


        result = browser.find_element(By.ID, 'result')
        print(result.text)


def visible_text_test_5():
    with (webdriver.Chrome() as browser):
        browser.get('https://parsinger.ru/selenium/5.9/7/index.html')
        for el in browser.find_elements(By.CSS_SELECTOR, '.container'):
            if WebDriverWait(el, 10).until(EC.element_located_to_be_selected((By.CSS_SELECTOR, 'input'))):
                el.find_element(By.CSS_SELECTOR, 'button').click()

        print(browser.find_element(By.CSS_SELECTOR, '#result').text)



#####################++++++++++++++++
visible_text_test_5()