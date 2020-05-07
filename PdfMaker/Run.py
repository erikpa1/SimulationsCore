import os

from PdfMaker.PdfDocument import  PdfDocument
from PdfMaker.PdfTemplateParser import PdfTemplateParser

from Console import expand_console_to_builtins

expand_console_to_builtins()

pdfPath = 'tuto1.pdf'
sourcePath = 'TestData/example.xml'

document = PdfDocument()
parser = PdfTemplateParser(document)
parser.Parse(sourcePath, pdfPath)

os.system(pdfPath)




