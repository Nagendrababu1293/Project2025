students=[
    {"Name":"Nagendra", "Age":31, "Course":"Python"},
    {"Name":"Sailu", "Age":25, "Course":"Selenium"},
    {"Name":"Assir", "Age":20, "Course":"Pytest"}
]


input_str = "A3B2C1"
output = ''
for ch  in input_str:
  if ch.isalpha():
     x =ch
  else: 
    d = int(ch)
    output += x*d
output = ''.join(sorted(output))
print(output)
