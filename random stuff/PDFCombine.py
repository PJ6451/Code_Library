from PyPDF2 import PdfWriter
from os import walk

mypath = r'C:\Users\16617\Downloads\merge'

_, _, pdfs = next(walk(mypath))

merger = PdfWriter()

for pdf in pdfs:
    merger.append(mypath + '\\' + pdf)

merger.write(mypath + '\\' + 'CombinedPDF.pdf')
merger.close

#