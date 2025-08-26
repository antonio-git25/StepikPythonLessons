import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as ChromiumService

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def back_navigation():
    with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as browser:
        browser.get("https://parsinger.ru/selenium/6/6.2/index.html")
        browser.find_element(By.TAG_NAME, 'a').click() #to page-2
        time.sleep(0.5)
        browser.find_element(By.TAG_NAME, 'a').click()  # to page-3
        time.sleep(0.5)
        browser.back()
        time.sleep(0.5)
        browser.back()
        time.sleep(0.5)
        browser.find_element(By.ID, 'getPasswordBtn').click()
        time.sleep(4)


def get_screen():
    with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as browser:
        browser.get("https://parsinger.ru/selenium/6/6.2.1/index.html")
        element = browser.find_element(By.ID, "this_pic").screenshot("logo.png")
        time.sleep(10)


def make_refresh():
    with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as browser:
        browser.get('https://parsinger.ru/methods/1/index.html')
        while True:
            res = browser.find_element(By.ID, 'result').text
            browser.refresh()
            if res.isdigit():
                print(res)
                break


def make_clear():
    with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as browser:
        browser.get('https://parsinger.ru/selenium/5.5/1/1.html')
        fields = browser.find_elements(By.CLASS_NAME, 'text-field')
        for field in fields:
            field.clear()
        browser.find_element(By.ID, 'checkButton').click()
        time.sleep(2)
        alert = browser.switch_to.alert
        print(alert.text)


def make_clear_fields():
    with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as browser:
        browser.get('https://parsinger.ru/selenium/5.5/2/1.html')
        fields = browser.find_elements(By.CLASS_NAME, 'text-field')
        for field in fields:
            if field.is_enabled():
                field.clear()

        browser.find_element(By.ID, 'checkButton').click()
        time.sleep(2)
        alert = browser.switch_to.alert
        print(alert.text)



def checkbox_fields_plus():
    summ = 0
    with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as browser:
        browser.get('https://parsinger.ru/selenium/5.5/3/1.html')
        objects = browser.find_elements(By.CLASS_NAME, 'parent')
        for obj in objects:
            box = obj.find_element(By.CLASS_NAME, 'checkbox')
            if box.is_selected():
                field = obj.find_element(By.TAG_NAME, 'textarea').text
                print(f"textarea: {field}")
                summ += int(field)
    print(summ)


def color_sync():
    with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as browser:
        browser.get('https://parsinger.ru/selenium/5.5/4/1.html')
        windows = browser.find_elements(By.CLASS_NAME, 'parent')
        for win in windows:
            inpt = win.find_element(By.XPATH, ".//textarea[@color='gray']").text
            win.find_element(By.XPATH, ".//textarea[@color='blue']").send_keys(inpt)
            win.find_element(By.XPATH, ".//textarea[@color='gray']").clear()
            win.find_element(By.TAG_NAME, "button").click()
            time.sleep(0.5)
        browser.find_element(By.ID, 'checkAll').click()
        time.sleep(15)


def color_code_hell():
    with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as browser:
        browser.get('https://parsinger.ru/selenium/5.5/5/1.html')
        objects = browser.find_elements(By.CSS_SELECTOR,'div[style]')[1:]
        for obj in objects:
            code = obj.find_element(By.TAG_NAME, "span").text
            print(code)
            select = Select(obj.find_element(By.TAG_NAME, "select"))
            time.sleep(0.3)
            select.select_by_visible_text(code)
            for c in obj.find_elements(By.CSS_SELECTOR,'button[data-hex]'):
                if c.get_attribute('data-hex').strip() == code: c.click()
            time.sleep(0.5)
            obj.find_element(By.XPATH, ".//input[@type='checkbox']").click()
            obj.find_element(By.XPATH, ".//input[@type='text']").send_keys(code)
            time.sleep(0.4)
            obj.find_element(By.XPATH, "//button[text()='Проверить']").click()

        browser.find_element(By.XPATH, "//button[text()='Проверить все элементы']").click()
        time.sleep(2)
        alert = browser.switch_to.alert
        print(alert.text)










#container > div:nth-child(1) > textarea:nth-child(1)
####################=============
color_code_hell()
