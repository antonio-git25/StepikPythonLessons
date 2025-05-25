class MyClass:
    class_attribute = 10

    def __init__(self, value):
        self.instance_attribute = value

    @classmethod
    def modify_class_attribute(cls, new_value):
        # Метод класса для изменения классового атрибута
        cls.class_attribute = new_value


class BankAccount:
    interest_rate = 0.02  # Атрибут класса для процентной ставки

    def __init__(self, balance):
        self.balance = balance

    def add_interest(self):
        self.balance += self.balance * BankAccount.interest_rate

    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate

    def display_balance(self):
        return print(f"Баланс счета: {self.balance}")



# # Создание экземпляра с использованием метода класса
# obj1 = MyClass(42)
# print(obj1.class_attribute)  # Вывод: 10
#
# obj2 = MyClass(50)
# print(obj2.class_attribute)  # Вывод: 10
#
# obj1.modify_class_attribute(20)
# print(obj1.class_attribute)
# print(obj2.class_attribute)



# Создаем счета
# account1 = BankAccount(1000)
# account2 = BankAccount(2000)

# Выводим балансы
# account1.display_balance()  # Вывод: Баланс счета: 1000
# account2.display_balance()  # Вывод: Баланс счета: 2000
# account1.add_interest()
# account2.add_interest()
# account1.display_balance()
# account2.display_balance()

# # Изменяем процентную ставку с помощью метода класса
# BankAccount.change_interest_rate(0.03)
# # Применяем процентную ставку ко всем счетам
# account1.add_interest()
# account2.add_interest()
# # Выводим обновленные балансы
# account1.display_balance()  # Вывод: Баланс счета: 1030.0
# account2.display_balance()  # Вывод: Баланс счета: 2060.0


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        # реализация сложения дробей
        return Fraction((self.numerator * other.denominator) + (other.numerator * self.denominator), self.denominator * other.denominator)

    def __sub__(self, other):
        # реализация вычитания дробей
        return Fraction((self.numerator * other.denominator) - (other.numerator * self.denominator), self.denominator * other.denominator)

    def __mul__(self, other):
        # реализация умножения дробей
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __eq__(self, other):
        # реализация сравнения дробей
        return self.numerator * other.denominator == self.denominator * other.numerator





class Juice:
    def __init__(self, name, capacity):
       self.name = name
       self.capacity = capacity

    def __str__(self):
        return f"{self.name} {self.capacity}"

    def __add__(self, other):
        return Juice(f"{self.name}&{other.name}", f"{self.capacity + other.capacity}L")



import math

class Shape:
    def calculate_area(self):
        return 0

    def __add__(self, other):
        return self.calculate_area() + other.calculate_area()


class Rectangle(Shape):
    def __init__(self, length, width):
      self.length = length
      self.width = width

    def calculate_area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return round(math.pi * self.radius ** 2)


class Triangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        return (self.a * self.b)/2



#################################################################

class Book:
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow_book(self):
        self.available_copies -= 1
        if self.available_copies == 0:
            print(f"Sorry, '{self.title}' is currently unavailable.")

    def return_book(self):
        self.available_copies += 1
        if self.available_copies == self.total_copies:
            print(f"Invalid operation. All copies of '{self.title}' have already been returned.")


class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def display_info(self):
        print(f"Author: {self.name}, Born: {self.birth_year}")


class Librarian:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def issue_book(self, book, member):
        book.available_copies -= 1
        if book.available_copies > 0:
            print(f"Book '{book.title}' issued to {member}.")
        else:
            print(f"Sorry, '{book.title}' is currently unavailable for issuing.")


    def collect_book(self, book, member):
        book.available_copies += 1
        if book.available_copies == book.total_copies:
            print(f"Book '{book.title}' collected from {member}.")
        else:
            print(f"Invalid operation. All copies of '{book.title}' have already been returned.")



##########################################################

class Player:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}"


class Team:
    list_players = []

    def __init__(self, name, coach):
        self.name = name
        self.coach = coach

    def add_player(self, player):
        Team.list_players.append(player)

    def remove_player(self, player):
        Team.list_players.remove(player)

    def list_players(self):
        for play in Team.list_players:
            print(play)




from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, balance=0):
        self.balance = balance

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    def check_balance(self):
        print(self.balance)
        return self.balance


class SavingsAccount(BankAccount):
    def deposit(self, value):
        self.balance += value
        print(f"Успешно внесено: {value}")

    def withdraw(self, value):
        print("С сберегательного счёта нельзя снимать деньги!")


class CheckingAccount(BankAccount):
    def deposit(self, value):
        self.balance += value
        print(f"Успешно внесено: {value}")

    def withdraw(self, value):
        self.balance -= value
        print(f"Успешно снято: {value}")



savings_account = SavingsAccount(500)
checking_account = CheckingAccount()

#Снятие и пополнение Сберегательного счета
savings_account.deposit(500) #Успешно внесено: 500
savings_account.withdraw(700) #С сберегательного счёта нельзя  снимать деньги!

#Снятие и пополнение Расчетного счета
checking_account.deposit(1000) #Успешно внесено: 1000
checking_account.withdraw(500) #Успешно снято: 500

#Проверка балланса счетов
savings_account.check_balance() #1000
checking_account.check_balance() #500