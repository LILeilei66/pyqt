import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_test import Ui_window

"""
利用内置函数
"""

class Mainwindow(QMainWindow, Ui_window):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.SetupUi()
        self.setMouseTracking(True)


    def mousePressEvent(self,e):
        """
        点击显示坐标
        :param e:
        :return:
        """
        x = e.x()
        y = e.y()
        self.btn1.setText(str(x))
        self.btn2.setText(str(y))

    def mouseMoveEvent(self, e):
        """
        拖动显示坐标
        :param e:
        :return:
        """
        self.line1.setText(str(e.x()))
        self.line2.setText(str(e.y()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec())

