n = int(input("Enter number of elements: "))
items = []

for i in range(n):
   value = input("Enter element: ")
   items.append(value)

print("List elements:")
for item in items:
    print()