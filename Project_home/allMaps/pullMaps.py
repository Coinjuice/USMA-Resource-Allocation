#!/usr/bin/env python
import os 
import sys
import subprocess
def main():
	
	department_list= subprocess.check_output("ls departments/", shell=True)
	for i in department_list.split("\n"):
		print(i)
		departmentFiles_list= subprocess.check_output("ls departments/"+i, shell=True)
		for f in departmentFiles_list.split("\n"):
			if ".png" in f:
				os.system("cp departments/"+i+"/"+f+" pngFiles")
if __name__=="__main__":
	main()
