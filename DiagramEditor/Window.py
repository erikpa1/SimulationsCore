from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel


def CreateWindow():

    app = QApplication([])
    label = QLabel("Hello")
    label.show()
    app.exec()


CreateWindow()


