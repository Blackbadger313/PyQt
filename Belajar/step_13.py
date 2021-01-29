from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

import sys

def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,300,300) # set the window x,y,width,heigth
    win.setWindowTitle("My First PyQt App by Farid") # setting the window title

    label = QLabel(win)
    label.setText("Hello There!")
    label.move(50,50) # set x, y from top left hand corner
    
    b1 = QtWidgets.QPushButton(win) #declare button
    b1.setText("Send")
    b1.move(100,100) #move button position
    b1.clicked.connect(teken) #link the button and event fucntion

    win.show() #show the main window
    sys.exit(app.exec_()) #make sure we have clean exit

def teken():
    print("Oh hai :) ") #print string while the button cliked

main()