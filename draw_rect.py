import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPen, QPainter, QBrush
from PyQt5.QtCore import Qt, QRect

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRect(qp)
        qp.end()

    def drawRect(self,qp):
        qp.setBrush(QBrush(Qt.red)) # 实心
        # qp.setPen(QPen(Qt.red)) # 只有外框
        rect = QRect(0,0,self.height()/3, self.width()/3)
        qp.drawRect(rect)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())