import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from Ui_test import Ui_window

"""
不需要将QInputDialog实例化直接用就可以了。
"""


class Mainwindow(QMainWindow, Ui_window):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.SetupUi()

        self._create_connection()

    def _create_connection(self):
        self.btn1.clicked.connect(self._show_dialog)

    def _show_dialog(self):
        text, ok = QInputDialog.getText(self, u'标题', u'信息')
        if ok:
            self.line1.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())