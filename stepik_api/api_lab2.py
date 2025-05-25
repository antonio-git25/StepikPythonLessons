import requests

class Test_joke():
    """url's for using"""
    base_url = "https://api.chucknorris.io/jokes/categories"
    category_url = "https://api.chucknorris.io/jokes/random?category="

    def __init__(self):
        pass

    """получение всех категорий"""
    def get_categories(self):
        result_1 = requests.get(self.base_url)
        assert 200 == result_1.status_code
        joke_list = list(result_1.json())
        return joke_list

    """вывод всех категорий"""
    def show_categories(self):
        result_1 = requests.get(self.base_url)
        assert 200 == result_1.status_code
        joke_list = list(result_1.json())
        print("Please, choose on of the next categories:")
        print(joke_list)

    """вывод шутки для выбраной категории"""
    def show_jokes_type(self, joke_type):
        url_2 = self.category_url + joke_type
        print(url_2)
        print("type of category: " + joke_type)
        result_2 = requests.get(url_2)
        assert 200 == result_2.status_code
        info = result_2.json()
        joke = info.get("value")
        print("Joke: " + joke)


type_joke = input("Enter type of joke: ")
print("Your input type: ", type_joke)

start = Test_joke()
list_t = start.get_categories()

if type_joke in list_t:
    start.show_jokes_type(type_joke)
else:
    start.show_categories()



