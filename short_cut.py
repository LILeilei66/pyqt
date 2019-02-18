import sys
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QMainWindow, QApplication
from PyQt5.QtWidgets import QHBoxLayout

class Ui_Mainwindow(QWidget):
    def SetupUi(self):
        self.btn = QPushButton('btn')
        self.lbl = QLabel('lbl')

        hbox = QHBoxLayout()
        hbox.addWidget(self.btn)
        hbox.addWidget(self.lbl)

        main_widget = QWidget()
        main_widget.setLayout(hbox)
        self.setCentralWidget(main_widget)

class Mainwindow(QMainWindow, Ui_Mainwindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.SetupUi()
        self.btn.setShortcut('1') # 与改变 KeyPressEvent() 效果相同


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())
