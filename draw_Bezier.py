import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QPainterPath
from PyQt5.QtCore import Qt

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        self.drawBezier(qp)
        qp.end()

    def drawBezier(self, qp):
        path = QPainterPath()
        path.cubicTo(30,30,200,350,350,30)

        qp.drawPath(path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())