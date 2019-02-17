#!/usr/bin/env python
import os
import subprocess
def main():
	major_list=subprocess.check_output("ls ../allMaps/pngFiles/",shell=True).split("\n")
	begin_payload = "<!DOCTYPE html> \n<html> \n<body> \n"
	end_payload="</body> \n</html>"
	for i in major_list:
		if i!= " " and i !="":
			n = i.replace(".png",".html")
			os.system("touch htmlPages/"+ n)
			outf = open("htmlPages/"+n,"w")
			outf.write(begin_payload+"<img src= '../../allMaps/pngFiles/"+i+"' alt='"+i.replace(".png","")+"'> \n"+end_payload)
			outf.close()
if __name__=="__main__":
	main()
