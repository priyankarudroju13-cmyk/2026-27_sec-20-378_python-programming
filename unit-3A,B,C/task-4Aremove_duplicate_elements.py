items = [1, 2, 2, 3, 4, 3, 5]
unique = []

for item in items:
 if item not in unique:
   unique.append(item)

print("Original list:", items)
print("List without duplicates:", unique)