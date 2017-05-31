#!/usr/bin/env python
import sys
import os
import csv
import subprocess
def all_courses():
	master = open("entire.csv","a")
	writer = csv.writer(master)
	file_list=subprocess.check_output("ls majors/",shell=True)
	for i in file_list.split("\n"):
		
		if ".csv" in i:
			csv_file = open("majors/"+i.replace(" ","").replace("'","").replace("[","").replace("]","").replace(",","\n").replace("crse_nbr;rltd_crse_nbr\n","").replace("set(","").replace(")",""))
			for line in csv_file:
				writer.writerow([line])
	master.close()
if __name__=="__main__":
	all_courses()
