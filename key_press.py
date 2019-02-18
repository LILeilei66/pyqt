import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from Ui_test import Ui_window

"""
重写时间处理器
"""

class Mainwindow(QMainWindow, Ui_window):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.SetupUi()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())
