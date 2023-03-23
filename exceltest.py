import openpyxl

workbook = openpyxl.load_workbook('av.xlsx')
sheet = workbook['S1200-IK']
header = [cell.value for cell in sheet[1]]