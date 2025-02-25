
import string
from random import randint
import random
import datetime


# dark = 78.89
# if type(dark) == int:
#     print('it is int number')
# else:
#     print('it is not int number')
#
# cat = isinstance(dark, int)
# print(cat)


###############################################
# first_name = "Ivan"
# last_name = "Durov"
# a = '{} {}'
# result = a.format(first_name, last_name)
# print("My name is : " + result)
#
# result = f'{first_name} {last_name}'
# print("My name is: " + result)


####################################################

# num = 5  # Глобальная переменная
#
# def my_function():
#     num = 10  # Локальная переменная
#     print(f"Внутри функции num = {num}")
#
# my_function()
#
# print(f"Вне функции num = {num}")

# mass = [5,4,9,7,2]
# for num in mass:
#     for i in range(2, num):
#         if (num % i) == 0:
#             break
#     else:
#         print(num)



# from collections import Counter
#
# def count_repeats(lst):
#     """Возвращает словарь, в котором каждому элементу списка lst соответствует количество его повторений"""
#     repeats = {}
#     for item in lst:
#         if item in repeats:
#             repeats[item] += 1
#         else:
#             repeats[item] = 1
#     return repeats
#
# lst = [10, 10, 23, 10, 123, 66, 78, 123]
# repeats = count_repeats(lst)
# print(repeats)  # {10: 3, 123: 2}


# numbers = [5, 8, 2, 1, 3, 5, 4, 5, 2, 8, 12]
# numbers.sort()
# pairs = 0
# i = 1
#
# while i < len(numbers):
#     if numbers[i] == numbers[i - 1]:
#         pairs += 1
#         i += 1
#
#     i += 1
#
# print(pairs)


# new_dict = {'file1.txt': 10, 'file2.txt': 100, 'file3.txt': 101, 'file4.txt': 200, 'file5.txt': 5, 'file6.txt': 305}
#
# for key, value in new_dict.items():
#     if value > 100: print(key)


# new_dict2 = {'Имя': 'Светлана', 'Пароль': 'qwer1234', 'Код': 1984}
#
# for key, value in new_dict2.items():
#     if key == 'Имя':
#         coded_name = value[0]
#         k1 = 1
#         while k1 < len(value):
#             coded_name = coded_name + '#'
#             k1 += 1
#         print(coded_name)
#     elif key == 'Пароль':
#         coded_pass = ""
#         k2 = 0
#         while k2 < len(value):
#             coded_pass = coded_pass + '#'
#             k2 += 1
#         print(coded_pass)
#     elif key == 'Код':
#         coded_pin = ""
#         str3 = str(value)
#         k3 = 0
#         while k3 < len(str3)-1:
#             coded_pin = coded_pin + '#'
#             k3 += 1
#         coded_pin = coded_pin + str3[-1]
#         print(coded_pin)


##################################
# films = ['Скала', 'Западня', 'Бэтман', 'Западня', 'Западня', 'Бэтман']
#
# def count_repeats(films):
#     repeats = {}
#     for item in films:
#         if item in repeats:
#             repeats[item] += 1
#         else:
#             repeats[item] = 1
#     return repeats
#
# repeats = count_repeats(films)
# print(repeats)
#
# sorted_dict = dict(sorted(repeats.items(), reverse=True, key=lambda item: item[1]))
# print(sorted_dict)
#
# for k1, v1 in sorted_dict.items():
#     print(f"{k1} - {v1}")


# num_1=int(input("Введите первое число: "))
# num_2=int(input("Введите второе число: "))
#
# try:
#     result = num_1 / num_2
#     print(f"Результат деления: {result}")
# # except ZeroDivisionError:
# #     print("На ноль делить нельзя")
# except TypeError:
#     print("Неверный формат числа ")
# finally:
#     print("До скорых встреч")


# r1 = '-5 anyf p'
# r2 = '-5dr'
# r3 = '-6.5fr'
# r4 = '2.r'
# r5 = '4.23'
# r6 = '-1.5'

# def is_digit(string):
#     if string.isdigit():
#        return True
#     else:
#         try:
#             float(string)
#             return True
#         except ValueError:
#             return False
#
# print(r1, "->", is_digit(r1))
# print(r2, "->", is_digit(r2))
# print(r3, "->", is_digit(r3))
# print(r4, "->", is_digit(r4))
# print(r5, "->", is_digit(r5))
# print(r6, "->", is_digit(r6))


# >>> x = 12
# >>> isinstance(x, int)
# True
# >>> y = 12.0
# >>> isinstance(y, float)
# True

# f1 = '-5'
# f2 = '7'
#
# if '.' in f1:
#     result = float(f1) + float(f2)
#     print(result)
# else:
#     result = int(f1) + int(f2)
#     print(result)
#
# d1 = '-5.62'
# d2 = '7'
# result = float(d1) + float(d2)
# print('\n')
# print(result)




#result = randint(1,6)
# mass = ['906','901','902','908']
# print(random.choice(['906','901','902','908']))
#
# cell_gen = f"{random.choice(['906','902','908','960','910','950'])}{randint(340,820)}{randint(10,90)}{randint(10,90)}"
# print(cell_gen)
#
# def randomword(length):
#    letters = string.ascii_lowercase
#    return ''.join(random.choice(letters) for i in range(length))
#
# i=1
# while i < 8:
#     print(randomword(50))
#     i += 1


#Test date def
def date_creation(cur_date, plus_day):
    #format: dd/mm/yyyy
    upd_date = ''
    m_ms = [31,28,31,30,31,30,31,31,30,31,30,31]
    print(cur_date)
    print(plus_day)
    #parsing
    year = cur_date[6:]
    month = cur_date[3:5]
    day = cur_date[:2]
    print(year)
    print(month)
    print(day)

    if month == '01': days_in_month = 31
    elif month == '02': days_in_month = 28
    elif month == '03': days_in_month = 31
    elif month == '04': days_in_month = 30
    elif month == '05': days_in_month = 31
    elif month == '06': days_in_month = 30
    elif month == '07': days_in_month = 31
    elif month == '08': days_in_month = 31
    elif month == '09': days_in_month = 30
    elif month == '10': days_in_month = 31
    elif month == '11': days_in_month = 30
    elif month == '12': days_in_month = 31

    if (plus_day + int(day)) > days_in_month:
        month = str(int(month) + 1)
        day = str(plus_day-(days_in_month-int(day)))
    else:
        day = str(int(day) + plus_day)

    if int(month) > 12:
        year = str(int(year) + 1)
        month = '01'

    print(f"Feature date is {day}/{month}/{year}")
    upd_date = f"{month}/{day}/{year}"
    return upd_date


date_creation('25/06/2010', 10)


now_date = datetime.datetime.now().strftime("%m.%d.%Y")
now_date_day = datetime.datetime.now().strftime("%d")
now_date_month = datetime.datetime.now().strftime("%m")
now_date_year = datetime.datetime.now().strftime("%Y")
print("Current date: ", now_date)
print("Current day: ", now_date_day)
print("Current month: ", now_date_month)
print("Current year: ", now_date_year)


past_date = datetime.datetime.today() + datetime.timedelta(days=5)
print(f"today: {datetime.datetime.today()}")
print(f"after 10 days: {past_date.strftime("%m.%d.%Y")}")
print(past_date.strftime("%m"))
print(past_date.strftime("%d"))
print(past_date.strftime("%Y"))


# for i in range(0,5):
#     print('hello')

sum = 6
locator_mass = []
for i in range(0,sum):
    prod_locator = f"//a[@id='item_{str(i+1)}_title_link']"
    locator_mass.append(prod_locator)
    print(prod_locator)

print("print massiv")
for d in locator_mass:
    print(d)


bye_prod1_bt = "//button[@id='add-to-cart-sauce-labs-backpack']"  #Sauce Labs Backpack
bye_prod2_bt = "//button[@id='add-to-cart-sauce-labs-bike-light']"  #Sauce Labs Bike Light
bye_prod3_bt = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"  #Sauce Labs Bolt T-Shirt
bye_prod4_bt = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']" #Sauce Labs Fleece Jacket
bye_prod5_bt = "//button[@id='add-to-cart-sauce-labs-onesie']" #Sauce Labs Onesie
bye_prod6_bt = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"  #Test.allTheThings() T-Shirt (Red)


string = 'Sauce Labs Fleece Jacket'
print(string.casefold().replace(' ', '-'))