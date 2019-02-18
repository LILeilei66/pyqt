
import  sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QMessageBox
from PyQt5.QtCore import Qt

class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.cb1 = QCheckBox('1', self)
        # self.cb1.toggle() # toggle()决定预设值是否为勾选状态

        self.cb1.stateChanged.connect(self.change_cb1)

    def change_cb1(self, state):
        if state == Qt.Checked:
            QMessageBox.information(self, 'cb1', 'cb1')
        else:
            QMessageBox.information(self, 'no', 'no')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())
