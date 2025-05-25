import requests
import time
from requests.adapters import HTTPAdapter


# URL для примеров
# url = "https://httpbin.org/user-agent"
# response = requests.get(url)
# print("HTTP-код статуса ответа:", response.status_code)
# print("Текстовое содержимое ответа:", response.text)
# print("Содержимое ответа в виде байтов:", response.content)
# json_response = response.json()
# print("Десериализованный JSON-ответ:", json_response)
# print("Заголовки HTTP:", response.headers)
# print("Исходный URL-адрес запроса:", response.url)
# print("Кодировка ответа:", response.encoding)
# print("Куки, возвращаемые сервером:", response.cookies)
# print("Запрос успешен (коды 2xx):", response.ok)
# print("Сообщение статуса HTTP:", response.reason)  https://parsinger.ru/video_downloads/videoplayback.mp4


def download_video():
    # Базовый URL для API фильмов
    url = 'https://parsinger.ru/video_downloads/videoplayback.mp4'
    response = requests.get(url=url, stream=True)

    with open('file.mp4', 'wb') as file:
        file.write(response.content)


def status_code_url():
    status_count = 0
    code_mass = []
    start = time.time()
    with requests.Session() as rs:
        for i in range(1,201):
            url_string = f'https://parsinger.ru/3.3/2/{i}.html'
            response = rs.head(url=url_string)
            code_mass.append(response.status_code)

    stop = time.time()
    #print(code_mass)
    for df in code_mass:
        status_count += int(df)

    print("Sum of codes: ", status_count)
    print("Time: ", str(stop - start))



def status_code_find():
    found_url = ''
    start = time.time()
    with requests.Session() as rs:
        for i in range(1,201):
            url_string = f'https://parsinger.ru/3.3/1/{i}.html'
            response = rs.head(url=url_string)
            if response.status_code == 200:
                found_url = url_string
            else:
                continue

    stop = time.time()
    call = requests.get(url=found_url)
    print("Found data: ", call.text)
    print("Time: ", str(stop - start))




def photo_size_scan(name_img):
    size_mass = []
    img_mass = name_img
    print("Size of mass: ", len(img_mass))
    for img in img_mass:
        photo_url = f'https://parsinger.ru/3.3/3/img/{img}'
        response = requests.head(url=photo_url)
        size_mass.append(int(response.headers.get('Content-Length')))

    size_mass.sort(reverse=True)
    print(f"max length: {size_mass[0]}")
    max_find = str(size_mass[0])

    for img in img_mass:
        photo_url = f'https://parsinger.ru/3.3/3/img/{img}'
        response = requests.head(url=photo_url)
        if max_find == str(response.headers.get('Content-Length')):
            print("Cool!, we've wind url of photo: ", photo_url)




def first_last_valid():
    mass_ok = []
    start = time.time()
    with requests.Session() as rs:
        for i in range(1,101):
            url_string = f'https://parsinger.ru/3.3/4/{i}.html'
            response = rs.head(url=url_string)
            if response.status_code == 200:
                mass_ok.append(url_string)
            else:
                continue

    stop = time.time()
    print("first available page: ", mass_ok[0])
    print("last available page: ", mass_ok[len(mass_ok)-1])



def find_image_code():
    for i in range(1, 161):
        url_string = f'https://parsinger.ru/img_download/img/ready/{i}.png'
        file_path = f'C:\\Users\\Antonio\\Pictures\\test_img\\image{i}.png'
        response = requests.get(url=url_string)
        with open(file_path, 'wb') as file:
            file.write(response.content)



def json_weather():
    gradus_mass = []
    data_line = ''
    response = requests.get("https://parsinger.ru/3.4/1/json_weather.json")
    data_list = response.json()
    for i in range(1,len(data_list)):
        temp_dict = dict(data_list[i])
        gradus = temp_dict['Температура воздуха']
        gradus_mass.append(int(gradus.rstrip('°C')))

    gradus_mass.sort(reverse=False)
    print(gradus_mass)
    print(gradus_mass[0])

    data_list_2 = response.json()
    for i in range(1, len(data_list_2)):
        temp_dict_2 = dict(data_list_2[i])
        if int(temp_dict_2['Температура воздуха'].rstrip('°C')) == gradus_mass[0]:
            data_line = temp_dict_2['Дата']
            print(data_line)




def get_posts():
    response = requests.get("https://parsinger.ru/3.4/3/dialog.json")
    lst = response.json()
    answer = {} # это словарь-счетчик юзеров и постов
    for dct in lst: # далее прохожу по каждому словарю в списке (lst - это dct['comments'])
        answer[dct['username']] = answer.get(dct['username'], 0) + 1 # добавляю юзера в мой словарь
        if not dct['comments']: # если это крайний случай - ничего не делаю
            continue
        else: # если не крайний, то ищу дальше, пока не нащупаю дно :)
            for key, value in get_posts(dct['comments']).items():
                answer[key] = answer.get(key, 0) + value

    print(answer)
    return answer


def pull_session():
    session = requests.Session()
    # Измерение времени выполнения запросов с переиспользованием соединения
    start_time = time.time()
    for _ in range(10):
        response = session.get('https://example.com')
    end_time = time.time()
    print(f'Время выполнения с переиспользованием соединения: {end_time - start_time}')


def pull_without_session():
    start_time = time.time()
    for _ in range(10):
        response = requests.get('https://example.com')
    end_time = time.time()
    print(f'Время выполнения с переиспользованием соединения: {end_time - start_time}')


def try_proxi():
    proxies_list = {
        'http': 'http://27.68.171.164:1080',
        'https': 'http://27.68.171.164:1080',
    }

    session = requests.Session()
    session.proxies.update(proxies_list)

    adapter = HTTPAdapter()
    session.mount('http://', adapter)
    session.mount('https://', adapter)



def adapter_call():
    # Создаем сессию
    session = requests.Session()

    # Создаем адаптер с конфигурацией по умолчанию
    adapter = HTTPAdapter(pool_connections=10, pool_maxsize=20)

    # Монтируем адаптер для HTTP и HTTPS
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    # Теперь можно делать запросы через эту сессию
    response = session.get('https://httpbin.org/get')
    print(response.status_code)  # 200






###################
try_proxi()











# try:
#     response = requests.get('https://httpstat.us/500')
#     response.raise_for_status()
# except requests.HTTPError as e:
#     print('HTTP ошибка: ', str(e))
#
#
# # Создание объекта сессии и Установка заголовков для сессии
# session = requests.Session()
# session.headers.update({'User-Agent': 'my_parser'})
# # Отправка запроса через объект сессии
# response = session.get('https://example.com')
# print(session.headers['User-Agent'])
