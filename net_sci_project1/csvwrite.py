#! /usr/bin/env python

import csv
import subprocess

file_list=subprocess.check_output('ls majors/',shell=True)

#print file_list.split("\n")[:-1]
#print file_list.split("\n")
for doc in file_list.split("\n")[:-1]:

	cdoc=doc.replace(".txt",".csv")
	f=open("majors/"+cdoc,"wt")
	writer = csv.writer(f)
	inf = open("majors/"+doc)
	for line in inf:
		writer.writerow([line])
	f.close()
	inf.close()
#print(open('eve1.csv', 'rt').read())
