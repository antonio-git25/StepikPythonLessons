import requests

class Show_acters():

    def __init__(self):
        pass

    base_url = "https://swapi.dev/"
    first_get_resource = "api/people/4/"

    def get_darth_vader(self):
        get_url = self.base_url + self.first_get_resource
        print(get_url)
        result_get = requests.get(get_url)
        print("status code: " + str(result_get.status_code))
        assert result_get.status_code == 200

        check = result_get.json()
        check_films = check.get("films")
        show_films = list(check_films)
        print("Darth Vader was acter in next movies:")
        for show in show_films:
            print(show)

        return show_films


    def get_acters(self,show_films):
        for film in show_films:
            print("Check next link of film: " + film)
            get_film = requests.get(film)
            print("status code: " + str(get_film.status_code))
            assert get_film.status_code == 200

            check = get_film.json()
            check_actors = check.get("characters")
            show_actors = list(check_actors)
            print("Current film has next actors:")
            print(len(show_actors))
            for show in show_actors:
                print(show)
                file = open('../acter_links.txt', 'a')
                file.write(show)
                file.write('\n')
                file.close()


    def parse_people_list(self):
        file_1 = open('../acter_links.txt', 'r')
        lines = file_1.readlines()
        file_1.close()
        data_set = set(lines)
        print(len(data_set))

        file_2 = open('unique_acter_links.txt', 'a')
        for data in data_set:
            #print(data.strip())
            file_2.write(data.strip())
            file_2.write('\n')
        file_2.close()
        print("List with actor links has been updated!")


    def show_names_acters(self):
        file_3 = open('unique_acter_links.txt', 'r')
        lines = file_3.readlines()
        file_3.close()
        print("Count names: " + str(len(lines)))

        file_4 = open('final_names.txt', 'a', encoding='utf-8')
        for line in lines:
            get_name = requests.get(line.strip())
            assert get_name.status_code == 200
            check = get_name.json()
            show_name = check.get("name")
            print(show_name)
            file_4.write(show_name)
            file_4.write('\n')
        file_4.close()
        print("Final file with unique names has been created!")











#Create object of class
start = Show_acters()

#Show films od Darth Vader
list_movies = start.get_darth_vader()

#Show links of actors
start.get_acters(list_movies)

#Update file for unique links
start.parse_people_list()

#Get unique names of acters and put it into final file
start.show_names_acters()













