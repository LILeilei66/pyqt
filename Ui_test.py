from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
import sys

class Ui_window(QWidget):
    def SetupUi(self):
        self.btn1 = QPushButton('btn1')
        self.btn2 = QPushButton('btn2')
        self.line1 = QLabel('line1')
        self.line2 = QLabel('line2')

        hlayout1 = QHBoxLayout()
        hlayout1.addWidget(self.btn1)
        hlayout1.addWidget(self.line1)

        hlayout2 = QHBoxLayout()
        hlayout2.addWidget(self.btn2)
        hlayout2.addWidget(self.line2)

        main_layout = QVBoxLayout()
        main_layout.addLayout(hlayout1)
        main_layout.addLayout(hlayout2)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)



    def keyPressEvent(self, e):
        if e.key() == 49:
            self.btn1.click()
        if e.key() == Qt.Key_Escape:
            sys.exit()
        if e.key() == 50:
            self.btn2.click()