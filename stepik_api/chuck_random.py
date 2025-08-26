import requests

class Test_new_joke():
    """create new joke"""

    def __init__(self):
        pass

    def test_create_new_random_joke(self):
        url = "https://api.chucknorris.io/jokes/random"
        print(url)
        result = requests.get(url)
        print("status code: " + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Success!")
        else:
            print("Fail!")
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        # check_info = check.get("categories")
        # print(check_info)
        # assert check_info == []
        # print("Category is correct")
        check_info_value = check.get("value")
        print(check_info_value)
        name = "Chuck"
        if name in check_info_value:
            print("Chuck is present in joke")
        else:
            print("Chuck is not present")


    def test_create_new_random_category_joke(self):
        category = "sport"
        url = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url)
        result = requests.get(url)
        print("status code: " + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Success!")
        else:
            print("Fail!")
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == ["sport"]
        print("Category is correct")



class TestCreateJoke():

    url = 'https://api.chucknorris.io/jokes/random'

    def test_create_random_joke_category(self):
        category = 'animal'
        path_random_joke_category = f"?category={category}"
        url_random_joke_category = self.url + path_random_joke_category
        print(url_random_joke_category)

        result = requests.get(url_random_joke_category)
        print(result.json())

        print(f'Статус-код: {result.status_code}')
        assert result.status_code == 200, 'ОШИБКА, Статус-код не совпадают'
        print('Статус-код корректен')

        check_joke = result.json()
        joke_value = check_joke.get("value")
        print(joke_value)

        joke_category = check_joke.get("categories")
        print(joke_category)
        assert joke_category[0] == category, 'ОШИБКА, Статус-код не совпадает'
        print('Категория корректна')

        assert_word = 'Chuck'
        assert assert_word in joke_value, 'ОШИБКА, Проверочное слово отсутствует'
        print('Проверочное слово присутствует')
        print("Тест прошел успешно")


# random_joke = Test_new_joke()
# random_joke.test_create_new_random_joke()


# start = TestCreateJoke()
# start.test_create_random_joke_category()

sport_joke = Test_new_joke()
sport_joke.test_create_new_random_category_joke()