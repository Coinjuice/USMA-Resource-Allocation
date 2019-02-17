#! /usr/bin/env python
import openpyxl as px
import sys
def option_look_up(options, inf, sheet, first, second):
	if "W" and "D" in options:
		try:
			outf= open(sys.argv[6],'w')
			
			outf.write("Data Dictionary:\n"+str(make_dict(inf,sheet,first,second,options)))
		except:
			print usage+"	Output File"
	elif "W" and "E" in options:
		if "M" in options:
			outf= open(sys.argv[8]+".txt",'w')
			toWrite=(str(make_edge_list(inf,sheet,first,second,options)))
			toWrite = toWrite.replace(" ","").replace("'","").replace("[","").replace("]","").replace(",",'\n')
			outf.write(toWrite)
		else:
			outf= open(sys.argv[6],'w')
			toWrite=(str(make_edge_list(inf,sheet,first,second,options)))
			toWrite = toWrite.replace(" ","").replace("'","").replace("[","").replace("]","").replace(",",'\n')
			outf.write(toWrite)
		#except:
		#	print usage
	
	#if "F" in options:
	#	return filterer(filterWord)
	elif "E" in options:
		return str(make_edge_list(inf,sheet,first,second,options))
	elif "D" in options:
		return "Data Dictionary:\n"+str(make_dict(inf,sheet,first,second,options))
	else:
		print usage
def make_edge_list(filename,sheetname,first,second,options):
	data=make_dict(filename,sheetname,first,second,options)
	edge_list=[]
	for k in data.keys():
		for v in data[k]:
			
			edge_list+=[str(k.replace(" ",'')+';'+v.replace(" ",''))]
	return edge_list
def make_dict(filename,sheetname,first,second,options):
	first = str(first).upper()
	second = str(second).upper()
	wb = px.load_workbook(filename)
	inf = wb.active
	p = wb.get_sheet_by_name(name=sheetname)
	courses = dict()
	majors= dict()

	for i in range(1,p.max_row+1):
		if "F" in options:
			
			if sys.argv[8] in str(inf[sys.argv[7]+str(int(i))].value).replace(" ",""):
				
				if inf[first+str(int(i))].value not in courses.keys():
					courses[inf[first+str(int(i))].value]=set()
				else:
					courses[inf[first+str(int(i))].value].add(inf[second+str(int(i))].value)
	#	if "M" in options
	#		if inf[sys.argv[7]+str(int(i)).value] not in majors.keys:
	#			majors
		else:
			if inf[first+str(int(i))].value not in courses.keys():
				courses[inf[first+str(int(i))].value]=set()
			else:
				courses[inf[first+str(int(i))].value].add(inf[second+str(int(i))].value)
	
	return courses

	

if __name__=='__main__':
	usage = "Usage:\n./net_sci_parser.py	Input File	Sheet name	[-WDE]	First column	Second column	[Output File]\n\n Discription:\n	This program is used to orgnaize data from csv files to create corrilations (mainly for network science)\n\n Options:\n	W: write to an output file\n	D: Create a Dictionary\n	E: Create an edge List"
	inf=sys.argv[1]
	sheet=sys.argv[2]
#	try:
	
	if sys.argv[3][0] =='-':
		first_column = sys.argv[4]
		second_column = sys.argv[5]
		options = list(sys.argv[3][1:].upper())
		option_look_up(options, inf, sheet, first_column, second_column)
	else:
		first_column = sys.argv[3]
		second_column = sys.argv[4]
		make_dict(inf,sheet,first_column,second_column)
	#except:
	#	print usage
