#! /usr/bin/env python
import openpyxl as px
import sys
import csv
import subprocess
def make_major_dict(filename,sheetname,first,second,third):
	first = str(first).upper()
	second = str(second).upper()
	wb = px.load_workbook(filename)
	inf = wb.active
	p = wb.get_sheet_by_name(name=sheetname)
	majors = dict()
	for i in range(1,p.max_row+1):
		
		
		
		if inf[second+str(int(i))].value not in majors.keys():
			majors[inf[second+str(int(i))].value] = set()
		majors[inf[second+str(int(i))].value].add(inf[third+str(int(i))].value)
		
		edge_list = set()
		for k in majors.keys():
			for v in majors[k]:
				edge_list.add(str(k.replace(" ","")+';'+v.replace(" ",'')))
		
		to_insert=str(edge_list).replace(" ","").replace("'","").replace("[","").replace("]","").replace(",","\n").replace("crse_nbr;rltd_crse_nbr\n","").replace("set(","").replace(")","")
		maj_outf = open("majors/"+inf[first+str(int(i))].value+".txt","w")
		
		
		maj_outf.write(to_insert)
		maj_outf.close()
	file_list=subprocess.check_output('ls majors/',shell=True)
	for doc in file_list.split("\n")[:-1]:

		cdoc=doc.replace(".txt",".csv")
		f=open("majors/"+cdoc,"wt")
		writer = csv.writer(f)
		inf = open("majors/"+doc)
		for line in inf:
			writer.writerow([line])
		f.close()
		inf.close()
	return majors
if __name__=='__main__':
	inf = sys.argv[1]
	sheet = sys.argv[2]
	major = sys.argv[3]
	course = sys.argv[4]
	prereq = sys.argv[5]
	make_major_dict(inf,sheet,major,course,prereq)
