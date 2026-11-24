name = input("Enter student name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")

student = {
    "name": name,
    "age": age,
    "course": course
}

print("Original Dictionary:", student)

student["age"] = int(input("Enter updated age: "))
student["city"] = input("Enter city: ")

print("Updated Dictionary:", student)