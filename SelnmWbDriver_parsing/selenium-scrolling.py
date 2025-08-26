from pprint import pprint
from selenium import webdriver
import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
import random
import string
from selenium.webdriver.common.action_chains import ActionChains


def scroll_1():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/scroll/1/')
        time.sleep(5)
        for i in range(1,10):
            browser.execute_script("window.scrollBy(0,5000)")
            time.sleep(3)
        print("scroll is completed")



def scroll_2():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/scroll/1/')
        height = browser.execute_script("return document.body.scrollHeight")
        time.sleep(2)
        print(height)



def scroll_3():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/scroll/1/')
        height = browser.execute_script("return window.innerHeight")
        width = browser.execute_script("return window.innerWidth")
        print(f'{width=}, {height=}')
        # Время посмотреть на открытую страницу
        time.sleep(3)



def scroll_4():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/scroll/1/')
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(6)



def scroll_test_1():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/6/6.5/index.html')
        element = browser.find_element(By.ID, 'target')
        time.sleep(1)
        browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        element.click()
        key = browser.find_element(By.ID, 'secret-key').text
        print(key)


def scroll_test_2():
    sum = 0
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/scroll/4/index.html')
        elements = browser.find_elements(By.CLASS_NAME, 'btn')
        result = browser.find_element(By.ID, 'result').text
        for elem in elements:
            browser.execute_script("return arguments[0].scrollIntoView(true);", elem)
            time.sleep(1)
            elem.click()
            result = browser.find_element(By.ID, 'result').text
            print(f"click button, result: {result}")
            sum += int(result)
        print(f"Completed! Final result: {sum}")



def scroll_test_3():
    sum = 0
    with webdriver.Chrome() as browser:
        count = 1
        browser.get('https://parsinger.ru/selenium/5.7/1/index.html')
        urans = browser.find_elements(By.CLASS_NAME, 'clickMe')
        for ura in urans:
            browser.execute_script("return arguments[0].scrollIntoView(true);", ura)
            time.sleep(0.4)
            ura.click()
            print(f"catch current piece of uran: {count}")
            count += 1
        time.sleep(1)
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(f"Completed! Final result: {alert_text}")



def scroll_test_4_1():
    sum = 0
    with (webdriver.Chrome() as browser):
        count = 1
        browser.get('https://parsinger.ru/selenium/7/7.2/index.html')

        list_input = []
        while True:
            #tags_input = browser.find_elements(By.TAG_NAME, 'input')
            tags_input = [x for x in browser.find_elements(By.TAG_NAME, 'input')]
            for input in tags_input:
                if input not in list_input:
                    rand = (''.join(random.choices(string.ascii_lowercase, k=10)))
                    time.sleep(0.4)
                    input.send_keys(Keys.TAB)
                    input.send_keys(rand)
                    input.send_keys(Keys.ENTER)
                    time.sleep(0.4)
                    input.send_keys(Keys.DOWN)
                    time.sleep(1)
                    list_input.append(input)

        time.sleep(20)


def scroll_test_4_2():
    with webdriver.Chrome() as browser:
        browser.get(r"https://parsinger.ru/selenium/7/7.2/index.html")
        list_input = []
        for i in range(100):
            inputs = browser.find_elements(By.CLASS_NAME, "interactive")
            for field in inputs:
                if field not in list_input:
                    field.send_keys(f'{i}')
                    field.send_keys(Keys.ENTER)
                    field.send_keys(Keys.DOWN)
                    list_input.append(field)
        time.sleep(5)
        res = browser.find_element(By.ID, "hidden-password").text
        print(res) #Пароль: Wasteland-Survivor-2077


def action_chairs_1():
    browser = webdriver.Chrome()
    browser.get("https://parsinger.ru/selenium/5.7/2/index.html")

    draggable = browser.find_element(By.ID, "draggable")
    actions = ActionChains(browser)

    for i in range(1,10):
        time.sleep(0.5)
        actions.drag_and_drop_by_offset(draggable, -100, 0).perform()
        time.sleep(0.5)
        actions.drag_and_drop_by_offset(draggable, 0, 100).perform()
        time.sleep(0.5)
        actions.drag_and_drop_by_offset(draggable, 100, 0).perform()
        time.sleep(0.5)
        actions.drag_and_drop_by_offset(draggable, 0, -100).perform()
        time.sleep(0.5)

    #browser.quit()


def action_chairs_1():
    browser = webdriver.Chrome()
    browser.get("https://parsinger.ru/selenium/7/7.3.1/index.html")

    object = browser.find_element(By.ID, 'draggable')
    actions = ActionChains(browser)
    actions.drag_and_drop_by_offset(object, 0, -180).perform()

    time.sleep(3)
    res = browser.find_element(By.ID, "password").text
    print(res)
    browser.quit()


def action_chairs_2():
    browser = webdriver.Chrome()
    browser.get("https://parsinger.ru/selenium/7/7.3.2/index.html")

    object = browser.find_element(By.ID, 'dblclick-area')
    actions = ActionChains(browser)
    actions.double_click(object).perform()

    time.sleep(3)
    res = browser.find_element(By.ID, "password").text
    print(res)
    browser.quit()


def action_chairs_3():
    browser = webdriver.Chrome()
    browser.get("https://parsinger.ru/selenium/7/7.3.3/index.html")

    actions = ActionChains(browser)

    time.sleep(2)
    actions.key_down(Keys.CONTROL) \
        .key_down(Keys.CONTROL) \
        .key_down(Keys.ALT) \
        .key_down(Keys.SHIFT) \
        .key_down('T').perform()

    time.sleep(1)
    actions.key_up(Keys.CONTROL) \
        .key_up(Keys.CONTROL) \
        .key_up(Keys.ALT) \
        .key_up(Keys.SHIFT) \
        .key_up('T').perform()

    time.sleep(3)
    res = browser.find_element(By.CSS_SELECTOR, 'span[key=access_code]').text
    print(res)
    browser.quit()


def action_chairs_4():
    browser = webdriver.Chrome()
    browser.get("https://parsinger.ru/selenium/7/7.3.4/index.html")

    object = browser.find_element(By.ID, 'context-area')
    actions = ActionChains(browser)

    actions.context_click(object).perform()
    time.sleep(0.5)

    #<div class="menu-item" data-action="get_password">Получить пароль</div>
    browser.find_element(By.CSS_SELECTOR, 'div[data-action=get_password]').click()

    time.sleep(3)
    #<span key="access_code">RightClick@2025</span>
    res = browser.find_element(By.CSS_SELECTOR, 'span[key=access_code]').text
    print(res)
    browser.quit()




def action_chairs_5():
    browser = webdriver.Chrome()
    browser.get("https://parsinger.ru/selenium/7/7.3.5/index.html")

    container_1 = browser.find_element(By.ID, 'scrollable-container-left')
    container_2 = browser.find_element(By.ID, 'scrollable-container-right')

    actions = ActionChains(browser)

    actions.click(container_1).send_keys(Keys.END).perform()
    time.sleep(2)
    actions.click(container_2).send_keys(Keys.END).perform()
    time.sleep(3)

    res = browser.find_element(By.CSS_SELECTOR, 'span[key=access_code]').text
    print(res)
    browser.quit()


def scroll_by_ammount():
    with webdriver.Chrome() as browser:
        browser.get("https://parsinger.ru/selenium/7/7.4.1/index.html")
        time.sleep(1)
        action = ActionChains(browser)
        action.scroll_by_amount(delta_x=1, delta_y=840).perform()
        time.sleep(5)
        countdown = browser.find_element(By.CLASS_NAME, "countdown").text.split("Код: ")[1].strip()
        action.scroll_by_amount(delta_x=1, delta_y=1340).perform()
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, '[placeholder = "Введите код"]').send_keys(countdown)
        time.sleep(2)
        browser.find_element(By.TAG_NAME, 'button').click()
        time.sleep(5)
        res = browser.find_element(By.ID, 'final-key').text
        print(res)


def grap_numbers():
    with webdriver.Chrome() as browser:
        browser.get("https://parsinger.ru/scroll/2/index.html")
        lines = browser.find_elements(By.CLASS_NAME, 'item')
        i=1
        data_mass=0
        for line in lines:
            line.find_element(By.CLASS_NAME, 'checkbox_class').click()
            time.sleep(0.4)
            id_mark = f"result{i}"
            data = line.find_element(By.ID, id_mark).text
            print(data)
            i+=1
            if data == '':
                continue
            else:
                data_mass+=int(data)
        print("completed!")
        print(data_mass)


def infinite_scroll_1():
    with webdriver.Chrome() as browser:
        total=0
        browser.get("https://parsinger.ru/infiniti_scroll_1/")
        div = browser.find_element(By.XPATH, "//*[@id='scroll-container']/div")
        for _ in range(15):
            ActionChains(browser).move_to_element(div).perform()
            time.sleep(0.5)
        button = browser.find_elements(By.CSS_SELECTOR, 'span[id]')
        for txt in button:
            txt = txt.text
            print(txt)
            if txt.isdigit():
                total += int(txt)
        print(total)


def infinite_scroll_5():
    with webdriver.Chrome() as browser:
        total=0
        browser.get("https://parsinger.ru/infiniti_scroll_3/")

        frames = browser.find_elements(By.CLASS_NAME, "main")
        for frame in frames:
            div = frame.find_element(By.XPATH, "//*[@id='scroll-container']/div")
            for _ in range(15):
                ActionChains(browser).move_to_element(div).perform()
                time.sleep(0.5)
            button = browser.find_elements(By.CSS_SELECTOR, 'span[id]')
            for txt in button:
                txt = txt.text
                print(txt)
                if txt.isdigit():
                    total += int(txt)
            print(total)







###############
infinite_scroll_5()