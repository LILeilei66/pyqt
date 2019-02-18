import sys
from Ui_test import Ui_window
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QObject, pyqtSignal

"""
QObject: 基类，其实例能发送事件信号
1. 创建QObject集成pyqtSignal，并在主程序中实例化
2. 将widget连接至method
3. 通过method emit signal
4. 将每个signal connect到一个method
"""
class Communicate(QObject):
    closeApp = pyqtSignal()
    printApp = pyqtSignal()



class Mainwindow(QMainWindow, Ui_window):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.SetupUi()
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        self.c.printApp.connect(self.line_write)

        self.btn1.clicked.connect(self.act)
        self.btn2.clicked.connect(self.write)

    def act(self):
        self.c.closeApp.emit()

    def write(self):
        self.c.printApp.emit()

    def line_write(self):
        self.line1.setText('Print app emitted.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())
