
from fpdf import FPDF


from PdfMaker.TestingText import *

class Orientation:
    PORTRAIT = 'P'
    LANDSCAPE = 'l'
    pass

class Units:
    MM = 'mm'
    PT = 'pt'
    CM = 'cm'
    IN = 'in'

class Format:
    A4 = 'A4'
    LETTER = 'Letter'
    LEGAL = 'Legal'

class Fonts:
    TIMES_NEW_ROMAN = 'Times'

class FontModifiers():
    NONE = ''
    BOLD = 'B'
    ITALIC = 'I'
    UNDERLINE = 'U'



class PdfDocument(FPDF):

    _headerText: str = ""
    _footerText: str = ""

    def __init__(self):

        super().__init__(Orientation.PORTRAIT, Units.MM, Format.A4)

        self.set_margins(left = 10, top = 10, right = 10)
        self.set_font("Times", FontModifiers.NONE, 12)
        self.set_auto_page_break(True, 1)

        self._headerText = ""
        self._footerText = ""


    def SaveDoc(self, path):
        self.output(path, 'F')
        pass

    def PrintChapter(self, name = 'My chapter'):
        self.add_page()
        self.chapter_title(1, name)
        self.set_title(name)
        #self.chapter_body(name)

    def header(self):
        self.cell(80)
        self.cell(30, 10, self._headerText, 0, 0, 'C')
        self.ln(20)
        pass

    def footer(self):
        self.set_y(-15)
        self.cell(80)
        self.cell(30, 10, self._footerText)
        pass

    def chapter_title(self, num, label):
        self.set_font('Arial', '', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, name):
        # Read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        self.cell(0, 5, '(end of excerpt)')



