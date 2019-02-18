# TODO: draw text
# https://github.com/LILeilei66/PyQt5-Chinese-tutorial/blob/master/%E7%BB%98%E5%9B%BE.md
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QRect

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text = '深刻搭街坊结果'
        self.setGeometry(200,200,200,200)

    def paintEvent(self, e):
        print('paintevent')
        qp = QPainter()
        qp.begin(self)
        self.drawText(e, qp)
        qp.end()

    def drawText(self, e, qp):
        qp.setPen(QColor(0,0,0))
        rect = QRect(10,10,100,100)
        print('pensetted')
        qp.setFont(QFont('Decorative'))
        qp.drawRect(rect)
        qp.drawText(rect, Qt.AlignCenter, self.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())
