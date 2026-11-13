a=int(input("enter the first value:"))
b=int(input("enter the second value:"))
c=int(input("enter the third value:"))
if a<b:
    if a<c:
        print("smallest number:",a)
    else:
        print("smallest number:",c)
else:
    if b<c:
        print("smallest number :",b)
    else:
        print("smallest number :",c)