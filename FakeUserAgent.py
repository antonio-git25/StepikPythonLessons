import json
import requests
from fake_useragent import UserAgent

def fake_test1():
    url = "http://31.130.149.237/ua_trainer"
    with open('list (1).json', 'r', encoding='utf-8') as file:
        agent = json.load(file)

    for i in agent.get("user_agents"):
        print(i)
        headers = {
            "User-Agent": i,
        }
        response = requests.get(url, headers=headers, verify=False)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            data = response.json()
            print(data)



def fake_test2():
    url = 'http://31.130.149.237/os-challenge/os'
    os_list = ["Mac OS X", "Windows", "Android", "Linux", "iOS"]
    num_mass = []
    for item in os_list:
        ua = UserAgent(os=item)
        headers = {"User-Agent": ua.random}
        print(headers)
        response = requests.get(url, headers=headers, verify=False)
        print(response.status_code)
        temp = response.text
        print(temp)
        print(f"{temp} pass: {temp[20:26]}")
        num_mass.append(temp[20:26])
    print(num_mass)
    sum = 0
    for num in num_mass:
        sum += int(num)
    print(f"sum: {sum}")


def fake_test3():
    combinations = {
        "valid_combinations": [
            {
                "browser": "Chrome",
                "os": "Windows",
            },
            {
                "browser": "Chrome",
                "os": "Mac OS X",
            },
            {
                "browser": "Chrome",
                "os": "Linux",
            },
            {
                "browser": "Safari",
                "os": "Mac OS X",
            },
            {
                "browser": "Firefox",
                "os": "Windows",
            },
            {
                "browser": "Firefox",
                "os": "Linux",
            },
            {
                "browser": "Firefox",
                "os": "Mac OS X",
            },
            {
                "browser": "Edge",
                "os": "Windows",
            },
        ],
    }

    url = 'http://31.130.149.237/browser-compatibility/browser-os-check'
    pwd = 0

    for combination in combinations["valid_combinations"]:
        ua = UserAgent(browsers=combination["browser"], os=combination["os"])
        headers = {"User-Agent": ua.random}
        response = requests.get(url=url, headers=headers, verify=False)
        print(response.status_code)
        print(response.text)
        response_data = response.json()
        pwd_part = response_data["part_of_password"]
        pwd += int(pwd_part)

    print(pwd)



def fake_test4():
    browser_os_combinations = [
        {"browser": ["Chrome"], "os": "Windows"},
        {"browser": ["Chrome"], "os": "Mac OS X"},
        {"browser": ["Chrome"], "os": "Linux"},
        {"browser": ["Chrome"], "os": "Android"},
        {"browser": ["Firefox"], "os": "Windows"},
        {"browser": ["Firefox"], "os": "Mac OS X"},
        {"browser": ["Firefox"], "os": "Linux"},
        {"browser": ["Firefox"], "os": "Android"},
        {"browser": ["Safari"], "os": "Mac OS X"},
        {"browser": ["Edge"], "os": "Windows"},
        {"browser": ["Opera"], "os": "Windows"},
        {"browser": ["Opera"], "os": "Mac OS X"},
        {"browser": ["Opera"], "os": "Linux"},
        {"browser": ["Opera"], "os": "Android"},
        {"browser": ["Mobile Safari"], "os": "iOS"},
        {"browser": ["Opera"], "os": "iOS"},
        {"browser": ["Chrome"], "os": "iOS"},
    ]

    url = 'http://31.130.149.237/right_combination/check'
    pwd = 0

    for combination in browser_os_combinations:
        ua = UserAgent(browsers=combination["browser"], os=combination["os"])
        headers = {"User-Agent": ua.random}
        #print(headers)
        response = requests.get(url=url, headers=headers, verify=False)
        if response.status_code == 200:
            print(response.status_code)
            print(response.text)
            response_data = response.json()
            pwd_part = response_data["part_of_password"]
            pwd += int(pwd_part)

    print(pwd)

#####################
fake_test4()