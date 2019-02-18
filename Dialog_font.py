import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFontDialog
from PyQt5.QtGui import QFont
from Ui_test import Ui_window

class Mainwindow(QMainWindow, Ui_window):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.SetupUi()
        self.btn1.clicked.connect(self._set_font)
        self.btn2.clicked.connect(self._create_font)

    def _set_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.line1.setText(str(font.family()))
            self.line1.setFont(font)

    def _create_font(self):
        font = QFont()
        font.setFamily('Arial')
        font.setBold(True)
        font.setPointSize(12)
        self.line2.setFont(font)
        self.line2.setStyleSheet("color: red")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())