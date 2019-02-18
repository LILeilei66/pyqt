import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QComboBox, QHBoxLayout, QLabel, QPushButton, QWidget

class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.btn = QPushButton()
        self.lbl = QLabel('lbl')

        combo = QComboBox(self)
        combo.addItem('1')
        combo.addItem('2')

        hbox = QHBoxLayout()
        hbox.addWidget(self.lbl)
        hbox.addWidget(combo)

        main_widget = QWidget()
        main_widget.setLayout(hbox)
        self.setCentralWidget(main_widget)

        combo.currentTextChanged.connect(self.change_lbl)

    def change_lbl(self, string):
        self.lbl.setText(string)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())