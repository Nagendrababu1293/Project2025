import openpyxl
import csv

wb = openpyxl.load_workbook(r'C:\Users\P N Babu\Documents\TestData.xlsx')
sheet = wb.active
for row in sheet.iter_rows(values_only =True):
    print(row)


with open(r'C:\Users\P N Babu\Documents\Test_Data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open(r'C:\Users\P N Babu\Desktop\pytest exucution.txt') as txtfile:
    lines = txtfile.readlines()
    for line in lines:
        print(line)