import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as ChromiumService

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



def webdriver_test_1():
    with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as browser:
        browser.get("https://stepik.org/course/104774")
        time.sleep(5)


def webdriver_test_2():
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--headless=new')
    with webdriver.Chrome(options=options_chrome) as browser:
        url = 'https://stepik.org/course/104774'
        browser.get(url)
        a = browser.find_element(By.TAG_NAME, 'a')
        print(a.get_attribute('href'))


def webdriver_test_3():
    url = 'http://parsinger.ru/selenium/3/3.html'
    with webdriver.Chrome() as browser:
        browser.get(url)
        link = browser.find_element(By.CLASS_NAME, 'text')
        print(type(link))
        print(link)
        print(link.text)


def webdriver_test_4():
    url = 'http://parsinger.ru/selenium/3/3.html'
    with webdriver.Chrome() as browser:
        browser.get(url)
        links = browser.find_elements(By.CLASS_NAME, 'text')
        #print(links)
        for ln in links: print(ln)


def webdriver_test_5():
    url = 'http://parsinger.ru/selenium/3/3.html'
    with webdriver.Chrome() as browser:
        browser.get(url)
        p_elements = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
        for i, p_element in enumerate(p_elements):
            print(f"Текст второго p тега в {i + 1}-м div с классом 'text': {p_element.text}")


def webdriver_test_6():
    url = 'http://parsinger.ru/selenium/3/3.html'
    with webdriver.Chrome() as browser:
        browser.get(url)
        divs = browser.find_elements(By.CLASS_NAME, 'text')
        for i, div in enumerate(divs):
            first_p = div.find_element(By.XPATH, './p[1]')
            third_p = div.find_element(By.XPATH, './p[3]')
            print(f"Для div #{i + 1}, первый p: {first_p.text}, третий p: {third_p.text}")


def webdriver_test_7():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/1/1.html')
        input_form = browser.find_elements(By.CLASS_NAME, 'form')
        for input in input_form:
            input.send_keys('Text')
        button = browser.find_element(By.CLASS_NAME, 'btn')
        button.click()
        #<span id="result">1123581321345589144233377610987</span>
        result = browser.find_element(By.ID, 'result').text
        print(result)


def webdriver_test_8():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/2/2.html')
        find_link = browser.find_element(By.LINK_TEXT, '16243162441624')
        find_link.click()
        time.sleep(1)
        result = browser.find_element(By.ID, 'result').text
        print(result)


def webdriver_test_9():
    url = 'http://parsinger.ru/selenium/3/3.html'
    count_mass = 0
    with webdriver.Chrome() as browser:
        browser.get(url)
        divs = browser.find_elements(By.CLASS_NAME, 'text')
        for i, div in enumerate(divs):
            first_p = div.find_element(By.XPATH, './p[1]')
            second_p = div.find_element(By.XPATH, './p[2]')
            third_p = div.find_element(By.XPATH, './p[3]')
            temp = int(first_p.text) + int(second_p.text) + int(third_p.text)
            count_mass += temp
    print(f"Final result: {count_mass}")


def webdriver_test_10():
    url = 'http://parsinger.ru/selenium/3/3.html'
    count_mass = 0
    with webdriver.Chrome() as browser:
        browser.get(url)
        divs = browser.find_elements(By.CLASS_NAME, 'text')
        for i, div in enumerate(divs):
            second_p = div.find_element(By.XPATH, './p[2]')
            count_mass += int(second_p.text)
    print(f"Final result: {count_mass}")



def webdriver_test_11():
    url = 'https://parsinger.ru/selenium/4/4.html'
    result = ''
    with webdriver.Chrome() as browser:
        browser.get(url)
        boxes = browser.find_elements(By.CLASS_NAME, 'check')
        for i, box in enumerate(boxes):
            box.click()
            print(f"{i+1} box is clicked")
        button = browser.find_element(By.CLASS_NAME, 'btn')
        button.click()
        time.sleep(2)
        result = browser.find_element(By.ID, 'result').text
    print(result)



def webdriver_test_12():
    numbers = [1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 22, 23, 28, 29, 33, 34, 38,
               39, 43, 44, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 63, 64, 68, 69, 73,
               74, 78, 79, 83, 84, 88, 89, 91, 92, 97, 98, 101, 104, 108, 109, 113, 114, 118,
               119, 123, 124, 128, 129, 131, 132, 137, 138, 140, 141, 144, 145, 148, 149, 153,
               154, 158, 159, 163, 164, 165, 168, 169, 171, 172, 177, 178, 180, 181, 184, 185,
               187, 188, 189, 190, 192, 193, 194, 195, 197, 198, 199, 200, 204, 205, 206, 207,
               208, 209, 211, 212, 217, 218, 220, 221, 224, 225, 227, 228, 229, 230, 232, 233,
               234, 235, 237, 238, 239, 240, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255,
               256, 257, 258, 260, 261, 264, 265, 268, 269, 273, 274, 278, 279, 288, 289, 291,
               292, 293, 294, 295, 296, 297, 300, 301, 302, 303, 304, 305, 308, 309, 313, 314,
               318, 319, 328, 329, 331, 332, 339, 340, 341, 342, 343, 344, 345, 346, 348, 349,
               353, 354, 358, 359, 368, 369, 371, 372, 379, 380, 385, 386, 408, 409, 411, 412,
               419, 420, 425, 426, 428, 429, 433, 434, 438, 439, 444, 445, 446, 447, 448, 451,
               452, 459, 460, 465, 466, 467, 468, 469, 470, 472, 473, 474, 475, 477, 478, 479,
               480, 485, 486, 487, 488, 491, 492, 499, 500, 505, 506, 508, 509, 513, 514, 518, 519]
    url = 'https://parsinger.ru/selenium/5/5.html'
    result = ''
    with webdriver.Chrome() as browser:
        browser.get(url)
        boxes = browser.find_elements(By.CLASS_NAME, 'check')
        for i, box in enumerate(boxes):
            numb = box.get_attribute('value')
            if int(numb) in numbers:
                print(f"{numb} present in list and should be clicked")
                box.click()
                print(f"{i + 1} box is clicked")
            else:
                print(f"{numb} is not present in list")

        button = browser.find_element(By.CLASS_NAME, 'btn')
        button.click()
        time.sleep(2)
        result = browser.find_element(By.ID, 'result').text
    print(result)



def webdriver_test_13():
    count = 0
    result = ''
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/7/7.html')
        vals = browser.find_elements(By.TAG_NAME, 'option')
        for val in vals:
            count += int(val.text)
            #print(val.text)
        input = browser.find_element(By.ID, 'input_result')
        input.send_keys(count)
        button = browser.find_element(By.CLASS_NAME, 'btn')
        button.click()
        time.sleep(2)
        result = browser.find_element(By.ID, 'result').text

    print(f"Count: {count} Resut_code: {result}")



def webdriver_test_14():
    task_result = ((12434107696 * 3) * 2) + 1
    print(f"task result: {task_result}")
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/6/6.html')

        select = Select(browser.find_element(By.ID,"selectId"))
        time.sleep(1)
        select.select_by_visible_text(str(task_result))

        button = browser.find_element(By.CLASS_NAME, 'btn')
        button.click()
        time.sleep(2)
        result = browser.find_element(By.ID, 'result').text

    print(f"Resut_code: {result}")


def webdriver_test_15():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/3/3.2.1/index.html')
        button = browser.find_element(By.ID, 'clickButton')
        button.click()
        time.sleep(9)


def webdriver_test_16():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/3/3.2.2/index.html')
        name = browser.find_element(By.ID, 'codeInput')
        name.send_keys("Дрогон")
        button = browser.find_element(By.ID, 'clickButton')
        button.click()
        time.sleep(9)



def webdriver_test_17():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/3/3.2.3/index.html')
        start = browser.find_element(By.ID, 'showTextBtn')
        start.click()
        time.sleep(0.5)
        code = browser.find_element(By.ID, 'text1').text
        input = browser.find_element(By.ID, 'userInput')
        input.send_keys(code)
        button = browser.find_element(By.ID, 'checkBtn')
        button.click()
        result = browser.find_element(By.ID, 'text2').text
        print(result)


def webdriver_test_18():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/3/3.2.4/index.html')
        button = browser.find_element(By.ID, 'secret-key-button')
        button.click()
        time.sleep(1)
        button = browser.find_element(By.ID, 'secret-key-button').get_attribute("data")
        print(button)


def webdriver_test_19():
    count = 0
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/3/3.3.3/index.html')
        how_much = browser.find_elements(By.TAG_NAME, 'a')
        for how in how_much:
            check = how.get_attribute("stormtrooper")
            #print(check)
            if check.isnumeric():
                print(check)
                count += int(check)
        input = browser.find_element(By.ID, 'inputNumber')
        input.send_keys(str(count))
        button = browser.find_element(By.ID, 'checkBtn')
        button.click()
        time.sleep(1)
        result = browser.find_element(By.ID, 'feedbackMessage').text
    print(result)



def webdriver_test_20():
    url = 'https://parsinger.ru/selenium/3/3.3.2/index.html'
    with webdriver.Chrome() as browser:
        browser.get(url)
        blocks = browser.find_elements(By.CLASS_NAME, 'block')
        for block in blocks:
            block.find_element(By.CLASS_NAME, 'button').click()

        password = browser.find_element(By.TAG_NAME, 'password').text
        print(password)




############88888888888888
webdriver_test_20()

