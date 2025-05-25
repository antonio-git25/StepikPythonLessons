import requests

class Test_new_location():

    def __init__(self):
        pass

    def test_create_new_location(self):

        base_url = "https://rahulshettyacademy.com"
        post_resourse = "/maps/api/place/add/json"
        key = "?key=qaclick123"

        post_url = base_url + post_resourse + key
        print(post_url)

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

        result_post = requests.post(post_url, json = json_for_create_new_location)
        print(result_post.text)

        print("status code: " + str(result_post.status_code))
        assert 200 == result_post.status_code
        if result_post.status_code == 200:
            print("Success! New location is created")
        else:
            print("Fail!")

        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print("Status code: " + check_info_post)
        assert check_info_post == "OK"
        print("Status is correct")

        place_id = check_post.get("place_id")
        print("place id: " + place_id)

        """check new location creation"""
        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print("status code: " + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Success! of checking of new location creation")
        else:
            print("Fail!")


        """change of new location"""
        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        result_put = requests.put(put_url, json = json_for_update_new_location)
        print(result_put.text)
        print("status code: " + str(result_put.status_code))
        assert 200 == result_put.status_code
        if result_put.status_code == 200:
            print("Success of checking of update location")
        else:
            print("Fail!")

        check_put = result_put.json()
        check_put_info = check_put.get("msg")
        print("Message: " + check_put_info)
        assert check_put_info == "Address successfully updated"
        print("Message is wrong")


        """Checking of changing of new location"""
        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print("status code: " + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Success! of checking of changing location")
        else:
            print("Fail!")
        check_address = result_get.json()
        check_address_info = check_address.get("address")
        print("Message: " + check_address_info)
        assert check_address_info == "100 Lenina street, RU"
        print("Message is correct")


        """Delete of new location"""
        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_for_delete_new_location = {"place_id": place_id}
        result_delete = requests.delete(delete_url, json = json_for_delete_new_location)
        print(result_delete.text)
        print("status code: " + str(result_delete.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Success! Deleting of created location")
        else:
            print("Fail!")
        check_status = result_delete.json()
        check_status_info = check_status.get("status")
        print("Message: " + check_status_info)
        assert check_status_info == "OK"
        print("Message is correct")

        """check of deleting of new"""
        result_get = requests.get(get_url)
        print(result_get.text)
        print("status code: " + str(result_get.status_code))
        assert 404 == result_get.status_code
        if result_get.status_code == 404:
            print("Success! of deleting new location creation")
        else:
            print("Fail!")
        check_msg = result_get.json()
        check_msg_info = check_msg.get("msg")
        print("Message: " + check_msg_info)
        assert check_msg_info == "Get operation failed, looks like place_id  doesn't exists"
        print("Message is correct")




new_place = Test_new_location()
new_place.test_create_new_location()