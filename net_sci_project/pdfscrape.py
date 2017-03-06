#!/usr/bin/env python
import PyPDF2
pdfFileObj = open('RedBook_GY2018.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pages = pdfReader.getNumPages()
for i in range(1,pages):
	pageObj = pdfReader.getPage(i)
	page=pageObj.extractText()
	print page.encode('utf-8')

