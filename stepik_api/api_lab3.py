import requests

class Test_location():

    def __init__(self):
        pass

    json_for_create_new_location = {
        "location": {
            "lat": -38.383494,
            "lng": 33.427362
        },
        "accuracy": 50,
        "name": "Frontline house",
        "phone_number": "(+91) 983 893 3937",
        "address": "29, side layout, cohen 09",
        "types": [
            "shoe park",
            "shop"
        ],
        "website": "http://google.com",
        "language": "French-IN"
    }

    base_url = "https://rahulshettyacademy.com"
    post_resourse = "/maps/api/place/add/json"
    get_resource = "/maps/api/place/get/json"
    key = "?key=qaclick123"

    def test_create_new_location(self):
        post_url = self.base_url + self.post_resourse + self.key
        print(post_url)
        result_post = requests.post(post_url, json = self.json_for_create_new_location)
        #print(result_post.text)
        print("status code: " + str(result_post.status_code))
        assert result_post.status_code == 200
        if result_post.status_code == 200:
            print("Success! New location is created")
        else:
            print("Fail! New location is not created")

        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print("Status code: " + check_info_post)
        assert check_info_post == "OK"
        print("Status is correct")

        place_id = check_post.get("place_id")
        print("Place ID: " + place_id)

        return place_id


    def write_placeid(self, place_id):
        file = open('place_id.txt', 'a')
        file.write(place_id)
        file.write('\n')
        file.close()
        print(f"Place ID: {place_id} put into file")


    def check_location(self):
        print('\n')
        print("Check created locations from file")
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
            assert result_get.status_code == 200
            if result_get.status_code == 200:
                print("Success! Current location is present in server")
            else:
                print("Fail! Current location is not present in server")
            count += 1




#Create object of class
start = Test_location()

#Create five locations
for i in range(1,6):
    print(i)
    df=start.test_create_new_location()
    start.write_placeid(df)


#Check created location from file data
start.check_location()












