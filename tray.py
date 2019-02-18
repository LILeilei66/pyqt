import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import (QSystemTrayIcon, QPushButton, QHBoxLayout,\
                             QMenu, QAction)
from PyQt5.QtGui import QIcon

class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()

        self.btn = QPushButton('To tray')

        hbox = QHBoxLayout()
        hbox.addWidget(self.btn)
        main_widget = QWidget()
        main_widget.setLayout(hbox)
        self.setCentralWidget(main_widget)

        self.btn.clicked.connect(self.to_tray)

    def setupTray(self):
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon('chat.png'))
        self.tray_menu = QMenu(QApplication.desktop())

        self.RestoreAction = QAction('Restore', self, triggered = self.show)
        self.QuitAction = QAction('Exit', self, triggered=sys.exit)

        self.tray_menu.addAction(self.RestoreAction)
        self.tray_menu.addAction(self.QuitAction)
        self.tray.setContextMenu(self.tray_menu)


    def to_tray(self):
        self.hide()
        self.setupTray()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec_())
