items = input("Enter values separated by spaces: ").split()
t = tuple(items)
print("Tuple:", t)
if len(t) > 0:
 print("First element:", t[0])
 print("Last element:", t[-1])
