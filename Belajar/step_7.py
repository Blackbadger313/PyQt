# Creating Simple GUI App

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QHBoxLayout, QDialog, QGroupBox, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

#Define Method
class App(QDialog, QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.title="PyQt5 Simple By Farid"
        self.left=10
        self.top=10
        self.width=320
        self.height=100
        self.initUI()

    #Define Title
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.createHorizontalLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def createHorizontalLayout(self):
        self.horizontalGroupBox = QGroupBox("Wat is your fav color?")
        Layout = QHBoxLayout()

        buttonBlue = QPushButton("Blue", self)
        buttonBlue.clicked.connect(self.on_click)
        Layout.addWidget(buttonBlue)

        buttonRed = QPushButton("Red", self)
        buttonRed.clicked.connect(self.on_click)
        Layout.addWidget(buttonRed)

        buttonGreen = QPushButton("Green", self)
        buttonGreen.clicked.connect(self.on_click)
        Layout.addWidget(buttonGreen)

        self.horizontalGroupBox.setLayout(Layout)

    @pyqtSlot()
    def on_click(self):
        print("button click")

#Main method
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())