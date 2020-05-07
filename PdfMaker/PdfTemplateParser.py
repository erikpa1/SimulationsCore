from PdfMaker.PDFDocument import *

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

class PdfTemplateParser():

    _root: ET.Element = None
    _body: ET.Element = None

    _tagsParsers: {} = None




    def __init__(self, pdfDocument):
        self._document: Document = pdfDocument
        self._dataToParse = ""
        self._root : ET.Element = None
        self._body: ET.Element = None

        self._tagsParsers = {

            "styles": self._ParseStyles,
            "constants": self._ParseConstants,
            "variables": self._ParseConstants,
            "externals": self._parseExternals,

            "title": self._ParseTitle,
            "header": self._ParseHeader,
            "footer": self._ParseFooter,
            "body": self._ParseBody,

            "content": self._parseContent,

            "h1": self._ParseH1,
            "p": self._ParseParagraph,
            "pagebreak": self._ParsePageBreak

        }





    def Parse(self,fileToParse, exportPath):
        self._root = ET.parse(fileToParse).getroot()
        self._body = self._root.find("body")

        self._ParseTitle()
        self._ParseHeader()
        self._ParseBody()
        self._ParseFooter()

        self._document.SaveDoc(exportPath)
        pass

    def _ParseTitle(self):
        title: ET.Element = self._root.find("title")

        self._document.set_title(title.text)
        pass

    def _ParseHeader(self):
        header: ET.Element = self._root.find("header")

        self._document._headerText = header.text
        pass

    def _ParseFooter(self):
        footer: ET.Element = self._root.find("footer")

        self._document._footerText = footer.text
        pass

    def _ParseBody(self):

        self._document.add_page()

        body: ET.Element = self._root.find("body")

        self._document._footerText = body.text

        for ele in body.iter():
            self._tagsParsers[ele.tag]

        pass

    def _ParseParagraph(self, element: ET.Element):

        self._document.multi_cell(0, 0, element.text)
        pass

    def _ParseExpressions(self):
        pass

    def _ParsePageBreak(self):
        pass

    def _ParseH1(self):
        pass

    def _ParseStyles(self):
        pass

    def _ParseConstants(self):
        pass

    def _ParseVariables(self):
        pass

    def _parseExternals(self):
        pass

    def _parseContent(self):
        pass



