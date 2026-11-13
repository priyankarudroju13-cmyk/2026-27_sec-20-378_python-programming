a=int(input("enter the first angle:"))
b=int(input("enter the second angle:"))
c=int(input("enter the third value:"))
total=a+b+c
if a>0 and b>0 and c>0 and total==180:
    print("triangle is valid")
else:
    print("triangle is invalid")