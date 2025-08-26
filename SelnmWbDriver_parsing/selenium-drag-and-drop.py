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

from selenium.webdriver.support.color import Color


def drag_1():
    url = "https://parsinger.ru/selenium/5.10/1/index.html"
    with webdriver.Chrome() as browser:
        browser.get(url)

        draganddrop = browser.find_element(By.CLASS_NAME, "draganddrop")
        draganddrop_end = browser.find_element(By.CLASS_NAME, "draganddrop_end")

        ActionChains(browser).drag_and_drop(draganddrop, draganddrop_end).perform()
        time.sleep(5)


def drag_2():
    url = "https://parsinger.ru/selenium/5.10/5/index.html"
    with webdriver.Chrome() as browser:
        browser.get(url)
        slider = browser.find_element(By.ID, "volume")
        ActionChains(browser).click_and_hold(slider).move_by_offset(-300, 0).release().perform()

        current_offset = 10
        for i in range(1, 10):
            current_offset += 30
            ActionChains(browser).click_and_hold(slider).move_by_offset(current_offset, 0).release().perform()
            time.sleep(1.5)
            volume = browser.find_element(By.TAG_NAME, 'label').text
            print(f"Current iterration for offset: {current_offset} - volume: {volume}")

        time.sleep(5)


def drag_3():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/5.10/5/index.html')
        slider = browser.find_element(By.ID, 'volume')
        width = slider.size['width']
        offset = width / 100

        actions = ActionChains(browser)
        actions.click_and_hold(slider).perform()

        for _ in range(20):  # пример для 10 шагов
            actions.move_by_offset(offset, 0).perform()
            time.sleep(0.3)  # пауза для наглядности

        actions.release().perform()


def drag_4():
    with webdriver.Chrome() as driver:
        driver.get("https://parsinger.ru/selenium/5.10/7/index.html")
        element_to_drag = driver.find_element(By.ID, "click_and_hold")
        time.sleep(1)
        # Создание объекта ActionChains, инициализация операции перетаскивания элемента на 500 пикселей вправо
        # и выполнение цепочки действий
        ActionChains(driver).drag_and_drop_by_offset(element_to_drag, 700, 0).release().perform()

        time.sleep(10)


def drag_5():
    url = "https://parsinger.ru/selenium/5.10/7/index.html"

    with (webdriver.Chrome() as driver):
        # Устанавливаем неявное ожидание для всех элементов
        driver.implicitly_wait(10)

        # Переход на страницу
        driver.get(url)
        time.sleep(1)
        # Поиск элемента для перетаскивания и контейнера
        click_and_hold_element = driver.find_element(By.ID, "click_and_hold")
        container = driver.find_element(By.CLASS_NAME, "container")

        # Выполнение операции перетаскивания
        actions = ActionChains(driver)
        actions.click_and_hold(click_and_hold_element).move_to_element(container).release().perform()

        # Даем время для визуальной проверки (по желанию)
        time.sleep(5)



def drag_test_1():
    with webdriver.Chrome() as driver:
        driver.implicitly_wait(10)
        driver.get("https://parsinger.ru/selenium/5.10/9/index.html")

        square = driver.find_element(By.CSS_SELECTOR, "canvas")
        actions = ActionChains(driver)
        actions.click_and_hold(square).move_by_offset(100, 100).release().perform()

        time.sleep(5)


def drag_test_2():
    url = "https://parsinger.ru/draganddrop/1/index.html"
    with webdriver.Chrome() as browser:
        browser.get(url)
        time.sleep(1)
        drag_obj = browser.find_element(By.ID, "draggable")
        destination = browser.find_element(By.ID, "field2")

        ActionChains(browser).drag_and_drop(drag_obj, destination).perform()
        time.sleep(3)

        result = browser.find_element(By.ID, 'result').text
        print(result)


def drag_test_3():
    url = "https://parsinger.ru/draganddrop/3/index.html"
    with webdriver.Chrome() as browser:
        browser.get(url)
        time.sleep(1)

        obj = browser.find_element(By.ID, "block1")
        for point in browser.find_elements(By.CLASS_NAME, 'controlPoint'):
            ActionChains(browser).drag_and_drop(obj, point).perform()
            time.sleep(2)

        time.sleep(8)
        result = browser.find_element(By.ID, 'message').text
        print(result)


def drag_test_4():
    url = "https://parsinger.ru/selenium/5.10/2/index.html"
    with (webdriver.Chrome() as browser):
        browser.get(url)
        time.sleep(1)

        dest = browser.find_element(By.CLASS_NAME, "draganddrop_end")
        for i in range(1,11):
            temp_id = f"draganddrop{i}"
            square = browser.find_element(By.ID, temp_id)
            ActionChains(browser).drag_and_drop(square, dest).perform()
            time.sleep(2)

        time.sleep(8)
        result = browser.find_element(By.ID, 'message').text
        print(result)



def drag_test_5():
    url = "https://parsinger.ru/draganddrop/2/index.html"
    with (webdriver.Chrome() as browser):
        browser.get(url)
        time.sleep(1)

        ball = browser.find_element(By.ID, "draggable")
        for i in range(1,5):
            temp_id = f"box{i}"
            box = browser.find_element(By.ID, temp_id)
            ActionChains(browser).drag_and_drop(ball, box).perform()
            time.sleep(2)

        time.sleep(8)
        result = browser.find_element(By.ID, 'message').text
        print(result)



def drag_test_6():
    url = "https://parsinger.ru/selenium/5.10/3/index.html"
    with (webdriver.Chrome() as browser):
        browser.get(url)
        time.sleep(2)
        action = ActionChains(browser)

        for main_box in browser.find_elements(By.CSS_SELECTOR, "div[class^='draganddrop ui']"):
            target = main_box.find_element(By.XPATH, "following-sibling::div[@class='draganddrop_end']")
            action.drag_and_drop(main_box, target).perform()

        time.sleep(3)
        print(browser.find_element(By.ID, 'message').text)


def drag_test_7():
    url = "https://parsinger.ru/selenium/5.10/4/index.html"
    with (webdriver.Chrome() as browser):
        browser.get(url)
        time.sleep(2)

        color_mass = ['red', 'blue', 'green', 'black']

        for color in color_mass:
            print(f"start sort process for color: {color}")
            square_path = f"div[class^='basket_color {color} ui-droppable']"
            square_target = browser.find_element(By.CSS_SELECTOR, square_path)

            ball_path = f"div[class^='ball_color {color}_ball ui-draggable ui-draggable-handle']"
            i = 1
            for ball in browser.find_elements(By.CSS_SELECTOR, ball_path):
                ActionChains(browser).drag_and_drop(ball, square_target).perform()
                time.sleep(2)
                print(f"{color} ball number: {i} has been delivered")
                i += 1

            print('\n')

        time.sleep(3)
        print(browser.find_element(By.CLASS_NAME, 'message').text)



def drag_test_8():
    url = "https://parsinger.ru/selenium/5.10/8/index.html"
    with (webdriver.Chrome() as browser):
        browser.get(url)
        time.sleep(2)

        for i in range(1,9):
            column_path = f"range_{i*100}"
            ball_path = f"piece_{i*100}"
            column = browser.find_element(By.ID, column_path)
            ball = browser.find_element(By.ID, ball_path)

            ActionChains(browser).drag_and_drop(ball, column).perform()
            time.sleep(2)
            print(f"{i} ball delivered to column")

        time.sleep(3)
        print(browser.find_element(By.ID, 'message').text)


def drag_test_9():
    url = "https://parsinger.ru/selenium/5.10/6/index.html"
    with (webdriver.Chrome() as browser):
        browser.get(url)
        time.sleep(2)

        for row in browser.find_elements(By.CLASS_NAME, 'slider-row'):
            print(row.find_element(By.CLASS_NAME, 'label').text)
            start = row.find_element(By.CLASS_NAME, 'current-value').text
            print(f"start position: {start}")
            end = row.find_element(By.CLASS_NAME, 'target-value').text
            print(f"end position: {end}")

            point = row.find_element(By.CLASS_NAME, 'volume-slider')

            if int(end) < 50:
                count = 50 - int(end)
                for i in range(1,count+1): point.send_keys(Keys.ARROW_LEFT)
                print(f"point has been moved to {count} LEFT")

            if int(end) > 50:
                count = int(end) - 50
                for i in range(1,count+1): point.send_keys(Keys.ARROW_RIGHT)
                print(f"point has been moved to {count} RIGHT")

            time.sleep(2)

        time.sleep(3)
        print(browser.find_element(By.ID, 'message').text)



def drag_test_10():
    url = "https://parsinger.ru/draganddrop/4/index.html"
    with (webdriver.Chrome() as browser):
        browser.get(url)
        time.sleep(2)

        word = browser.find_element(By.ID, 'target-word').text
        print(f"target word: {word}")

        i=0
        for w in word:
            button = browser.find_element(By.XPATH, f"//div[text()='{w}']")
            cell = browser.find_element(By.XPATH, f"//div[@data-index='{i}']")

            ActionChains(browser).drag_and_drop(button, cell).perform()
            time.sleep(2)
            i+=1
            print(f"letter {w} pushed into cell: {i}")

        time.sleep(3)
        print(browser.find_element(By.ID, 'password-container').text)



#####################++++++++++++++++
drag_test_10()