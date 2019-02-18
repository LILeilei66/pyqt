from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag
import sys

class Drag_btn(QPushButton):
    def __init__(self, title):
        super().__init__(title)

    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.RightButton:
            return

        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        print(e.pos())
        drag.setHotSpot(e.pos())
        dropAction = drag.exec_(Qt.MoveAction)
    #
    # def mousePressEvent(self, e):
    #     super().mouseMoveEvent(e)
    #
    #     if e.button() == Qt.LeftButton:
    #         print('press')

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.btn = Drag_btn('drag_btn')
        self.setAcceptDrops(True)
        self.btn.setFixedSize(20,20)
        self.setCentralWidget(self.btn)
        self.setGeometry(300,300,280,140)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()
        self.btn.move(position)
        e.setDropAction(Qt.MoveAction)
        e.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())
