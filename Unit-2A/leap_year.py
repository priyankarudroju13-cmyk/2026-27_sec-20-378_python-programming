#leap year
num=int(input("enter the num value:"))
if num%400==0 or(num%4==0 and num%100!=0):
    print(f"{num}year is a leap year")
else:
    print(f"{num}  year is not leap year") 
