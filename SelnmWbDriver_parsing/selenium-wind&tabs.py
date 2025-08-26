from pprint import pprint
from selenium import webdriver
import time
import re
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
import random
import string
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
from unicodedata import digit


def switch_1():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/blank/modal/1/index.html')
        browser.find_element(By.ID, 'alert').click()
        time.sleep(2)
        # Если вы планируете что-то делать с этим событием, можно добавить его в переменную
        alert = browser.switch_to.alert
        print(alert.text)
        time.sleep(1)
        alert.accept()
        time.sleep(1)


def switch_2():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/blank/modal/1/index.html')
        browser.find_element(By.ID, 'prompt').click()
        time.sleep(2)
        prompt = browser.switch_to.alert
        time.sleep(1)
        prompt.send_keys('Введёный текст')
        time.sleep(2)
        prompt.accept()
        time.sleep(5)
        print(browser.find_element(By.ID, 'result').text)
        time.sleep(1)


def switch_3():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/blank/modal/1/index.html')
        browser.find_element(By.ID, 'confirm').click()
        time.sleep(2)
        confirm = browser.switch_to.alert
        confirm.dismiss()  # Замените на .dismiss() чтобы нажать на кнопку "Отмена"
        time.sleep(3)



def switch_test_1():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/8/8.3.1/index.html')

        browser.find_element(By.ID, 'alertButton').click()
        time.sleep(1)
        browser.switch_to.alert.accept()

        browser.find_element(By.ID, 'promptButton').click()
        time.sleep(1)
        promt = browser.switch_to.alert
        promt.send_keys("Alert")
        promt.accept()

        browser.find_element(By.ID, 'confirmButton').click()
        time.sleep(1)
        browser.switch_to.alert.accept()

        time.sleep(2)
        pwd = browser.find_element(By.ID, 'secretKey').text
        print(pwd)


#321968541687435564865796413874
def switch_test_2():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/5.8/1/index.html')
        time.sleep(1)

        for i in range(1, 101):
            idd = f"input[value='{i}']"
            browser.find_element(By.CSS_SELECTOR, idd).click()
            time.sleep(0.4)
            browser.switch_to.alert.accept()
            print(f"button {i} clicked and closed")
            time.sleep(0.5)
            code = browser.find_element(By.ID, "result").text
            if code != "":
                print(f"possible code: {code}")
                break

        print("completed!")


#PIN codes broot force!!!!!
def switch_test_3():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/5.8/2/index.html')
        time.sleep(1)

        pin_mass = []
        for i in range(1, 101):
            idd = f"input[value='{i}']"
            browser.find_element(By.CSS_SELECTOR, idd).click()
            time.sleep(0.3)
            alert = browser.switch_to.alert
            pin_mass.append(alert.text)
            print(f"current button {i} accepted with code: {alert.text}")
            alert.accept()

        print("Navigation is completed. Checked founded PINs")

        for pin in pin_mass:
           browser.find_element(By.ID, 'input').send_keys(pin)
           browser.find_element(By.ID, 'check').click()
           time.sleep(0.4)
           result = browser.find_element(By.ID, 'result').text
           if result != "Неверный пин-код":
               print(f"code is found({pin}): {result}")
               break



#PIN codes broot force!!!!!
def switch_test_4():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/5.8/3/index.html')
        time.sleep(1)
        pin_mass = []
        #buttons = browser.find_elements(By.CLASS_NAME, 'pins-container')
        buttons = browser.find_elements(By.TAG_NAME, "span")

        for button in buttons:
            print(button.text)
            pin_mass.append(button.text)
        print("Navigation is completed. Checked founded PINs")

        for pin in pin_mass:
           browser.find_element(By.ID, 'check').click()
           time.sleep(0.4)
           prompt = browser.switch_to.alert
           time.sleep(0.5)
           prompt.send_keys(pin)
           prompt.accept()
           time.sleep(0.5)

           result = browser.find_element(By.ID, 'result').text
           if result != "Неверный пин-код":
               print(f"code is found({pin}): {result}")
               break


def frame_1():
    res = ""
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/8/8.4.1/')

        # Переключаемся на iframe
        iframe_element = browser.find_element(By.TAG_NAME, 'iframe')
        browser.switch_to.frame(iframe_element)

        # Извлекаем HTML содержимое из iframe
        iframe_content = browser.page_source

        lst = re.findall(r"\*.\*", iframe_content)
        for symbol in lst:
            res = res + symbol.strip('*')

        print(res)


#the matrix
def frame_2():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/8/8.4.2/index.html')

        # Переключаемся на iframe
        for i in range(1,5):
            mark = f"frame{i}"
            iframe = browser.find_element(By.ID, mark)
            browser.switch_to.frame(iframe)
            iframe = browser.page_source
            time.sleep(2)
            if i != 4 and i != 5:
                browser.find_element(By.CLASS_NAME, 'unlock-button').click()
                browser.switch_to.default_content()
            else:
                code = browser.find_element(By.TAG_NAME, 'h2').text
                print(code)
                #<h2> ACCESS GRANTED YOUR PASSWORD: TH3 - M4TR1X - H4S - C0NTR0LL3D - Y0U </h2>

        time.sleep(5)



def frame_3():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/8/8.4.3/index.html')

        #Переключаемся на iframe
        for i in range(4):
            print(f"current itteration: {i}")
            iframe = browser.find_element(By.TAG_NAME, 'iframe')
            browser.switch_to.frame(iframe)
            iframe = browser.page_source
            time.sleep(2)
            browser.find_element(By.CLASS_NAME, 'button').click()

        result = browser.find_element(By.CLASS_NAME, "password-container").text
        print("Result is:", result)


def frame_4():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/5.8/5/index.html')
        num_mass = []
        #Переключаемся на iframe
        for i in range(1,10):
            print(f"current frame itteration: {i}")
            mark = f"iframe{i}"
            iframe = browser.find_element(By.ID, mark)
            browser.switch_to.frame(iframe)
            iframe = browser.page_source
            time.sleep(2)
            browser.find_element(By.TAG_NAME, 'button').click()
            time.sleep(0.3)
            number = browser.find_element(By.CSS_SELECTOR, "p[id='numberDisplay']").text
            print(f"get number: {number}")
            num_mass.append(number)
            browser.switch_to.default_content()
        print("completed get numbers \n")

        print("start code force: ")

        for num in num_mass:
            browser.find_element(By.ID, 'guessInput').clear()
            time.sleep(1)
            browser.find_element(By.ID, 'guessInput').send_keys(num)
            browser.find_element(By.ID, 'checkBtn').click()
            time.sleep(2)

            try:
                alert = browser.switch_to.alert
                print(alert.text)
                alert.accept()
                break
            except NoAlertPresentException:
                continue


def window_1():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/window_size/1/')
        browser.set_window_size(1400, 820)
        time.sleep(5)


def window_2():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/window_size/1/')
        browser.set_window_size(1200, 720)

        size = browser.get_window_size()
        print(size)

        print(browser.get_window_size().get('height'))
        print(browser.get_window_size()["height"])

        print(browser.get_window_size().get('width'))
        print(browser.get_window_size()["width"])


def window_test_1():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/8/8.2.1/index.html')
        browser.set_window_size(1200, 720)
        time.sleep(1)
        browser.find_element(By.ID, 'checkSizeBtn').click()
        time.sleep(0.5)
        result = browser.find_element(By.ID, 'message').text
        secret = browser.find_element(By.ID, 'secret').text
        print(result)
        print(secret)


def window_test_2():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/8/8.2.2/index.html')
        time.sleep(1)

        height = browser.get_window_size().get('height')
        width = browser.get_window_size().get('width')

        per = int(height) + int(width)
        browser.find_element(By.ID, 'answer').send_keys(str(per))
        browser.find_element(By.ID, "checkBtn").click()
        time.sleep(1)
        secret = browser.find_element(By.ID, 'resultMessage').text
        print(secret)



def window_test_3():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/window_size/1/')
        time.sleep(1)
        browser.set_window_size(1200, 720)
        time.sleep(10)

        width = browser.get_window_size().get('width')
        height = browser.get_window_size().get('height')

        width = int(width) + 555
        height = int(height) + 555
        browser.set_window_size(str(width), str(height))
        time.sleep(3)
        secret = browser.find_element(By.ID, 'result').text
        print(secret)


def tabs_1():
    with webdriver.Chrome() as browser:
        browser.get("https://ya.ru")
        browser.execute_script('window.open("https://icloud.com", "_blank");')
        time.sleep(5)
        print(browser.title)
        browser.get("https:google.com")
        time.sleep(5)
        print(browser.title)
        time.sleep(5)


def tabs_2():
    with webdriver.Chrome() as browser:
        result = []
        browser.get('http://parsinger.ru/blank/2/1.html')
        time.sleep(1)
        browser.switch_to.new_window("tab")
        browser.get("http://parsinger.ru/blank/2/2.html")
        time.sleep(1)
        browser.switch_to.new_window("tab")
        browser.get("http://parsinger.ru/blank/2/3.html")
        time.sleep(1)
        browser.switch_to.new_window("tab")
        browser.get("http://parsinger.ru/blank/2/4.html")
        time.sleep(2)
        desc_mass = browser.window_handles
        print(desc_mass)

        for desc in desc_mass:
            browser.switch_to.window(desc)
            time.sleep(2)
            print(browser.title)


def tabs_3():
    with webdriver.Chrome() as browser:
        result = []
        browser.get('http://parsinger.ru/blank/2/1.html')
        time.sleep(1)
        browser.switch_to.new_window("window")
        browser.get("http://parsinger.ru/blank/2/2.html")
        time.sleep(1)
        browser.switch_to.new_window("window")
        browser.get("http://parsinger.ru/blank/2/3.html")
        time.sleep(1)
        browser.switch_to.new_window("window")
        browser.get("http://parsinger.ru/blank/2/4.html")
        time.sleep(2)
        desc_mass = browser.window_handles
        print(desc_mass)

        for desc in desc_mass:
            browser.switch_to.window(desc)
            time.sleep(2)
            print(browser.title)


def tabs_4():
    with webdriver.Chrome() as browser:
        # Вместо вкладки data; будет вкладка в которой будет загружен степик
        browser.get("https://stepik.org/course/104774/promo")
        browser.switch_to.new_window("tab")
        browser.get("http://parsinger.ru/blank/2/1.html")
        browser.switch_to.new_window("tab")
        browser.get("http://parsinger.ru/blank/2/2.html")
        browser.switch_to.new_window("tab")
        browser.get("http://parsinger.ru/blank/2/3.html")
        browser.switch_to.new_window("tab")
        browser.get("http://parsinger.ru/blank/2/4.html")
        time.sleep(2)
        for x in reversed(range(len(browser.window_handles))):  # reversed(range(len(browser.window_handles))) Для итерирования
            browser.switch_to.window(browser.window_handles[x])  # от последней вкладки к первой
            for y in browser.find_elements(By.CLASS_NAME, 'check'):
                y.click()
            time.sleep(2)


def tabs_5():
    with webdriver.Chrome() as browser:
        time.sleep(1)
        browser.execute_script('window.open("http://parsinger.ru/blank/0/1.html", "_blank1");')
        browser.execute_script('window.open("http://parsinger.ru/blank/0/2.html", "_blank2");')
        browser.execute_script('window.open("http://parsinger.ru/blank/0/3.html", "_blank3");')
        browser.execute_script('window.open("http://parsinger.ru/blank/0/4.html", "_blank4");')
        browser.execute_script('window.open("http://parsinger.ru/blank/0/5.html", "_blank5");')
        browser.execute_script('window.open("http://parsinger.ru/blank/0/6.html", "_blank6");')

        for x in range(len(browser.window_handles)):
            browser.switch_to.window(browser.window_handles[x])
            time.sleep(1)
            print(browser.execute_script("return document.title;"), browser.window_handles[x])


def tabs_test_1():
    with webdriver.Chrome() as browser:
        browser.get("about:blank")

        browser.switch_to.new_window("tab")
        browser.get("https://parsinger.ru/selenium/8/8.1/site1/")
        time.sleep(1)
        title_1 = browser.title
        print(f"title1: {title_1}")

        browser.switch_to.new_window("tab")
        browser.get("https://parsinger.ru/selenium/8/8.1/site2/")
        time.sleep(1)
        title_2 = browser.title
        print(f"title2: {title_2}")

        new_title_1 = ''
        for i in title_1:
            if i not in ('4','3','9'):
                new_title_1 += i
        print(f"new title1: {new_title_1}")

        new_title_2 = ''
        for i in title_2:
            if i not in ('7', '8', '0'):
                new_title_2 += i
        print(f"new title2: {new_title_2}")

        result = int(new_title_1) + int(new_title_2)
        print(f"final result: {result}")


def tabs_test_2():
    final_mass = 0
    link_mass = []
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/8/8.1.2/index.html')
        time.sleep(1)
        links = browser.find_elements(By.TAG_NAME, 'a')

        for link in links:
            url = link.get_attribute('href')
            print(url)
            link_mass.append(url)

        for link in link_mass:
            print(link)
            browser.switch_to.new_window("tab")
            time.sleep(1)
            browser.get(link)
            time.sleep(6)
            nums = browser.find_elements(By.CLASS_NAME, 'number')
            for n in nums:
                print(n.text)
                final_mass += int(n.text)

        print("get back to first window...")
        desct = browser.window_handles
        browser.switch_to.window(desct[0])
        browser.find_element(By.ID, 'sumInput').send_keys(str(final_mass))
        browser.find_element(By.ID, 'checkButton').click()
        time.sleep(2)
        pwd = browser.find_element(By.ID, 'passwordDisplay').text
        print(pwd)


def tabs_test_3():
    final_mass = 0
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/blank/3/index.html')
        time.sleep(1)
        buttons = browser.find_elements(By.TAG_NAME, 'input')

        for but in buttons:
            but.click()
            time.sleep(1)

        hands = browser.window_handles
        for hand in hands:
            print(f"current hand: {hand}")
            browser.switch_to.window(hand)
            code = browser.title
            print(f"title: {browser.title}")
            if code.isdigit():
                final_mass += int(code)
                print(f"number {code} is added into final mass")

        print('\n')
        print(f"final result: {final_mass}")



def tabs_test_4():
    sites = ['http://parsinger.ru/blank/1/1.html',
             'http://parsinger.ru/blank/1/2.html',
             'http://parsinger.ru/blank/1/3.html',
             'http://parsinger.ru/blank/1/4.html',
             'http://parsinger.ru/blank/1/5.html',
             'http://parsinger.ru/blank/1/6.html']
    final_mass = 0
    with webdriver.Chrome() as browser:
        for site in sites:
            browser.switch_to.new_window("tab")
            browser.get(site)
            time.sleep(2)
            #make some steps
            browser.find_element(By.TAG_NAME, 'input').click()
            time.sleep(0.5)
            code = browser.find_element(By.ID, 'result').text
            print(f"current code: {code}")
            sqr = math.sqrt(int(code))
            print(f"current square: {sqr}")
            final_mass += sqr

        #final
        final_mass = round(final_mass, 9)
        print(f"final result: {final_mass}")




#####################++++++++++++++++
tabs_test_4()