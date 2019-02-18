from Ui_test import Ui_window
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

"""
目标：找到哪个btn被按下，并且显示在状态栏上
利用self.sender()
sender.text()为组件名称
"""

class Mainwindow(QMainWindow, Ui_window):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.SetupUi()
        self.add_Ui()
        self._create_connection()

    def _create_connection(self):
        # 法一：每个btn连接至不同的method
        # self.btn1.clicked.connect(self._btn1_act)
        # self.btn2.clicked.connect(self._btn2_act)

        # 法二：每个btn连接至同一个method
        self.btn1.clicked.connect(self._btn_act)
        self.btn2.clicked.connect(self._btn_act)

    def _btn1_act(self):
        self.statusBar().showMessage('btn1')

    def _btn2_act(self):
        self.statusBar().showMessage('btn2')

    def _btn_act(self):
        sender = self.sender()
        print(sender)
        self.statusBar().showMessage(sender.text())

    def add_Ui(self):
        self.statusBar()
        self.statusBar().showMessage('Bar created')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())