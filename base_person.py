class Person():
    """human model"""

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        description = self.name + ", has " + str(self.age) + ", his height = " + str(self.height) + ", his weight = " + str(self.weight)
        print(description)

    def get_weight(self):
        print("Wight of our human : " + str(self.weight))

    def update_weight(self, kg):
        self.weight = kg



class Warrior(Person):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        print("Value of rage : " + str(self.rage))

    def description_person(self):
        description = self.name + ", has " + str(self.age) + ", his rage = " + str(self.rage)
        #print(description)
        return description


