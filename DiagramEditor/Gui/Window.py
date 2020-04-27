from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

from DiagramEditor.Gui.MainMenu import *
from DiagramEditor.Gui.BottomMenu import *


class Window(QWidget):

    _layout: QVBoxLayout
    _label : QLabel


    _mainMenu: MainMenu
    _bottomMenu: BottomMenu

    def __init__(self):
        super().__init__()
        self._layout = QVBoxLayout()
        self.setWindowTitle("ESim")
        self.setGeometry(300, 300, 300, 150)
        self.setLayout(self._layout)

        self._label = QLabel("Hello")

        self._mainMenu = MainMenu()
        self._layout.addLayout(self._mainMenu.GetLayout())
        self._layout.addWidget(self._label)

        self._bottomMenu = BottomMenu()
        self._layout.addLayout(self._bottomMenu.GetLayout())
        pass