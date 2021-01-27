# Creating Simple GUI App
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog, QDialogButtonBox, QFormLayout, QGridLayout,
                            QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox,
                            QTextEdit, QVBoxLayout)
import sys


#Define Method
class Dialog(QDialog):
    NumGridRows = 3
    NumButtons = 4
    #Define Title
    def __init__(self):
        super(Dialog, self).__init__()
        b1 = QPushButton("Button 1")
        b2 = QPushButton("Button 2")
        b3 = QPushButton("Button 3")
        b4 = QPushButton("Button 4")

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(b1)
        mainLayout.addWidget(b2)
        mainLayout.addWidget(b3)
        mainLayout.addWidget(b4)

        self.setLayout(mainLayout)
        self.setWindowTitle("Form Layout")

#Main method
if __name__=='__main__':
    app=QApplication(sys.argv)
    dialog=Dialog()
    sys.exit(dialog.exec_())