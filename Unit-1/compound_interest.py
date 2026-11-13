principal=int(input("enter the principal value:"))
rate=int(input("enter the rate value:"))
time=int(input("enter the time value:"))
n=int(input("enter the n value:"))
compound_interest=principal*(1+rate/n)**n*time
print(compound_interest)