def marks_result(m1, m2, m3):
 total = m1 + m2 + m3
 average = total / 3
 return total, average
a = float(input("Enter first subject marks: "))
b = float(input("Enter second subject marks: "))
c = float(input("Enter third subject marks: "))
total, average = marks_result(a, b, c)
print("Total marks:", total)
print("Average marks:", average)