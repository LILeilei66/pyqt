import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplitter, QHBoxLayout, QWidget, QLineEdit, QFrame
from PyQt5.QtCore import Qt

class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        line1 = QLineEdit('line1')
        line2 = QLineEdit('line2')
        frame = QFrame()


        split1 = QSplitter(Qt.Vertical)
        split1.addWidget(line1)
        # split2 = QSplitter(Qt.Vertical)
        split1.addWidget(line2)

        hbox = QHBoxLayout()
        hbox.addWidget(split1)
        
        # hbox.addWidget(split2)

        main_widget = QWidget()
        main_widget.setLayout(hbox)
        self.setCentralWidget(main_widget)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())