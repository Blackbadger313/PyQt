# Creating Simple GUI App

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

#Define Method
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title="PyQt5 Simple By Farid"
        self.left=10
        self.top=10
        self.width=640
        self.height=480
        self.initUI()

    #Define Title
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        
        #Create Button
        button = QPushButton("Press the button", self)
        button.setToolTip("Example button")
        button.move(100,70)
        button.clicked.connect(self.on_click)

        self.show()

    #click action method
    @pyqtSlot()
    def on_click(self):
        a = 10
        b = 5
        print(a+b)

#Main method
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())