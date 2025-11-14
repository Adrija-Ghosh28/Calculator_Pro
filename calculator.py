# print("Hello World")

def sum (x, y):
    return x + y 

def subtract (x, y):
    return x - y

def multiply (x, y):
    return x * y

def division (x, y):
    if y == 0:
        print("Division by 0 Error")

    else:
        return x / y

print("Welcome to Calculator Pro")
print(" Select 1 for addition \n Select 2 for subtraction \n Select 3 for multiplication \n Select 4 for division \n Select any other button to exit")

choice=int(input("Enter Choice: "))

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

while (True):
    if choice == 1:
        res = sum (a, b)
        break

    elif choice == 2:
        res = subtract (a, b)
        break

    elif choice == 3:
        res = multiply (a, b)
        break

    elif choice == 4:
        res = division (a, b)
        break

    else:
        break

print("Answer: ", res)