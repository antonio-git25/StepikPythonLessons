from bs4 import BeautifulSoup
import lxml
import html5lib
import requests
import json
import csv
import os


def json_create_1():
    url = 'http://parsinger.ru/html/mouse/3/3_11.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    result_json = {
        'name': soup.find('p', id='p_header').text,
        'price': soup.find('span', id='price').text}

    with open('res.json-1', 'w', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)



def json_create_2():
    url = 'http://parsinger.ru/html/index3_page_1.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    result_json = []

    for item in soup.find_all('div', class_='item'):
        name = item.find('a', class_='name_item').text.strip()
        price = item.find('p', class_='price').text
        description = [value.text.split(':')[1].strip() for value in item.find_all('li')]

        result_json.append({
            'name': name,
            'brand': description[0],
            'type': description[1],
            'connect': description[2],
            'game': description[3],
            'price': price
        })

    print("Количество собранных товаров:", len(result_json))
    print("Пример первого товара:", result_json[0] if result_json else "Данных нет")

    with open('res.json-2', 'w', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)

    print("Проверьте файл res.json в директории:", os.getcwd())



def json_create_3():
    response = requests.get('http://parsinger.ru/html/watch/1/1_1.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    description = soup.find('ul', id='description').find_all('li')

    for li in description:
        print(li['id'])



def check_test_json_1():
    result_json = []
    for i in range (1,5):
        url = f"https://parsinger.ru/html/index4_page_{i}.html"
        print(f"Iteration={i} Current page: {url} \n")
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        for item in soup.find_all('div', class_='item'):
            name = item.find('a', class_='name_item').text.strip()
            price = item.find('p', class_='price').text
            description = [value.text.split(':')[1].strip() for value in item.find_all('li')]

            result_json.append({
                'Наименование': name,
                'Бренд': description[0],
                'Форм-фактор': description[1],
                'Ёмкость': description[2],
                'Объем буферной памяти': description[3],
                'Цена': price
            })

            print("Количество собранных товаров:", len(result_json))

    with open('res.json_test1', 'w', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)
    print("Проверьте файл res.json в директории:", os.getcwd())


def check_test_json_2():
    result_json = []
    for j in range(1,6):
        for i in range(1,5):
            schema_page = f"https://parsinger.ru/html/index{j}_page_{i}.html"
            print(schema_page)
            response = requests.get(url=schema_page)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')

            for item in soup.find_all('div', class_='item'):
                name = item.find('a', class_='name_item').text.strip()
                price = item.find('p', class_='price').text
                description_key = [value.text.split(':')[0].strip() for value in item.find_all('li')]
                description_val = [value.text.split(':')[1].strip() for value in item.find_all('li')]

                result_json.append({
                    'Наименование': name,
                    description_key[0]: description_val[0],
                    description_key[1]: description_val[1],
                    description_key[2]: description_val[2],
                    description_key[3]: description_val[3],
                    'Цена': price
                })

    print("Количество собранных товаров:", len(result_json))
    with open('res.json_test2', 'w', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)
    print("Проверьте файл res.json в директории:", os.getcwd())



def check_test_json_3():
    main_result_json = []
    for i in range (1,33):
        url = f"https://parsinger.ru/html/mobile/2/2_{i}.html"
        print(f"Iteration={i} Current page: {url} \n")
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        name = soup.find('p', id='p_header').text
        article = soup.find('p', class_='article').text.split(': ')[1]
        count = soup.find('span', id='in_stock').text.split(': ')[1]
        price = soup.find('span', id='price').text
        old_price = soup.find('span', id='old_price').text

        description = {tag['id'] : tag.text.split(':')[1].strip() for tag in soup.select('li')}

        main_result_json.append({
            "categories": "mobile",
            "name": name,
            "article": article,
            "description": description,
            "count": count,
            "price": price,
            "old_price": old_price,
            "link": url
            })

        print("Количество собранных товаров:", len(main_result_json))

    with open('res.json_test3', 'w', encoding='utf-8') as file:
        json.dump(main_result_json, file, indent=4, ensure_ascii=False)
    print("Проверьте файл res.json в директории:", os.getcwd())



def parsing_json_1():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url=url).json()
    print(len(response))
    for item in response:
        print(item["userId"], item["title"])


def parsing_json_2():
    url = 'http://parsinger.ru/downloads/get_json/res.json'
    response = requests.get(url=url).json()
    for item in response:
        print(item["description"]["brand"], item["description"]["model"])
        #print(item["description"])


def pars_j_test_1():
    url = 'http://parsinger.ru/downloads/get_json/res.json'
    response = requests.get(url=url).json()

    my_json = {}
    for item in response:
        if item['categories'] not in my_json:
            my_json[item['categories']] = int(item['count'])
        elif item['categories'] in my_json:
            my_json[item['categories']] += int(item['count'])

    print(my_json)


def pars_j_test_2():
    url = 'http://parsinger.ru/downloads/get_json/res.json'
    response = requests.get(url=url).json()

    my_json = {}
    for item in response:
        if item['categories'] not in my_json:
            my_json[item['categories']] = int(item['count']) * int(item['price'].split(' ')[0].strip())
        elif item['categories'] in my_json:
            my_json[item['categories']] += int(item['count']) * int(item['price'].split(' ')[0].strip())

    print(my_json)



def pars_j_test_3():
    url = 'https://parsinger.ru/4.6/1/res.json'
    response = requests.get(url=url).json()

    my_json = {}
    for item in response:
        if item['categories'] not in my_json:
            my_json[item['categories']] = int(item['article']) * int(item['description']['rating'])
        elif item['categories'] in my_json:
            my_json[item['categories']] += int(item['article']) * int(item['description']['rating'])

    print(my_json)



############
#pars_j_test_3()




url = "https://parsinger.ru/selenium/3/3.html"
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

list = soup.find_all('div', class_='text')
for ls in list:
    mark1 = ls.find_all('p')[0].text
    mark2 = ls.find_all('p')[1].text
    mark3 = ls.find_all('p')[2].text
    print(f"{mark1} {mark2} {mark3}")
    #print(ls.find_all('p'))


