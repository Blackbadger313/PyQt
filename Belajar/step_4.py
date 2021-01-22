# Creating Simple GUI App

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

#Define Method
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title="PyQt5 Simple By Farid"
        self.left=10
        self.top=10
        self.width=400
        self.height=140
        self.initUI()

    #Define Title
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.textbox = QLineEdit(self)
        self.textbox.move(50,20)
        self.textbox.resize(280, 40)

        #Create Button
        self.button = QPushButton("Show Text", self)
        self.button.setToolTip("Example button")
        self.button.move(50,80)
        self.button.clicked.connect(self.on_click)

        self.show()

    #click action method
    @pyqtSlot()
    def on_click(self):
        textboxvalue = self.textbox.text()
        QMessageBox.question(self,'Message',"You typed:"+textboxvalue,QMessageBox.Ok,QMessageBox.Ok)
        self.textbox.setText("")

#Main method
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())