students = {
    "student1": {"name": "Pavan", "marks": 90},
    "student2": {"name": "Ravi", "marks": 85}
}

for student in students.values():
    print("Name:", student["name"])
    print("Marks:", student["marks"])