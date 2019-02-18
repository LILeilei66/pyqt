import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QColorDialog
from Ui_test import Ui_window

class Mainwindow(QMainWindow, Ui_window):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.SetupUi()
        self.btn1.clicked.connect(self._show_color_dialog)


    def _show_color_dialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            print(color.value())
            print(color.name())
            self.line1.setText(color.name())
            self.btn1.setStyleSheet("background-color: {:s}".format(color.name()))
            self.btn1.setStyleSheet("color: {:s}".format(color.name()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())

