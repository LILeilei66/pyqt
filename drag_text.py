import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QHBoxLayout, QWidget, QLabel

"""
只有QLineEdit支持被拖动。
但是，可以通过mouseEvent和global Mapping组合来实现拖动。
"""

class Drag_btn(QPushButton):
    def __init__(self, title):
        super().__init__(title)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())





class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()

        self.line1 = QLineEdit('line1')
        self.btn1 = Drag_btn('btn1')

        hbox = QHBoxLayout()
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.line1)

        main_widget = QWidget()
        main_widget.setLayout(hbox)
        self.setCentralWidget(main_widget)

        self.btn1.setAcceptDrops(True)
        self.line1.setDragEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())