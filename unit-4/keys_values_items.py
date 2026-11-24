student = {"name": "Priya", "age": 18, "marks": 90}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Name:", student.get("name"))

student.update({"age": 19})
student.pop("marks")

print("Updated Dictionary:", student)