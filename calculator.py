def is_any_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def adition(var1, var2):
    if '.' in var1 or '.' in var2:
        result = float(var1) + float(var2)
        var1 = float(var1)
        var2 = float(var2)
        print(f"{"%.2f" % var1} + {"%.2f" % var2} = {"%.2f" % result}")
    else:
        result = int(var1) + int(var2)
        print(f"{var1} + {var2} = {result}")



def subtraction(var1, var2):
    if '.' in var1 or '.' in var2:
        result = float(var1) - float(var2)
        var1 = float(var1)
        var2 = float(var2)
        print(f"{"%.2f" % var1} - {"%.2f" % var2} = {"%.2f" % result}")
    else:
        result = int(var1) - int(var2)
        print(f"{var1} - {var2} = {result}")


def multiplication(var1, var2):
    if '.' in var1 or '.' in var2:
        result = float(var1) * float(var2)
        var1 = float(var1)
        var2 = float(var2)
        print(f"{"%.2f" % var1} * {"%.2f" % var2} = {"%.2f" % result}")
    else:
        result = int(var1) * int(var2)
        print(f"{var1} * {var2} = {result}")


def devision(var1, var2):
    try:
        if '.' in var1 or '.' in var2:
            result = float(var1) / float(var2)
            var1 = float(var1)
            var2 = float(var2)
            print(f"{"%.2f" % var1} / {"%.2f" % var2} = {"%.2f" % result}")
        else:
            result = int(var1) / int(var2)
            print(f"{var1} / {var2} = {result}")
    except ZeroDivisionError:
        print("Error: You can't divide by zero!")
        exit()




##Main part
print("Welcome to console calculator application!")
menu_action = input("Press 'y' to continue or 'x' to exit: ")
if menu_action == 'y':
    var1 = input("Please, enter first number: ")
    if is_any_digit(var1):
        pass
    else:
        print("Number is a string")
        print("Please, rerun application and try again")
        exit()

    action = input("Please, enter an action: (+, -, *, /): ")
    if action in ('+', '-', '*', '/'):
        pass
    else:
        print("Operation is not supported")
        print("Please, rerun application and try again")
        exit()

    var2 = input("Please, enter second number: ")
    if is_any_digit(var2):
        pass
    else:
        print("Number is a string")
        print("Please, rerun application and try again")
        exit()

    if action == "+": adition(var1, var2)
    elif action == "-": subtraction(var1, var2)
    elif action == "*": multiplication(var1, var2)
    elif action == "/": devision(var1, var2)


elif menu_action == 'x':
    print("Application is closed. Thank you")
    exit()

else:
    print("Command is not supported")
    print("Please, rerun application and try again")
    exit()