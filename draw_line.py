import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPen, QPainter
from PyQt5.QtCore import Qt

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        qp.setPen(QPen(Qt.red, Qt.DashDotLine))
        qp.drawLine(0, self.height()/2, self.width(), self.height()/2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())