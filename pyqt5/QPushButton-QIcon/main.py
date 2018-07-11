#!/usr/bin/env python3

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class MyWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        
        #icon = QtGui.QIcon('1472610119960.jpg')
        icon = QtGui.QIcon('image.png')
        
        button = QtWidgets.QPushButton(self)
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(50, 50))
        
#        button.setMinimumSize(300, 300)
        button.clicked.connect(self.on_click)
        
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(button)

        self.setLayout(layout)

    def on_click(self, event):
        print('clicked')


if __name__ == '__main__':
    # Linux Mint 18.3 problem with style (GTK2/GTK3) 
    # "QApplication: invalid style override passed, ignoring it."
    sys.argv += ['-style', 'Fusion'] 
            
    app = QtWidgets.QApplication(sys.argv) #QApplication([]) #
    win = MyWindow()
    win.show()
    app.exec()
