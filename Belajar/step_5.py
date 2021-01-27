# Creating Simple GUI App

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QAction, QMessageBox,QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

#Define Method
class App(QMainWindow, QWidget):
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
        self.textbox.move(20, 30)
        self.textbox.resize(280, 40)

        #create menubar
        mainmenu = self.menuBar()
        filemenu = mainmenu.addMenu('File')
        editmenu = mainmenu.addMenu('Edit')
        viewmenu = mainmenu.addMenu('View')
        searchmenu = mainmenu.addMenu('Search')
        toolmenu = mainmenu.addMenu('Tools')
        helpmenu = mainmenu.addMenu('Help')

        exitButton = QAction('Exit',self)
        exitButton.setShortcut('ctrl+q')
        exitButton.triggered.connect(self.close)
        filemenu.addAction(exitButton)

        self.button = QPushButton("Show It!", self)
        self.button.move(20, 80)
        self.button.clicked.connect(self.click_show)

        self.show()

    @pyqtSlot()
    def click_show(self):
        textboxvalue = self.textbox.text()
        QMessageBox.question(self,'Input',textboxvalue,QMessageBox.Ok,QMessageBox.Ok)
        self.textbox.setText("")

#Main method
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())