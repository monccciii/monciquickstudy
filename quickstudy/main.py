from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore, QtGui, QtWidgets

from mainwindow import Ui_QuickStudy

class MainWindow(QMainWindow, Ui_QuickStudy):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.openmenu.setCheckable(True)
        self.openmenu.clicked.connect(lambda: self.open_menu())
        self.createset.clicked.connect(lambda: self.open_create_set())
    def open_create_set(self):
        layout = self.Header
        
        #self.label1 = QtWidgets.QLabel(self.Header)
        #font = QtGui.QFont()
        #font.setPointSize(14)
        #font.setBold(True)
        #font.setWeight(75)
        #self.label1.setFont(font)
        #self.label1.setObjectName("headertext")
        #self.gridLayout_2.addWidget(self.label, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        #self.label1.setText('hi')
        #self.Header = QtWidgets.QLabel(self.Header)
        #self.Header.setGeometry(QtCore.QRect(10, 10, 31, 23))
        #self.Header.setText("hi")

        pass
    def open_menu(self):
        if self.openmenu.isChecked():
            self.sidebar.setGeometry(QtCore.QRect(0, 40, 150, 611))
           # self.animation1 = QtCore.QPropertyAnimation(self.sidebar, b"maximumWidth")
            #self.animation1.setDuration(500)
            #self.animation1.setStartValue(40)
            #self.animation1.setEndValue(150)
            #self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            #self.animation1.start()

            #self.animation1 = QtCore.QPropertyAnimation(self.sidebar, b"minimumWidth")
            #self.animation1.setDuration(500)
            #self.animation1.setStartValue(40)
            #self.animation1.setEndValue(150)
            #self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            #self.animation1.start()
        else:
            self.sidebar.setGeometry(QtCore.QRect(0, 40, 40, 611))
app = QApplication([])
window = MainWindow()
window.show()
app.exec()