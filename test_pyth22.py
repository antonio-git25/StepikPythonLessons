print('hello man')
#name = input("What is your name?")
#print("Hi, ", name)

mobile_devices = {
    'cucuPhone': 2010,
    'cucuBlet': 2013,
    'cucuClock': 2015,
    'cucuEar': 2018,
    'cuCube': 2015,
}

home_devices = {
    'cucuLot': 2011,
    'cucuBlock': 2010,
    'cucuWall': 2010,
    'cucuMonitor': 2020,
    'cucuLamp': 2015,
    'cucuTable': 2016,
    'cucuTV': 2017,
}

not_supported_devices = {'cucuBlock', 'cucuBlet', 'cucuWall'}
result_catalog = {}

mobile_set = set(mobile_devices)
home_set = set(home_devices)

all_devices = mobile_set.union(home_set)
print(all_devices)
supported_devices = all_devices.difference(not_supported_devices)
print(supported_devices)

