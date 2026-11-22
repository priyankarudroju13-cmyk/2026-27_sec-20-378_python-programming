n=int(input("enter how many numbers:"))
total=0
for i in range(n):
    num=int(input("enter the num value:"))
    total += num
    if n>0:
        average =total/n
        print("sum=",total)
        print("average=",average)
    else:
        print("enter the positive number")
