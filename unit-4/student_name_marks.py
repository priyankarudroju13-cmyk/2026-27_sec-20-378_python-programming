name =input("enter student name:")
marks =int(input("enter the marks:"))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"

dict_data = {"Name":name , "Marks": marks, "Grade": grade}
print("Record:", dict_data)
for key, value in dict_data.items():
    print(f"{key}: {value}")