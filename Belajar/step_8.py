# Creating Simple GUI App
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog, QDialogButtonBox,
                            QFormLayout, QGridLayout, QGroupBox, QHBoxLayout, 
                            QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, 
                            QSpinBox, QTextEdit, QVBoxLayout)
import sys

#Define Method
class Dialog(QDialog):
    NumGridRows = 3
    NumButtons = 4
    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accepted)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.FormGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("Form Layout by Farid")
    
    def createFormGroupBox(self):
        self.FormGroupBox = QGroupBox("Form Layout")
        Layout = QFormLayout()
        Layout.addRow(QLabel("Name: "), QLineEdit())
        Layout.addRow(QLabel("Negara: "), QComboBox())
        Layout.addRow(QLabel("Umur: "), QSpinBox())

        self.FormGroupBox.setLayout(Layout)

#Main method
if __name__=='__main__':
    app=QApplication(sys.argv)
    dialog=Dialog()
    sys.exit(dialog.exec_())