import requests

class Test_joke():
    """url's for using"""
    base_url = "https://api.chucknorris.io/jokes/categories"
    category_url = "https://api.chucknorris.io/jokes/random?category="

    def __init__(self):
        pass

    """получение и вывод всех категорий"""
    def get_categories(self):
        print(self.base_url)
        result_1 = requests.get(self.base_url)
        assert 200 == result_1.status_code
        joke_list = list(result_1.json())
        print("We've got next catogories of jokes:")
        for i in joke_list:
            print(i)
        return joke_list

    """вывод шутки для текущей категории"""
    def show_jokes_type(self, joke_type):
        url_2 = self.category_url + joke_type
        print(url_2)
        print("type of category: " + joke_type)
        result_2 = requests.get(url_2)
        assert 200 == result_2.status_code
        info = result_2.json()
        joke = info.get("value")
        print("Joke: " + joke)

#Вызов методов
start = Test_joke()
joke = start.get_categories()

#Вывод каждой шутки из категории в массиве цикла
for jk in joke:
    start.show_jokes_type(jk)




