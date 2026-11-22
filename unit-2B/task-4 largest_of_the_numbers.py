n=int(input("enter the n value:"))
largest=int(input("enter number"))
for i in range(n-1):
    num=int(input("enter the num value:"))
    if num > largest:
        largest=num
        print("largest number=",largest)