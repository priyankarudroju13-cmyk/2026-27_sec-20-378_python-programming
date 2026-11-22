n=int(input("enter the number:"))
n=abs(n)
count=0
while n>0:
    count+=1
    n=n//10
print("number of digits=",count)