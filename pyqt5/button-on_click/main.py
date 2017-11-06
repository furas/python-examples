#!/usr/bin/env python3

from PyQt5 import QtWidgets
import sys

class MyWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__()
        
        self.clicks = 0

        self.vbox = QtWidgets.QVBoxLayout()
        self.setLayout(self.vbox)
        
        self.label = QtWidgets.QLabel('Clicks: {}'.format(self.clicks), self)
        self.vbox.addWidget(self.label)
        
        self.button = QtWidgets.QPushButton("Click Me!", self)
        self.vbox.addWidget(self.button)
        
        self.button.clicked.connect(self.on_click)

        self.show()

    def on_click(self):
        self.clicks += 1
        self.label.setText('Clicks: {}'.format(self.clicks))

if __name__ == '__main__':            
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    app.exec()
