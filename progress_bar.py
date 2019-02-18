import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QProgressBar, QPushButton, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QBasicTimer

# TODO: timer + 函数调用，是否需要使用多线程？

class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()

        self.line1 = QLabel('line1')
        self.btn1 = QPushButton('btn1')
        self.prg_bar = QProgressBar()

        hbox = QHBoxLayout()
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.line1)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.prg_bar)
        main_layout.addLayout(hbox)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.timer = QBasicTimer()
        self.step = 0

        self.btn1.setShortcut('1')
        self.btn1.clicked.connect(self.btn1_action)

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.line1.setText('>100')
            return
        self.step += 1
        self.prg_bar.setValue(self.step)

    def btn1_action(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(100, self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())

