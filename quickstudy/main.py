from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

from mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.openmenu.setCheckable(True)
        self.openmenu.clicked.connect(lambda: self.open_menu())
    def open_menu(self):
        if self.openmenu.isChecked():
            self.sidebar.setGeometry(QtCore.QRect(0, 40, 150, 611))
        else:
            self.sidebar.setGeometry(QtCore.QRect(0, 40, 40, 611))
app = QApplication([])
window = MainWindow()
window.show()
app.exec()