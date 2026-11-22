name = input("Enter name: ")
age = int(input("Enter age: "))

# Using format()
print("My name is {} and I am {} years old.".format(name, age))

# Using f-string
print(f"My name is {name} and I am {age} years old.")

# Using % operator
print("My name is %s and I am %d years old." % (name, age))