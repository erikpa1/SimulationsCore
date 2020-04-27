from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton

class MainMenu(object):

    _layout : QHBoxLayout
    _btn1 : QPushButton
    _btn2 : QPushButton

    def __init__(self):
        self._btn1 = QPushButton("Files")
        self._btn2 = QPushButton("Settings")

        self._layout = QHBoxLayout()
        self._layout.addWidget(self._btn1)
        self._layout.addWidget(self._btn2)
        pass


    def GetLayout(self):
        return self._layout



    pass
