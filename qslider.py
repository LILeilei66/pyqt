import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QSlider, QLabel, QVBoxLayout, QLCDNumber, QHBoxLayout
from PyQt5.QtCore import Qt

"""
PyQt的组成模块及功能：
    QtCore: 无GUI的核心类库
    QtGui:  窗口系统集成，事件处理，2D绘图，基本成像，字体设置，文本设置
    QtWidgets: 各种UI空间，用于创建传统桌面风格的用户界面

Remarque:
    QLabel 只能显示string类，而不能int类
"""

class Ui_mainwindow(QWidget):
    def SetupUi(self):
        self.qslider = QSlider(Qt.Horizontal)
        self.label = QLabel('0')
        self.lcd = QLCDNumber()

        hlayout = QHBoxLayout()
        hlayout.addWidget(self.label)
        hlayout.addWidget(self.lcd)

        vlayout = QVBoxLayout()
        vlayout.addLayout(hlayout)
        vlayout.addWidget(self.qslider)

        main_widget = QWidget()
        main_widget.setLayout(vlayout)
        self.setCentralWidget(main_widget)

class Mainwindow(QMainWindow, Ui_mainwindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.SetupUi()
        self._create_connection()

    def _create_connection(self):
        self.qslider.valueChanged.connect(self.act_qslider)

    def act_qslider(self):
        value = self.qslider.value()
        self.label.setText(str(value))
        # print(value)
        self.lcd.display(value)
        self

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())
