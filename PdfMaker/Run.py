import os

from PdfMaker.PDFDocument import  Document
from PdfMaker.PdfTemplateParser import PdfTemplateParser

from Console import expand_console_to_builtins

expand_console_to_builtins()

pdfPath = 'tuto1.pdf'
sourcePath = 'example.xml'

document = Document()
parser = PdfTemplateParser(document)
parser.Parse(sourcePath, pdfPath)

os.system(pdfPath)




