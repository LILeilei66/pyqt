
from PyQt5.QtWidgets import QWidget, QSlider, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, pyqtSignal, QRect, QObject
from PyQt5.QtGui import QPainter, QPen
import sys

"""
1. 每次要repaint；
2. 让text写在中间：
    metrics = qp.fontMetrics()
    fw = metrics.width(str(to_be_texted))
    qp.drawText()

"""

class Communicate(QObject):
    signal = pyqtSignal(int)

class BurningWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setMinimumSize(30, 30)
        self.value = 75
        self.num = [75,150,225,300,375,450,525,600,675]

    def setValue(self, value):
        self.value = value

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()

    def drawWidget(self,qp):
        height = self.size().height()
        width = self.size().width()
        step = int(round(width / 10))
        till = int((width / 750) * self.value)
        full = int((width / 750) * 700)

        qp.setBrush(Qt.yellow)
        qp.drawRect(0, 0, till, height)

        qp.setPen(QPen(Qt.black, Qt.SolidLine))
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(0, 0, width-1, height-1)

        j = 0

        for i in range(step, 10 * step, step):
            qp.drawLine(i, 0, i, 5)
            metrics = qp.fontMetrics()
            fw = metrics.width(str(self.num[j]))
            qp.drawText(i - fw / 2, height, str(self.num[j]))
            j = j + 1

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.sld = QSlider(Qt.Horizontal)
        self.sld.setValue(75)
        self.sld.setRange(1, 750)

        self.c = Communicate()
        self.wid = BurningWidget()

        vbox = QVBoxLayout()
        vbox.addWidget(self.sld)
        vbox.addWidget(self.wid)

        self.setLayout(vbox)

        self.c.signal.connect(self.wid.setValue)
        self.sld.valueChanged.connect(self.changeValue)

    def changeValue(self, int):
        self.c.signal.emit(int)
        self.wid.repaint()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = Example()
    wid.show()
    sys.exit(app.exec_())