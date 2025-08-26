from bs4 import BeautifulSoup
import lxml
import html5lib
import requests
import json


def table_1():
    url = 'https://parsinger.ru/4.8/1/index.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')

    # Проходим по строкам таблицы, начиная со второй (индекс 1), так как первая строка - это заголовки
    for row in rows[1:]:
        columns = row.find_all('td') # Извлекаем ячейки текущей строки
        name = columns[0].text # Первая ячейка содержит имя
        age = columns[1].text # Вторая ячейка содержит возраст
        print(f'Имя: {name}, Возраст: {age}')


def table_2():
    url = 'https://parsinger.ru/4.8/2/index.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table')
    # Извлекаем заголовки таблицы, пройдясь по всем элементам th в таблице и получив их текст
    headers = [header.text for header in table.find_all('th')]
    # Извлекаем строки таблицы, начиная со второй (индекс 1), так как первая строка - это заголовки
    rows = table.find_all('tr')[1:]

    data = []
    # Проходим по каждой строке в таблице
    for row in rows:
        # Собираем данные строки в словарь, ключами которого являются заголовки, а значениями - данные ячеек
        row_data = dict(zip(headers, (cell.text for cell in row.find_all('td'))))
        # Добавляем словарь с данными строки в общий список
        data.append(row_data)

    for entry in data:
        print(entry)



def table_test_1():
    url = 'https://parsinger.ru/table/1/index.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')

    sum_count = 0
    num_mass = []
    for row in rows[1:]:
        columns = row.find_all('td')
        print(columns)
        for col in columns:
            #print(col.text)
            num_mass.append(float(col.text))

    print(len(num_mass))
    num_mass = set(num_mass)
    print(len(num_mass))

    for num in num_mass:
        sum_count += num

    print(sum_count)


def table_test_2():
    url = 'https://parsinger.ru/table/2/index.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')

    sum_count = 0
    num_mass = []
    for row in rows[1:]:
        columns = row.find_all('td')
        print(columns[0].text)
        sum_count += float(columns[0].text)

    print(sum_count)



def table_test_3():
    url = 'https://parsinger.ru/table/3/index.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')

    sum_count = 0
    for row in rows[1:]:
        columns = row.find_all('b')
        for col in columns:
            value = col.text
            print(f"{col} {value}")
            sum_count += float(value)

    print(sum_count)



def table_test_4():
    url = 'https://parsinger.ru/table/4/index.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')

    sum_count = 0
    for row in rows[1:]:
        columns = row.find_all('td', class_='green')
        for col in columns:
            value = col.text
            print(f"{col} {value}")
            sum_count += float(value)

    print(sum_count)



def table_test_5():
    url = 'https://parsinger.ru/table/5/index.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')

    sum_count = 0
    for row in rows[1:]:
        columns = row.find_all('td', class_='orange')
        blue = float(row.find_all('td')[-1].text)
        orange = 0
        for col in columns: orange = float(col.text)
        print(f"current row: {orange} x {blue} = {orange * blue}")
        sum_count += (orange * blue)

    print(f"sum_count: {sum_count}")


def table_test_6():
    keys_list = ['1 column', '2 column', '3 column', '4 column', '5 column', '6 column',
                 '7 column', '8 column', '9 column', '10 column', '11 column', '12 column',
                 '13 column', '14 column', '15 column']

    column_data_list = []

    url = 'https://parsinger.ru/table/5/index.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    for i in range(0,15):
        table = soup.find('table')
        rows = table.find_all('tr')
        column_mass = 0
        temp=0
        for row in rows[1:]:
            columns = row.find_all('td')
            for col in columns[i]: temp = float(col.text)
            #print(f"current row: {temp}")
            column_mass += float(temp)
        print(f"sum of {i} column = {column_mass}")
        column_data_list.append(round(column_mass, 3))

    print("\n pre-final list:")
    print(column_data_list)

    vocal = {}
    for i in range(0,15): vocal[keys_list[i]] = column_data_list[i]
    print(f"created vocal: \n {vocal}")



#parse info from 6 tables
def table_test_7():
    url = 'https://parsinger.ru/table/7/index.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    sum_count = 0
    table = soup.find_all('table') #all 6 tables
    for tb in table:
        rows = tb.find_all('tr')
        for row in rows[1:]:
            columns = row.find_all('td')
            for clm in columns:
                temp_num = int(clm.text)
                if temp_num % 3 == 0:
                    sum_count += temp_num
            print(f"Current summator: {sum_count}")


    print(sum_count)



def table_test_8():
    url = "https://parsinger.ru/table/8/index.html"
    response = requests.get(url=url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    soup = BeautifulSoup(response.text, "html.parser")
    total = sum([int(el.text) for el in soup.find_all(lambda tag: tag.has_attr('colspan') and tag.text.strip().isdigit())])
    print(total)


def table_test_json():
    url = "https://parsinger.ru/table/6/index.html"
    response = requests.get(url=url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    fl_price = 4000000 #Стоимость авто <= 4000000
    fl_year = 2005 #Год выпуска >= 2005
    fl_engin = "Бензиновый"

    table = soup.find('table')
    rows = table.find_all('tr')

    cars = []
    for row in rows[1:]:
        columns = row.find_all('td')
        if fl_price >= int(columns[7].text) and fl_year <= int(columns[1].text) and fl_engin == columns[4].text:
            print(columns[0].text, columns[1].text, columns[4].text, columns[7].text)
            car = {
                "Марка Авто": columns[0].text,
                "Год выпуска": int(columns[1].text),
                "Тип двигателя": columns[4].text,
                "Стоимость авто": int(columns[7].text.replace(',', ''))
            }
            cars.append(car)

    sorted_cars = sorted(cars, key=lambda x: x["Стоимость авто"])
    print(json.dumps(sorted_cars, indent=4, ensure_ascii=False))



##################
table_test_json()
