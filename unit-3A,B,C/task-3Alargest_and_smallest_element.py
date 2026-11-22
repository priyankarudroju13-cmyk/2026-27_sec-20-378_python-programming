n = int(input("Enter number of elements: "))
nums = []

for i in range(n):
 nums.append(int(input("Enter number: ")))
 
if n > 0:
 print("Largest element:", max(nums))
 print("Smallest element:", min(nums))
else:
 print("List is empty")