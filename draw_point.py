import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print('init')

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self) # Watchout! self!
        self.drawPoints(e, qp)
        qp.end()

    def drawPoint(self, e, qp):
        qp.setPen(QPen(Qt.red, 10)) # QPen(color, size)
        qp.drawPoint(self.width()/2,self.height()/2) # drawPoint(x, y)

    def drawPoints(self, e, qp):
        qp.setPen(QPen(Qt.red, 10))
        for i in range(10):
            qp.drawPoint(self.width()/10*i, self.height()/2) # drawPoint 持续作图

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())