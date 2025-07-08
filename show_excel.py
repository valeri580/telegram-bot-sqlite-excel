import openpyxl

wb = openpyxl.load_workbook('users.xlsx')
ws = wb['Users']

for row in ws.iter_rows(values_only=True):
    print(row) 