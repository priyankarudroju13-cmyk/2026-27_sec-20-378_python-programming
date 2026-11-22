def simple_interest(principal, time, rate=5):
 return principal * time * rate / 100

print("Default rate:", simple_interest(1000, 2))
print("Explicit rate:", simple_interest(1000, 2, 8))