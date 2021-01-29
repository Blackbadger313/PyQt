#Convert code to oop from step 13
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

import sys

class FaridWindow(QMainWindow):
    def __init__(self):
        super(FaridWindow,self).__init__()
        self.initUI()
    
    def teken(self):
        print("Oh Hai :) ")
        self.label.setText("Yah ke teken :( ")
        self.label.adjustSize() #adjust size for label when cange

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("PyQt by Farid")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello There")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Send")
        self.b1.move(100,100)
        self.b1.clicked.connect(self.teken)

def muncul():
    app = QApplication(sys.argv)
    win = FaridWindow()
    win.show()
    sys.exit(app.exec_())

muncul()