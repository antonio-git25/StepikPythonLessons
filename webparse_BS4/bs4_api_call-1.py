from bs4 import BeautifulSoup
import lxml
import html5lib
import requests


def first_example():
    # Пример 1. Передача файла HTML напрямую без использования менеджера контекста
    # file = open('index.html', encoding='utf-8')
    # soup = BeautifulSoup(file, 'lxml')
    # file.close()
    # print("Анализ файла без использования менеджера контекста:\n", soup)

    # Пример 2. Передача файла HTML с использованием менеджера контекста
    with open('index.html', 'r', encoding='utf-8') as file:
        soup2 = BeautifulSoup(file, 'lxml')
        print("Анализ файла с использованием менеджера контекста:\n", soup2)


def second_example():
    response = requests.get(url='http://parsinger.ru/html/watch/1/1_1.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup)


def div_tag():
    html = "<div class='myclass'>Hello, world!</div>"
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup.div
    print(type(tag))  #<class 'bs4.element.Tag'>
    print(tag.name)   #div
    print(tag.attrs)  #{'class': ['myclass']}
    print(tag.string) #Hello, world!
    print(tag.text)
    print(tag.get_text())


def tag_a():
    html_doc = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Пример карточки товара</title>
    </head>
    <body>
        <div class="card">
            <img src="image.jpg" alt="Пример изображения товара">
            <h2 class="card-title"> iPhone 15 </h2>
            <p class="card-description">Аппаратной основой Apple iPhone 15 Pro Max стал 3-нанометровый чипсет A17 Pro с 6-ядерным GPU и поддержкой трассировки лучей.</p>
            <p class="card-price">999 999 руб.</p>
            <a href="https://example.com/product-link" class="card-link">Подробнее</a>
        </div>
    </body>
    </html>
    """

    soup = BeautifulSoup(html_doc, 'lxml')
    call = soup.find('p', class_='card-description')
    p_description = call.text
    print(p_description)


def sum_articles():
    response = requests.get('http://parsinger.ru/4.3/2/index.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    articuls = soup.find_all('p', attrs={'class': 'card-articul'})
    # Извлечение числовых значений артикулов и их суммирование
    sum_articuls = 0
    for tag in articuls:
        print(tag)
        cut = tag.text
        sum_articuls += int(cut[9:])
    print(f"Сумма артикулов: {sum_articuls}")  # Вывод результата


def tag_find():
    html = """
    <div id="outer">
      <span>Внутри outer</span>
      <div id="inner">
        <span>Внутри inner</span>
      </div>
    </div>
    """
    soup = BeautifulSoup(html, "html.parser")
    outer = soup.find("div", id="outer")
    # Поиск только в прямых детях
    span_shallow = outer.find("span", recursive=False)
    print(span_shallow)  # <span>Внутри outer</span>
    # Поиск глубоко (по умолчанию recursive=True)
    span_deep = outer.find("span")
    print(span_deep)  # первый найденный: <span>Внутри outer</span>


def tag_find_all():
    html_doc = """
    <html>
        <head>
            <title>Example Page</title>
        </head>
        <body>
            <div id="main">
                <h1>Hello World</h1>
                <p class="info">This is a paragraph.</p>
                <p class="info">This is another paragraph.</p>
                <ul>
                    <li>Item 1</li>
                    <li>Item 2</li>
                    <li>Item 3</li>
                </ul>
            </div>
            <div id="secondary">
                <p>Some additional information.</p>
            </div>
        </body>
    </html>
    """
    soup = BeautifulSoup(html_doc, 'html.parser')
    # Найти все теги p в HTML-документе, включая те, что находятся внутри вложенных тегов.
    all_p_tags = soup.find_all('p', recursive=True)
    print(all_p_tags)


def parser_test1():
    response = requests.get('https://parsinger.ru/4.1/1/index4.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    #tags_li = soup.find_all("div", attrs={"class": "description product_description"})
    tags_li = soup.find_all("li", id=True)
    for tag in tags_li:
        print(tag['id'])


def select_1():
    html = """
    <html>
      <body>
        <div id="div1">
          <p class="highlight">This is a highlighted paragraph in div1.</p>
          <p>This is a normal paragraph in div1.</p>
        </div>
        <div id="div2">
          <p class="highlight">This is a highlighted paragraph in div2.</p>
          <p>This is a normal paragraph in div2.</p>
        </div>
      </body>
    </html>
    """
    soup = BeautifulSoup(html, "html.parser")
    # Выберем первый параграф с классом "highlight"
    highlighted_para = soup.select_one("p[class='highlight']")
    print("Highlighted paragraph:")
    print(highlighted_para.text)


def parent():
    html = '''
    <!DOCTYPE html><html lang="en"><head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Пример .parent</title>
    </head>
    <body>
    <div id="parent-container">
        <h1 id="main-heading">Заголовок (.parent)</h1>
        <p id="paragraph">Текст абзаца ()</p>
        <ul id="list">
            <li class="list-item">Элемент списка 1</li>
            <li class="list-item">Элемент списка 2</li>
        </ul>
    </div></body></html>
    '''
    soup = BeautifulSoup(html, "html.parser")
    li_elem = soup.find('li', class_='list-item')
    parent_elem = li_elem.parent
    # Выводим содержимое родительского элемента
    print(parent_elem)


def section_text():
    response = requests.get('https://parsinger.ru/4.1/1/index6.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    sibling = soup.find('p', class_='section-text').next_sibling.text.strip()
    #print(sibling.text.strip())
    print(sibling)


def section_text2():
    response = requests.get('https://parsinger.ru/4.1/1/index5.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    email_fields = soup.find_all('div', class_='email_field')
    emails = []
    for eml in email_fields:
        text_node = eml.find('strong').next_sibling
        if text_node:
            email_text = text_node.strip()
            emails.append(email_text)

    print(emails)


"""======================"""
section_text2()
