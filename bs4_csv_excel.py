from bs4 import BeautifulSoup
import lxml
import html5lib
import requests
import json
import csv


def example_csv():
    lst = ['one', 'two', 'three']
    with open('res.csv', 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(lst)


def parsing_to_csv_1():
    url = 'http://parsinger.ru/html/mouse/3/3_11.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    name = soup.find('p', id='p_header').text
    article = soup.find('p', class_='article').text.split(': ')[1]
    brand = soup.find('li', id='brand').text.split(': ')[1]
    model = soup.find('li', id='model').text.split(': ')[1]
    type = soup.find('li', id='type').text.split(': ')[1]
    purpose = soup.find('li', id='purpose').text.split(': ')[1]
    light = soup.find('li', id='light').text.split(': ')[1]
    size = soup.find('li', id='size').text.split(': ')[1]
    dpi = soup.find('li', id='dpi').text.split(': ')[1]
    site = soup.find('li', id='site').text.split(': ')[1]
    in_stock = soup.find('span', id='in_stock').text.split(': ')[1]
    price = soup.find('span', id='price').text.split(' ')[0]

    data = [
        name, article, brand, model,
        type, purpose, light, size, dpi,
        site, in_stock, price
    ]
    header = [
        'Наименование', 'Артикул', 'Бренд', 'Модель',
        'Тип', 'Игровая', 'Размер', 'Разрешение', 'Подсветка',
        'Сайт производителя', 'В наличии', 'Цена'
    ]

    with open('res2.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)
        writer.writerow(data)


def parsing_to_csv_3():
    with open('res3.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([
            'Наименование', 'Цена', 'Бренд', 'Тип', 'Подключение', 'Игровая'])

    url = 'http://parsinger.ru/html/index3_page_2.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
    price = [x.text for x in soup.find_all('p', class_='price')]

    # Открываем файл для дополнительной записи данных
    with open('res3.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for item, price, descr in zip(name, price, description):
            # Формируем строку для записи
            flatten = item, price, *[x.split(':')[1].strip() for x in descr if x]
            writer.writerow(flatten)

    print('Файл res3.csv создан')



def parsing_to_csv_4():
    url = 'https://parsinger.ru/html/index4_page_1.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    pagen = soup.find('div', class_='pagen').find_all('a')
    list_link = []
    schema = 'http://parsinger.ru/html/'

    for link in pagen: list_link.append(f"{schema}{link['href']}")

    with open('res4.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([
            'Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объем буферной памяти', 'Цена'])

    for list in list_link:
        print(list)
        response = requests.get(url=list)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
        print(name)
        description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
        print(description)
        price = [x.text for x in soup.find_all('p', class_='price')]
        print(price)

        # Открываем файл для дополнительной записи данных
        with open('res4.csv', 'a', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for item, descr, price in zip(name, description, price):
                # Формируем строку для записи
                flatten = item, *[x.split(':')[1].strip() for x in descr if x], price
                writer.writerow(flatten)

    print('Файл res4.csv создан')



def parsing_to_csv_5():
    main_list = []
    for j in range(32):
        url = f"https://parsinger.ru/html/watch/1/1_{j + 1}.html"
        print(url)
        main_list.append(url)

    print(len(main_list))

    with open('res5.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([
        'Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана', 'Материал корпуса',
        'Материал браслета', 'Размер', 'Сайт производителя', 'Наличие', 'Цена', 'Старая цена', 'Ссылка на карточку с товаром'])

    for list in main_list:
        print(list)
        response = requests.get(url=list)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        name = soup.find('p', id='p_header').text
        article = soup.find('p', class_='article').text.split(': ')[1]
        brand = soup.find('li', id='brand').text.split(': ')[1]
        model = soup.find('li', id='model').text.split(': ')[1]
        type = soup.find('li', id='type').text.split(': ')[1]
        display = soup.find('li', id='display').text.split(': ')[1]
        material_frame = soup.find('li', id='material_frame').text.split(': ')[1]
        material_tail = soup.find('li', id='material_bracer').text.split(': ')[1]
        size = soup.find('li', id='size').text.split(': ')[1]
        site = soup.find('li', id='site').text.split(': ')[1]
        in_stock = soup.find('span', id='in_stock').text.split(': ')[1]
        price = soup.find('span', id='price').text
        old_price = soup.find('span', id='old_price').text
        link = list

        data = [name, article, brand, model, type, display, material_frame, material_tail,
                size, site, in_stock, price, old_price, link]

        with open('res5.csv', 'a', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(data)

    print('Файл res5.csv создан')



def parsing_to_csv_6():
    for j in range(1,6):
        for i in range(1,5):
            schema_page = f"https://parsinger.ru/html/index{j}_page_{i}.html"
            print(schema_page)
            response = requests.get(url=schema_page)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')

            name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
            description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
            price = [x.text for x in soup.find_all('p', class_='price')]

            # Открываем файл для дополнительной записи данных
            with open('res6.csv', 'a', encoding='utf-8-sig', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                for item, price, descr in zip(name, price, description):
                    # Формируем строку для записи
                    flatten = item, *[x.split(':')[1].strip() for x in descr if x], price
                    writer.writerow(flatten)

        print(f"Block {j} is completed")

    print('Файл res6.csv создан')


############
parsing_to_csv_6()