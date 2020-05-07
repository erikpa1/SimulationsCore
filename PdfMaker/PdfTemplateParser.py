from PdfMaker.PdfDocument import PdfDocument
from PdfMaker.PdfDocument import FontModifiers
from PdfMaker.PdfVariable import Variable

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element


const_core = "const_core_"

class PdfTemplateParser():

    _root: ET.Element = None
    _body: ET.Element = None

    _tagsParsers: {} = None

    _variables: {str : Variable} = None
    _styles: {} = None
    _constants: {} = None
    _externals: {} = None

    _paragraphCount: int = None

    def __init__(self, pdfDocument):
        self._document: PdfDocument = pdfDocument
        self._dataToParse = ""
        self._root : ET.Element = None
        self._body: ET.Element = None

        self._paragraphCount = 0

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
            "b": self._ParseBold,
            "pagebreak": self._ParsePageBreak
        }

        self._variables = {}
        self._constants = {}

        self.AddCoreConstants()


    def Parse(self,fileToParse, exportPath):
        self._root = ET.parse(fileToParse).getroot()

        self._InitContainers()

        self._ParseTitle()

        self._ParseHeader()

        self._body = self._root.find("body")

        self._ParseBody(self._body)

        self._ParseFooter()

        self._document.SaveDoc(exportPath)
        pass


    def AddCoreConstant(self, key, value):
        self._constants[const_core + key] = value
        pass

    def AddCoreConstants(self):
        import datetime

        x = datetime.datetime.now()

        self.AddCoreConstant("time_year", x.year)
        self.AddCoreConstant("time_month", x.month)
        self.AddCoreConstant("time_day", x.day)

        self.AddCoreConstant("time_hour", x.hour)
        self.AddCoreConstant("time_minute", x.minute)
        self.AddCoreConstant("time_second", x.second)
        pass

    def _InitContainers(self):

        constants: ET.Element = self._root.find("constants")

        for i in constants.iter():
            if (str(i.tag) == "constant"):
                self._constants["const_" + i.attrib["name"]] = i.attrib["value"]

        variables: ET.Element = self._root.find("variables")

        for i in variables.iter():
            if (str(i.tag) == "variable"):
                self._variables["var_" + i.attrib["name"]] = i.attrib["value"]


        pass

    def _ParseTitle(self):
        title: ET.Element = self._root.find("title")

        self._document.set_title(title.text)
        pass

    def _ParseHeader(self):
        header: ET.Element = self._root.find("header")
        text = self.FullParseText(header)
        self._document._headerText = text
        pass

    def _ParseFooter(self):
        footer: ET.Element = self._root.find("footer")
        text = self.FullParseText(footer)
        self._document._footerText = text
        pass

    def _ParseBody(self, body):

        self._document.add_page()

        self._document._footerText =  body.text

        for ele in  body.iter():
            if str(ele.tag) != "body":
                self._tagsParsers[ele.tag](ele)



        pass

    def _ParseParagraph(self, element: ET.Element):

        text = self.FullParseText(element)

        self._document.multi_cell(0, 5, text)
        self._paragraphCount += 1

        pass

    def _ParseExpressions(self, expresion):
        pass

    def FullParseText(self, element: ET.Element):

        newText = str(element.text)

        for key, value in self._constants.items():
            newText = newText.replace("{" + key + "}", str(value))

        for key, value in self._variables.items():
            newText = newText.replace("{" + key + "}", repr(value))

        return newText


    def _ParsePageBreak(self, pageBreak):
        pass

    def _ParseH1(self, headers):

        pass

    def _ParseBold(self, tag):

        self._document.cell(1, 1, tag.text)
        pass

    def _ParseStyles(self, styles):
        pass

    def _ParseConstants(self, constants):
        pass

    def _ParseVariables(self, variables):
        pass

    def _parseExternals(self, externals):
        pass

    def _parseContent(self, content):
        pass



