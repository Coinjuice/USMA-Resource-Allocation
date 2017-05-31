#! /usr/bin/env python
#./filter_departments.py 2019_majors.xlsx Sheet1 A B

import sys
import openpyxl as px
import os
import subprocess
def create_department(filename,sheetname,major_row,department_row):
	major_row = str(major_row).upper()
	department_row = str(department_row).upper()
	wb = px.load_workbook(filename)
	inf = wb.active
	p = wb.get_sheet_by_name(name=sheetname)
	
	os.system("mkdir departments")
	for i in range(2,p.max_row+1):
		file_list=subprocess.check_output("ls departments/",shell=True)
		department = inf[department_row+str(int(i))].value
		if department not in file_list:
			os.system("mkdir departments/"+ department)
		major_list= subprocess.check_output("ls majors/", shell=True)
		

		for m in major_list.split("\n"):
			
			if m.replace(".csv","").replace(".txt","") == inf[major_row+str(int(i))].value:
				os.system("cp majors/"+m +" "+"departments/"+department)

if __name__=="__main__":
	filename=sys.argv[1]
	sheetname=sys.argv[2]
	major_row=sys.argv[3]
	department_row=sys.argv[4]
	create_department(filename,sheetname,major_row,department_row)
