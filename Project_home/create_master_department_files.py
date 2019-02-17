#! /usr/bin/env python
import sys
import csv
import subprocess
def creator():
	dir_list = subprocess.check_output("ls departments/", shell=True)
	for directory in dir_list.split("\n")[:len(dir_list.split("\n"))-1]:
		file_list=subprocess.check_output("ls departments/"+directory,shell=True)
		
		for doc in file_list.split("\n")[:len(file_list.split("\n"))-1]:
			
			masterCSV = open("departments/"+directory+"/"+directory+".csv","wt")
			masterTXT = open("departments/"+directory+"/"+directory+".txt","w")
			writer = csv.writer(masterCSV)
			
			inf = open("departments/"+directory+"/"+doc)
			for line in inf:
				writer.writerow([line])
				masterTXT.write(line)
			masterCSV.close()
			masterTXT.close()
			inf.close()
if __name__=="__main__":
	creator()
