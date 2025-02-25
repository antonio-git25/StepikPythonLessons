#from base_person import Person, Warrior
import base_person

# man = base_person.Person("Alex", 30, 180)
# man.description_person()
#
# warrior = base_person.Warrior("Konan", 32, 200)
# print("Name of new person: " + warrior.description_person())

class Car():

    def __init__(self, model, year, v_engine, price, way):
        self.model = model
        self.year = year
        self.v_engine = v_engine
        self.price = price
        self.way = way
        self.weels = 4

    def description_car(self):
        print(f"{self.model} ({self.weels} weels)")
        print(f"Year: {self.year}")
        print(f"Volume of engine: {self.v_engine} cubes")
        print(f"Price: {self.price} USD")
        print(f"Way: {self.way} miles")


car1 = Car("Granta", 2015, 125, 10000, 115000)
car1.description_car()

class Trunk(Car):
    def __init__(self, model, year, v_engine, price, way):
        super().__init__(model, year, v_engine, price, way)
        self.weels = 8

    def description_car(self):
        print(f"{self.model} ({self.weels} weels)")
        print(f"Year: {self.year}")
        print(f"Volume of engine: {self.v_engine} cubes")
        print(f"Price: {self.price} USD")
        print(f"Way: {self.way} miles")

car2 = Trunk("Kamaz", 1990, 550, 220000, 45000)
print('\n')
car2.description_car()