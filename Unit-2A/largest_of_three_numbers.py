a=int(input("enter the first value:"))
b=int(input("enter the second value:"))
c=int(input("enter the third value:"))
if a>=b:
    if a>=c:
        print("largest number:",a)
    else:
        print("largest number:",c)
else:
    if b>=c:
        print("largest number :",b)
    else:
        print("largest number :",c)