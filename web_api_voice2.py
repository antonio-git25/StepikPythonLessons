import requests


def proxy_test_1():
    # Функция для выполнения запроса с использованием прокси
    def make_request(url, proxy):
        try:
            response = requests.get(url=url, proxies=proxy)
            print(response.json())
        except Exception as e:
            print(f"Ошибка: {e}")

    url = 'http://httpbin.org/ip'

    # Прокси для HTTP и HTTPS
    proxy_http_https = {
        'http': 'http://45.12.30.88:80',
        'https': 'https://45.12.30.88:80',
    }
    make_request(url, proxy_http_https)

    # Прокси для SOCKS4
    proxy_socks4 = {
        'http': 'socks4://45.12.30.88:80',
        'https': 'socks4://45.12.30.88:80',
    }
    make_request(url, proxy_socks4)

    # Прокси для SOCKS5
    proxy_socks5 = {
        'http': 'socks5://45.12.30.88:80',
        'https': 'socks5://45.12.30.88:80',
    }
    make_request(url, proxy_socks5)

    # # Если ваш прокси-сервер требует логин и пароль, укажите их прямо в URL прокси:
    # # Прокси с авторизацией
    # proxy_with_auth = {
    #     'http': 'socks5://login:password@103.177.45.3:8000',
    #     'https': 'socks5://login:password@103.177.45.3:8000',
    # }
    # make_request(url, proxy_with_auth)


def proxy_test_2():
    url = 'http://httpbin.org/ip'

    # Формируем словарь с прокси для http и https
    proxy = {
             'http': f'http://104.27.55.88:80',
             'https': f'https://104.27.55.88:80'
            }
    try:
        # Выполняем GET-запрос с использованием выбранного прокси
        response = requests.get(url=url, proxies=proxy)
        # Выводим результат в случае успешного подключения
        print(response.json(), 'Success connection')

    except Exception as _ex:
        print(_ex)


def response_code():
    url = 'https://parsinger.ru/html/watch/1/1_2.html'
    response = requests.get(url)
    print("Текущая кодировка:", response.encoding)

    response.encoding = 'utf-8'
    print("Пример текста с авто-определённой кодировкой:")
    print(response.text)


def crash_json():
    response = requests.get(url='https://api.github.com/eventsСЛОМАЕМ_ССЫЛКУ')
    print(f"JSON ответа: {response.json()}")
    print(f"Код статуса(.status_code): {response.status_code}")
    print(f"Метод для проверки ошибок(raise_for_status): {response.raise_for_status}")
    print(f"Успешность запроса(.ok): {response.ok}")

    print('\n')
    if response.status_code == 200:
        print("Запрос успешно выполнен")
    else:
        print(f"Произошла ошибка: {response.status_code}")



########################
proxy_test_1()