# Name:        Legend Addition to the Second Page of PDF Documents
# Purpose:      This script sources a list of PDF files in a defined folder,
#                   determines which PDFs will require the properly-oriented 
#                   second page, and attaches that page to each of the PDFs
#                   while producing a new PDF with an adjusted file name. 
#
#                   While this was initially meant for map files, it can be
#                   adjusted to apply a postscript page to PDF documents.
#
# Author:      Daniel Raleigh
#
# Created:     11 August 2022
# Copyright:   (c) draleig 2022
# 
#-------------------------------------------------------------------------------


import os, PyPDF2


# Define Data Locations and Other Variables
Products = r"C:\Map_Product_Folder"
Legend_Portrait = r"C:\Legend_Portrait.pdf"
Legend_Landscape = r"C:\Legend_Landscape.pdf"

Base_Portraits = ['Minnesota', 'Idaho', 'New Hampshire', 'Vermont']
Base_Landscapes = ['South Dakota', 'North Dakota', 'Kansas', 'Tennessee']
PDFs_List = []
PDFs_Portrait = []
PDFs_Landscape = []


# Define workspace and sort map products into specific categories
os.chdir(Products)
PDFs_List = os.listdir(Products)
for PDF in PDFs_List:
	for P in Base_Portraits:
		if PDF.endswith(P+".pdf"):
			PDFs_Portrait.append(PDF)
	for L in Base_Landscapes:
		if PDF.endswith(L+".pdf"):
			PDFs_Landscape.append(PDF)

print('Portrait PDFs: ', PDFs_Portrait)
print('Landscape PDFs: ', PDFs_Landscape)


for PDF in PDFs_Portrait:
    PDFReader = PyPDF2.PdfFileReader(open(PDF, 'rb'))
    PLegendReader = PyPDF2.PdfFileReader(open(Legend_Portrait, 'rb'))
    PpdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(PDFReader.numPages):
        PPageObj = PDFReader.getPage(pageNum)
        PpdfWriter.addPage(PPageObj)
    for pageNum in range(PLegendReader.numPages):
        PLPageObj = PLegendReader.getPage(pageNum)
        PpdfWriter.addPage(PLPageObj)
    PpdfOutput = open(PDF[:-4]+"_Final.pdf", 'wb')
    PpdfWriter.write(PpdfOutput)
    PpdfOutput.close()


for PDF in PDFs_Landscape:
    PDFReader = PyPDF2.PdfFileReader(open(PDF, 'rb'))
    LLegendReader = PyPDF2.PdfFileReader(open(Legend_Landscape, 'rb'))
    LpdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(PDFReader.numPages):
        LPageObj = PDFReader.getPage(pageNum)
        LpdfWriter.addPage(LPageObj)
    for pageNum in range(LLegendReader.numPages):
        LLPageObj = LLegendReader.getPage(pageNum)
        LpdfWriter.addPage(LLPageObj)
    LpdfOutput = open(PDF[:-4]+"_Final.pdf", 'wb')
    LpdfWriter.write(LpdfOutput)
    LpdfOutput.close()