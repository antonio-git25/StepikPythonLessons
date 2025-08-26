import requests

def fetch_1():
    url = "http://31.130.149.237/api/v1/ajax/GetSum"
    # Словарь с параметрами из исходной ссылки
    data = {
        'GiveName': 'RUB',
        'GetName': 'USD',
        'Sum': 5000000,
        'Direction': 0
    }
    response = requests.get(url=url, params=data)
    print(response.json())



def fetch_2():
    headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0',
               'X-Requested-With': 'XMLHttpRequest', }
    url = 'https://cbr.ru/Queries/AjaxDataSource/112805'
    data_dollar = {
        'DT': '',
        'val_id': 'R01235',
        '_': '1667219511852'
    }
    data_euro = {
        'DT': '',
        'val_id': 'R01239',
        '_': '1667219511853'
    }
    response_dollar = requests.get(url=url, headers=headers, params=data_dollar).json()[-1]
    response_euro = requests.get(url=url, headers=headers, params=data_euro).json()[-1]

    print(f'Дата: {response_dollar["data"][:10]}')
    print(f'Курс USD: {response_dollar["curs"]} рублей')
    print(f'Курс EUR: {response_euro["curs"]} рублей')


def fetch_3():
    url = "http://31.130.149.237/api/v1/ajax/GetSum"
    data = {
        'GiveName': 'JPY',
        'GetName': 'DOGE',
        'Sum': 51284.43,
        'Direction': 0
    }
    response = requests.get(url=url, params=data)
    print(response.json())


def fetch_4():
    url = "http://31.130.149.237/api/v1/ajax/GetSum"
    # data = {
    #     'GiveName': 'JPY',
    #     'GetName': 'DOGE',
    #     'Sum': 51284.43,
    #     'Direction': 0
    # }

    amounts_per_give_currency = {
        "USD": 150, "EUR": 120, "RUB": 20000, "BYN": 50, "JPY": 50000,
        "GBP": 250, "CAD": 1000, "BTC": 0.01, "ETH": 0.5, "SOL": 10,
        "USDT": 150, "ADA": 300, "DOGE": 5000, "XRP": 1000, "BNB": 1,
        "USDC": 150, "TRX": 10000
    }

    final_sum = 0
    # response = requests.get(url=url, params=data)
    # getSum = response.json()['getSum']
    # print(response.json()['getSum'])

    for k, v in amounts_per_give_currency.items():
        format_list = list(amounts_per_give_currency.keys())
        current_list = []
        for form in format_list:
            if form != k: current_list.append(form)
        print(f"For current line:  key: {k} => value: {v}")
        print(f"{v} {k} need convert to next currencies: {current_list}")

        for call in current_list:
            data = {
            'GiveName': k,
            'GetName': call,
            'Sum': v,
            'Direction': 0}

            response = requests.get(url=url, params=data)
            getSum = response.json()['getSum']
            final_sum += getSum

        print(f"For first itteration: {final_sum} \n")


###############
fetch_4()


