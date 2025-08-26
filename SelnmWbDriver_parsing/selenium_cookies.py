from pprint import pprint
from selenium import webdriver
import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def cook_1():
    with webdriver.Chrome() as browser:
        browser.get('https://ya.ru/')
        cookies = browser.get_cookies()
        pprint(cookies)


def cook_2():
    with webdriver.Chrome() as browser:
        browser.get('https://ya.ru/')
        cookies = browser.get_cookies()
        for cookie in cookies:
            print(cookie['name'], cookie['value'])


def get_cook_3():
    with webdriver.Chrome() as browser:
        browser.get('https://ya.ru/')
        #print(browser.get_cookie('_ym_uid')['expiry'])
        print(browser.get_cookie)


def get_cook_4():
    with webdriver.Chrome() as browser:
        url = "https://parsinger.ru/methods/3/index.html"
        browser.get(url)
        # Итерируемся по всем именам куков, в которых последнее число — чётное, и удаляем их.
        for i in range(0, 17, 2):
            print(browser.get_cookie)
            browser.delete_cookie(f"secret_cookie_{i}")
        time.sleep(30)


def get_cook_5():
    with webdriver.Chrome() as browser:
        url = "https://parsinger.ru/methods/3/index.html"
        browser.get(url)
        cookies = browser.get_cookies()
        for cook in cookies:
            print(cook['name'], cook['value'])


def delete_cook_6():
    with webdriver.Chrome() as browser:
        url = "https://parsinger.ru/methods/3/index.html"
        browser.get(url)

        print("Cookies before deletion:")
        pprint(browser.get_cookies())

        browser.delete_all_cookies()

        print("\nCookies after deletion:")
        pprint(browser.get_cookies())


def delete_cook_7():
    with webdriver.Chrome() as browser:
        url = "https://parsinger.ru/methods/3/index.html"
        browser.get(url)

        print("Cookies before deletion:")
        pprint(browser.get_cookies())

        browser.delete_cookie('domain')
        browser.delete_cookie('httpOnly')
        browser.delete_cookie('name')
        browser.delete_cookie('path')

        print("\nCookies after deletion:")
        pprint(browser.get_cookies())


def set_cook_8():
    cookie_dict = {
        'name': 'any_name_cookie',  # Любое имя для cookie
        'value': 'any_value_cookie',  # Любое значение для cookie
        'expiry': 2_000_000_000,  # Время жизни cookie в секундах
        'path': '/',  # Директория на сервере дял которой будут доступны cookie
        'domain': 'parsinger.ru',  # Информация о домене и поддомене для которых доступны cookie
        'secure': True,  # or False   # Сигнал браузера о том что передать cookie только по защищённому HTTPS
        'httpOnly': True,  # or False # Ограничивает достук к cookie по средствам API
        'sameSite': 'Strict',  # or lax or none # Ограничение на передачу cookie между сайтами
    }

    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/methods/4/index.html')
        browser.add_cookie(cookie_dict)
        pprint(browser.get_cookies())
        time.sleep(100)


def make_test_cook_1():
    with webdriver.Chrome() as browser:
        url = "https://parsinger.ru/selenium/6/6.3.1/index.html"
        browser.get(url)
        cookies = browser.get_cookies()
        #print(cookies)
        for cook in cookies:
            print(cook)
            if cook['name'] == 'token_22': print(f"\ntoken: {cook['value']}\n")


def make_test_cook_2():
    with webdriver.Chrome() as browser:
        song = ''
        url = "https://parsinger.ru/selenium/6/6.3/index.html"
        browser.get(url)
        cookies = browser.get_cookies()
        print(cookies)
        for cook in cookies:
            print(cook['name'])
            song = cook['name']

        browser.find_element(By.ID, "phraseInput").send_keys(song)
        browser.find_element(By.ID, "checkButton").click()
        time.sleep(3)
        print(browser.find_element(By.ID, "result").text)


def make_test_cook_3():
    with webdriver.Chrome() as browser:
        password = ''
        url = "https://parsinger.ru/selenium/6/6.3.2/index.html"
        browser.get(url)
        browser.delete_all_cookies()
        time.sleep(4)
        print(browser.find_element(By.ID, "password").text)



def make_test_cook_4():
    with webdriver.Chrome() as browser:

        cookie_dict_2 = {
            'name': 'secretKey',
            'value': 'selenium123'
        }

        url = "https://parsinger.ru/selenium/6/6.3.3/index.html"
        browser.get(url)
        browser.delete_all_cookies()
        time.sleep(1)
        browser.add_cookie(cookie_dict_2)
        time.sleep(1)
        browser.refresh()
        time.sleep(2)
        pprint(browser.get_cookies())
        time.sleep(2)
        result = browser.find_element(By.ID, 'password').text
        print(f"password: {result}")



def make_test_cook_5():
    with webdriver.Chrome() as browser:
        res = []
        url = "https://parsinger.ru/methods/3/index.html"
        browser.get(url)
        cookies = browser.get_cookies()
        i = 0
        for cook in cookies: res.append(int(cook['value']))
        print(res)
        print(sum(res))


def make_test_cook_6():
    with webdriver.Chrome() as browser:
        sum = 0
        url = "https://parsinger.ru/methods/3/index.html"
        browser.get(url)
        cookies = browser.get_cookies()
        keys = [f'secret_cookie_{i}' for i in range(0, 17, 2)]
        print(keys)
        for cook in cookies:
            for key in keys:
                if cook['name'] == key:
                    print(cook['name'], cook['value'])
                    sum += int(cook['value'])
        print(f"result: {sum}")


def make_test_cook_7():
    data_voc = {}
    link_muss = []
    with webdriver.Chrome() as browser:
        url = "https://parsinger.ru/methods/5/index.html"
        browser.get(url)
        links = browser.find_elements(By.CLASS_NAME, 'urls')
        for link in links:
            mark = link.find_element(By.TAG_NAME, 'a').get_attribute("href")
            print(mark)
            link_muss.append(mark)

    for link in link_muss:
        print(f"go to page: {link}")
        with webdriver.Chrome() as browser:
            browser.get(link)
            cookies = browser.get_cookies()
            for cook in cookies:
                print(cook['expiry'])
                data_voc[link] = cook['expiry']

    sort_data_voc = dict(sorted(data_voc.items(), key=lambda item: item[1], reverse=True))
    print("next results:")
    for k, v in sort_data_voc.items():
        print(f"{k} {v}")

    find_link = list(sort_data_voc.keys())[0]
    print(f"find site: {find_link}")
    with webdriver.Chrome() as browser:
        browser.get(find_link)
        result = browser.find_element(By.ID, 'result').text
        print(f"Final data: {result}")



def make_test_cook_8():
    age = ''
    skill_list = []
    cookies = {'name': 'KXIYO4xMrWh', 'value': 'ibyAZPfXAsPqptPaNyL'}
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/5.6/1/index.html')
        browser.delete_all_cookies()
        time.sleep(1)
        browser.add_cookie(cookies)
        time.sleep(1)
        browser.refresh()
        time.sleep(1)
        sooks = browser.get_cookies()
        for sook in sooks:
            print(sook['name'], sook['value'])  # или cookie['value']
        print(sook)
        time.sleep(20)
        age = browser.find_element(By.ID, 'age').text

        skills = browser.find_elements(By.TAG_NAME, 'li')
        for skill in skills:
            #print(skill.text)
            skill_list.append(skill.text)


    print(age)
    print(skill_list)
    print(len(skill_list))


#<span id="age">Age: 20</span>
#<ul id="skillsList"><li>Scala</li><li>Assembly (ASM)</li><li>PHP</li><li>TypeScript</li><li>Perl</li><li>C#</li><li>Kotlin</li><li>Python</li><li>Lua</li><li>R</li><li>C++</li><li>Swift</li><li>SQL</li><li>Ruby</li><li>MATLAB</li><li>Python</li><li>Go</li></ul>

###########++++++++++++++++++
make_test_cook_4()