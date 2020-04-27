from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton

class BottomMenu(object):

    _layout : QHBoxLayout
    _btn1 : QPushButton

    def __init__(self):
        self._btn1 = QPushButton("Testing")

        self._layout = QHBoxLayout()
        self._layout.addWidget(self._btn1)
        pass


    def GetLayout(self):
        return self._layout



    pass
