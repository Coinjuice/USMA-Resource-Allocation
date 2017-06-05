#!/usr/bin/env python
# ./option.py 2019_majors.xlsx Sheet1 A C
import os
import subprocess
import sys
import openpyxl as px
import csv
def main(filename,sheetname,major_row,maj_descrip_row):
	major_row = str(major_row).upper()
	maj_descrip_row = str(maj_descrip_row).upper()
	wb = px.load_workbook(filename)
	inf = wb.active
	p = wb.get_sheet_by_name(name=sheetname)
	outf = open("interface.html","a")
	outf.write("<!DOCTYPE html> \n <html>\n<body>\n<select name ='major_name' form='major_request'>")
	for i in range(2,p.max_row+1):
		outf.write("<option value = '"+inf[major_row+str(int(i))].value+"'>"+inf[maj_descrip_row+str(int(i))].value+"</option>")
	outf.write("</select>\n<form action='show_major.php' method='get' id='major_request'>\n<input type='submit'>\n</form>\n</body>\n</html>")
	outf.close()
	
if __name__=="__main__":
	main("../"+sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
