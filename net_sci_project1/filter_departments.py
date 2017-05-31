#! /usr/bin/env python
#./filter_departments.py 2019_majors.xlsx Sheet1 A B
import sys
import openpyxl as px
import os
def create_department(filename,sheetname,major_row,department_row):
	major_row = str(major_row).upper()
	department_row = str(department_row).upper()
	wb = px.load_workbook(filename)
	inf = wb.active
	p = wb.get_sheet_by_name(name=sheetname)
	departments={}
	
	for i in range(2,p.max_row+1):
		if inf[department_row+str(int(i))].value not in departments:
			departments[inf[department_row+str(int(i))].value]=set()
		departments[inf[department_row+str(int(i))].value].add(inf[major_row+str(int(i))].value)
	os.system("mkdir departments")
	for k in departments.keys():
		
		os.system("mkdir departments/" +k)
		
		for v in departments[k]:
	#		print v
			os.system("cp majors/"+v+".csv"+" departments/"+k)
if __name__=="__main__":
	filename=sys.argv[1]
	sheetname=sys.argv[2]
	major_row=sys.argv[3]
	department_row=sys.argv[4]
	create_department(filename,sheetname,major_row,department_row)
