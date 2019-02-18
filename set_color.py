import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QColorDialog
from Ui_test import Ui_window

"""
QFrame: Base class of widgets that can have a frame.
"""


class Mainwindow(QMainWindow, Ui_window):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.SetupUi()
        self.btn1.clicked.connect(self.change_frame_color)

    def change_frame_color(self):
        self.setStyleSheet("background-color : red")
        self.line1.setStyleSheet("background-color : green")
        color = QColorDialog.getColor()
        if color.isValid():
            self.line2.setStyleSheet("background-color : {:s}".format(color.name()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())