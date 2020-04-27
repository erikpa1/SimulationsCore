from PyQt5.QtWidgets import QApplication

from DiagramEditor.Gui.Window import *

class App(object):

    _window : Window

    def __init__(self):
        self._window = Window()
        self._window.show()
        pass


    pass


app: QApplication = QApplication([])
myApp: App = App()
app.exec_()
