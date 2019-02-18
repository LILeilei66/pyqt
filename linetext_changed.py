# TODO: https://github.com/maicss/PyQt5-Chinese-tutorial/blob/master/%E6%8E%A7%E4%BB%B62.md

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.line1 = QLineEdit('line1')
        self.line2 = QLineEdit('line2')

        vbox = QVBoxLayout()
        vbox.addWidget(self.line1)
        vbox.addWidget(self.line2)

        main_widget = QWidget()
        main_widget.setLayout(vbox)
        self.setCentralWidget(main_widget)

        self.line1.textChanged[str].connect(self.get_changed)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            sys.exit(0)

    def get_changed(self):
        string = self.line1.text()
        self.line2.setText(string)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())