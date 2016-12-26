#!/usr/bin/env python2

from PyQt4 import QtGui
import sys

class MyWindow(QtGui.QWidget):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__()
        
        self.clicks = 0

        self.vbox = QtGui.QVBoxLayout()
        self.setLayout(self.vbox)
        
        self.label = QtGui.QLabel(str(self.clicks), self)
        self.vbox.addWidget(self.label)
        
        self.button = QtGui.QPushButton("Click Me!", self)
        self.vbox.addWidget(self.button)
        self.button.clicked.connect(self.on_click)

        self.show()

    def on_click(self):
        self.clicks += 1
        self.label.setText(str(self.clicks))
            
app = QtGui.QApplication(sys.argv)
win = MyWindow()
app.exec_()
