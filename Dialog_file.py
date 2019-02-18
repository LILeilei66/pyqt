import sys
import os
from Ui_test import Ui_window
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

class Mainwindow(QMainWindow, Ui_window):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.SetupUi()
        self.btn1.clicked.connect(self._get_file)

    def _get_file(self):
        fp = QFileDialog.getOpenFileName(self, '.', '.')
        fp = fp[0]
        self.line1.setText(fp)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())