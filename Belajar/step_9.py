# Creating Simple GUI App

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileSystemModel, QTreeView, QVBoxLayout
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
        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.show()

        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)

        self.tree.setWindowTitle("DirView by Farid")
        self.tree.resize(640,480)

        WindowsLayout = QVBoxLayout()
        WindowsLayout.addWidget(self.tree)
        self.setLayout(WindowsLayout)

        self.show()

#Main method
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())