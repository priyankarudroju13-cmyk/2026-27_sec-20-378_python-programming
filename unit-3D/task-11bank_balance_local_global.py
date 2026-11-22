balance = 1000

def deposit(amount):
 global balance
 balance += amount

def local_change():
 balance = 0 # local variable
 balance -= 100
print("Local balance:", balance)

deposit(500)
local_change()
print("Account balance:", balance)