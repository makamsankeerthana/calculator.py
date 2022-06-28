Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math
print("select an operation to perform: (1 - 6 ")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
print("5.SQUARE ROOT")
print("6.POWER")
operation = input()

if operation == "1": # PERFORM ADDITION
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) + int(num2)))
elif operation == "2": # PERFORM SUBTRACTION
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The difference is " + str(int(num1) - int(num2)))
elif operation == "3": # PERFORM MULTIPLICATION
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The product is " + str(int(num1) * int(num2)))
elif operation == "4": # PERFORM DIVISION
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The result is " + str(int(num1) / int(num2)))
elif operation == "5": # PERFORM SQUARE ROOT
    num = int(input("Enter number: "))
    print("The square root is %f " %(math.sqrt(num)))
elif operation == "6": # SQUARE A NUMBER
    num = int(input("Enter number: "))
    print("The result is %d " %(pow(num, 2)))

else:
    print("invalid entry")
