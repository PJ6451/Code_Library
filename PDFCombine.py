from PyPDF2 import PdfFileMerfger
from os import walk

mypath = r''

_, _, pdfs = next(walk(mypath))

merger = PdfFileMerfger

for pdf in pdfs:
    merger.append(mypath + '\\' + pdf)

merger.write(mypath + '\\' + 'CombinedPDF.pdf')
merger.close

#