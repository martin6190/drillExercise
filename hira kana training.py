import xlrd 

loc = ("drill list.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
print(sheet.cell_value(1, 1)) 

#print(u"あ")

