try:
    a = int(input("enter the a value:"))
    b =int(input("enter the b value:"))
    result = a / b
    print("Result:",result)
except ZeroDivisionError:
    print("Cannot divide by zero.")