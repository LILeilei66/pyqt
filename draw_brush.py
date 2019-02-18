import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()

    def drawBrushes(self, qp):
        qp.setBrush(QBrush(Qt.red, Qt.CrossPattern))
        qp.drawRect(0,0,self.width()/2, self.height())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())