#! /usr/bin/env python
import sys
import csv
import subprocess
import os
def creator():
	dir_list = subprocess.check_output("ls departments/", shell=True)
	for directory in dir_list.split("\n")[:len(dir_list.split("\n"))-1]:
		file_list=subprocess.check_output("ls departments/"+directory,shell=True)
		
		for doc in file_list.split("\n")[:len(file_list.split("\n"))-1]:
			
			master = open("departments/"+directory+"/"+directory+"_1.csv","wt")
			writer = csv.writer(master)
			
			inf = open("departments/"+directory+"/"+doc)
			for line in inf:
				writer.writerow([line])
			inf.close()
			master.close()
			master = open("departments/"+directory+"/"+directory+"_1.csv","rt")
			master2 = open("departments/"+directory+"/"+directory+".csv","wt")
			writer = csv.writer(master2)
			for line in master:
				if '"' in line:
					line=line.replace('"','')
				writer.writerow([line])
			master.close()
			os.system("rm -r departments/"+directory+"/"+directory+"_1.csv")
			master2.close()
if __name__=="__main__":
	creator()
