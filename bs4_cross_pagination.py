from bs4 import BeautifulSoup
import lxml
import html5lib
import requests


def cross_1():
    url = 'http://parsinger.ru/html/index1_page_1.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    divs = soup.find('div', 'description').find_all('li')
    # Проходимся по списку найденных элементов <li> и выводим их текстовое содержимое
    for txt in divs:
        print(txt.text)
    """
    Бренд: Jet
    Тип: умные часы
    Материал корпуса: пластик
    Технология экрана: Монохромный
    """


def cross_2():
    url = 'https://parsinger.ru/4.3/5/index.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    price_mass = []
    volume_mass = []

    prices = soup.find_all('div', class_='book-card')
    for price in prices:
        price_temp = price.find('p', class_='count price').get_text()
        price_int = int(''.join(x for x in price_temp.strip() if x.isdigit()))
        print(price_temp, price_int)
        price_mass.append(price_int/100)

    volume = soup.find_all('div', class_='book-card')
    for vol in volume:
        volume_temp = vol.find('p', class_='count stock').get_text()
        volume_int = int(''.join(x for x in volume_temp.strip() if x.isdigit()))
        print(volume_temp, volume_int)
        volume_mass.append(volume_int)

    print(price_mass)
    print(volume_mass)

    result = []
    for i in range(len(price_mass)):
        result.append(price_mass[i] * volume_mass[i])

    print(result)

    sum = 0
    for res in result:
        sum += res

    print(sum)



def cross_3():
    url = 'https://parsinger.ru/4.3/5/index.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    total_price = 0

    book_cards = soup.find_all("div", class_="book-card")
    for book in book_cards:
        book_price = book.find("p", class_="count price").text
        formated_book_price = float(book_price.split("$")[-1])

        book_count = book.find("p", class_="count stock").text
        formated_book_count = int(book_count.split(": ")[-1])

        total_price += formated_book_price * formated_book_count

    return total_price


#Парсинг стоимости часов
def cross_4():
    url = 'https://parsinger.ru/html/index1_page_1.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    total_price = 0

    clock = soup.find_all("div", class_="item")
    for part in clock:
        temp_price = part.find("p", class_="price").text
        price_int = int(''.join(x for x in temp_price.strip() if x.isdigit()))
        print(temp_price, price_int)
        total_price += price_int

    print(f"Final price: {total_price}")



#Расчёт скидки
def cross_5():
    url = 'https://parsinger.ru/html/hdd/4/4_1.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    current_price = soup.find('span', id='price').get_text()
    old_price = soup.find('span', id='old_price').get_text()

    new_num = int(''.join(x for x in current_price.strip() if x.isdigit()))
    old_num = int(''.join(x for x in old_price.strip() if x.isdigit()))
    discount = (old_num - new_num) * 100 / old_num

    print(discount)


def pagination_1():
    url = 'http://parsinger.ru/html/index1_page_3.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    pagen = soup.find('div', class_='pagen').find_all('a')
    list_link = []
    schema = 'http://parsinger.ru/html/'

    for link in pagen: list_link.append(f"{schema}{link['href']}")
    for list in list_link: print(list)


def pagination_2():
    url = 'http://parsinger.ru/html/index1_page_3.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    schema = 'http://parsinger.ru/html/'
    pagen = [link.text for link in soup.find('div', class_='pagen').find_all('a')][-1]
    print(pagen)


def pagination_3():
    url = 'https://parsinger.ru/html/index3_page_1.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    pagen = soup.find('div', class_='pagen').find_all('a')
    list_link = []
    schema = 'http://parsinger.ru/html/'
    global_list = []
    for link in pagen: list_link.append(f"{schema}{link['href']}")

    for list in list_link:
        print(list)
        response = requests.get(url=list)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        inner_list = []
        stuff_soup = soup.find_all('div', class_='item')
        for stuff in stuff_soup:
            name = stuff.find('a', class_='name_item').text
            #inner_list.append(name.strip())
            inner_list.append(name)

        #print(inner_list)
        global_list.append(inner_list)

    print(global_list)


def pagination_4():
    url = 'https://parsinger.ru/html/index3_page_1.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    #собираем линки всех страниц
    pagen = soup.find('div', class_='pagen').find_all('a')
    list_link = []
    schema = 'http://parsinger.ru/html/'
    global_list = []
    for link in pagen: list_link.append(f"{schema}{link['href']}")

    #работаем с каждой страницей
    link_mass = []
    for list in list_link:
        response = requests.get(url=list)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        stuff = soup.find_all('div', class_='item')
        for st in stuff:
            mark = st.find('div', class_='sale_button').find('a')
            #print(mark['href'])
            link_mass.append(f"http://parsinger.ru/html/{mark['href']}")

    #печатаем массив со всеми найдеными линками (34шт)
    print(link_mass)

    art_value_mass = 0
    for link in link_mass:
        response = requests.get(url=link)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        art = soup.find('p', class_='article').get_text()
        #print(art)
        art_value = int(''.join(x for x in art.strip() if x.isdigit()))
        art_value_mass += art_value

    print(f"Final result: {art_value_mass}")



# найти линки всех 160 товаров на сайте и общую стоимость товаров
def pagination_5():
    index_labels = {1: "watch", 2: "mobile", 3: "mouse", 4: "hdd", 5: "headphones"}
    main_list = []
    for i in range(5):
        for j in range(32):
            url = f"https://parsinger.ru/html/{index_labels[i + 1]}/{i + 1}/{i + 1}_{j + 1}.html"
            print(url)
            main_list.append(url)

    print(len(main_list))

    final_sum = 0
    for man in main_list:
        print(man)
        response = requests.get(url=man)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        volume = soup.find('span', id='in_stock').text
        price = soup.find('span', id='price').text
        volume_int = int(''.join(x for x in volume.strip() if x.isdigit()))
        price_int = int(''.join(x for x in price.strip() if x.isdigit()))
        first_sum = volume_int * price_int
        print(first_sum)
        final_sum += first_sum

    print(f"Final sum: {final_sum}")





################
pagination_5()