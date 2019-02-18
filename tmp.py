
import sys
from PyQt5.QtWidgets import (QMainWindow, QHBoxLayout, QLabel,
                             QPushButton, QApplication, QLineEdit,
                             QTextBrowser, QVBoxLayout, QWidget)
from PyQt5.QtCore import QThread, QObject, pyqtSignal
import time

class MainWindow(QMainWindow):
    startCalcSignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.init_ui()
        self.init_thread()
        self.init_connect()

    def init_ui(self):
        self.input_data_edit = QLineEdit()
        self.calc_btn = QPushButton('计算')
        calc_layout = QHBoxLayout()
        calc_layout.addWidget(self.input_data_edit)
        calc_layout.addWidget(self.calc_btn)

        info_label = QLabel('进度：')
        info_label_layout = QHBoxLayout()
        info_label_layout.addWidget(info_label)
        info_label_layout.addStretch(1)
        self.info_text = QTextBrowser()

        result_label = QLabel('结果：')
        result_label_layout = QHBoxLayout()
        result_label_layout.addWidget(result_label)
        result_label_layout.addStretch(1)
        self.result_edit = QLineEdit()

        main_layout = QVBoxLayout()
        main_layout.addLayout(calc_layout)
        main_layout.addSpacing(20)
        main_layout.addLayout(info_label_layout)
        main_layout.addWidget(self.info_text)
        main_layout.addSpacing(20)
        main_layout.addLayout(result_label_layout)
        main_layout.addWidget(self.result_edit)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)

    def init_thread(self):
        self.cal_thread = QThread()
        self.cal_thread_obj = Cal_Thread()
        self.cal_thread.start()
        self.cal_thread_obj.moveToThread(self.cal_thread)

    def init_connect(self):
        self.calc_btn.clicked.connect(self.start_cal)

        self.cal_thread_obj.startSignal.connect(self.print_info)
        self.cal_thread_obj.endSignal.connect(self.print_result)

	# TODO: 报错：endsignal无connect method


    def start_cal(self):
        data = self.input_data_edit.text()
        self.cal_thread_obj.start_cal(data)

    def print_info(self):
        self.info_text.setText('print info')

    def print_result(self):
        self.result_edit.setText('print result')


class Cal_Thread(QObject):

    def __init__(self):
        super().__init__()
        self.startSignal = pyqtSignal(str)
        self.endSignal = pyqtSignal(int)

    def start_cal(self, data):
        self.startSignal.emit('start')


        time.sleep(5)
        self.endSignal.emit(data*2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
