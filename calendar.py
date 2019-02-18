from PyQt5.QtWidgets import QCalendarWidget, QDialog
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import QDate
import sys
from Ui_test import Ui_window

class CalDialog(QDialog):
    def __init__(self):
        super(CalDialog, self).__init__()
        self.calendar = QCalendarWidget(self)
# class Mainwindow(QMainWindow):
#     def __init__(self):
#         super(Mainwindow, self).__init__()
#         self.btn1 = QPushButton('btn1')
#         self.line1 = QLineEdit('line1')
#         self.cal = QCalendarWidget()
#
#         hbox = QHBoxLayout()
#         hbox.addWidget(self.btn1)
#         hbox.addWidget(self.line1)
#         hbox.addWidget(self.cal)
#
#         main_widget = QWidget()
#         main_widget.setLayout(hbox)
#         self.setCentralWidget(main_widget)
#
#         self.cal.clicked[QDate].connect(self._change_date)
#
#     def _change_date(self, date):
#         print(date)
#         print(date.toString())
#
#         self.line1.setText(date.toString())


class Mainwindow(QMainWindow, Ui_window):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.SetupUi()

        self.btn1.clicked.connect(self._btn1_action)

        # self.cal.clicked[QDate].connect(self._change_date)

    def _btn1_action(self):
        caldialog = CalDialog()
        caldialog.exec_()
        date = caldialog.calendar.selectedDate()

        self.line1.setText(date.toString())

    def _change_date(self, date):
        print(date)
        print(date.toString())

        self.line1.setText(date.toString())






if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())

