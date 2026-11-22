rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")

for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")