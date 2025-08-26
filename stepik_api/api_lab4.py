import requests

class Test_location():

    def __init__(self):
        pass

    base_url = "https://rahulshettyacademy.com"
    delete_resource = "/maps/api/place/delete/json"
    get_resource = "/maps/api/place/get/json"
    key = "?key=qaclick123"


    def parsing_file(self, line):
        file = open('place_id.txt', 'r')
        lines = file.readlines()
        file.close()
        print(f"File has {len(lines)} lines")
        print(f"Extract {line} Place ID for delete location: {lines[line-1].strip()}")
        return lines[line-1].strip()


    def delete_location(self, place_id):
        """Delete of new location"""
        delete_url = self.base_url + self.delete_resource + self.key
        print(delete_url)
        json_for_delete_new_location = {"place_id": place_id}
        result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
        print("status code: " + str(result_delete.status_code))
        assert 200 == result_delete.status_code
        if result_delete.status_code == 200:
            print("Success! Location has deleted")
        else:
            print("Fail! Location is not deleted")
        check_status = result_delete.json()
        check_status_info = check_status.get("status")
        print("Message: " + check_status_info)
        assert check_status_info == "OK"
        print("Message is correct")


    def check_valid_locations(self):
        print('\n')
        print("Check valid locations from file")
        file = open('place_id.txt', 'r')
        lines = file.readlines()
        file.close()
        count = 1
        for ln in lines:
            place_id = ln.strip()
            print(f"Check Place ID #{count}: {place_id}")
            get_url = self.base_url + self.get_resource + self.key + "&place_id=" + place_id
            print(get_url)
            result_get = requests.get(get_url)
            print("status code: " + str(result_get.status_code))
            if result_get.status_code == 200:
                print("Success! Current location is present in server")
                print(f"Put Place ID: {place_id} into new updated file")
                file_2 = open('place_id_updated.txt', 'a')
                file_2.write(place_id)
                file_2.write('\n')
                file_2.close()
            elif result_get.status_code == 404:
                print("Fail! Current location is not present in server")
            count += 1




#Create object of class
start = Test_location()

#Choose locations for deleting
place_1 = start.parsing_file(2)
place_2 = start.parsing_file(4)

#Delete choosing locations
start.delete_location(place_1)
start.delete_location(place_2)

#Check corrected locations
start.check_valid_locations()












