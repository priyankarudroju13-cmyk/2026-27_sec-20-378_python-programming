n=int(input("enter the n value(1-100):"))
count=0
for i in range(1,n+1):
 if n%1==0:
    count+=1
if count==2:
    print("prime number")
else:
    print("not a prime number")