student ={"Name":"Nagendra",
          "Course":"python",
          "Age":"30",
          "Mobile": 9494902450}
print(student)
for k, v in student.items():
    print(k,":", v)

print(student["Name"])
print(student["Age"])
print(student["Mobile"])

print("---------add new pair in student dict---------")
student["City"]='Hyderabad'
print(student)

print("---------update age value---------")
student["Age"]="31"
print(student)

print("------delete any key---------")
del student["City"]
print(student)

student["Gender"] = "Male"
student["Course"] ='Selenium'


print(int(student["Age"])+1)

for keys in student:
    print(keys)

for values in student.values():
    print(values)

for k, v  in student.items():
    print(k, ":", v)

if "Email" in student:
    print("Emaild is present in student")
else:
    print("Email is not present in student")

student.setdefault("Email", "test@gmail.com")
print(student)