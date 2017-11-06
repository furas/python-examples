#!/usr/bin/env python3

from PyQt5 import QtWidgets
import sys

if __name__ == '__main__':

    # Linux Mint 18.3 problem with style (GTK2/GTK3) 
    # Error: "QApplication: invalid style override passed, ignoring it."
    sys.argv += ['-style', 'Fusion'] 
            
    app = QtWidgets.QApplication(sys.argv) #QApplication([]) #
    win = QtWidgets.QWidget()
    win.show()
    app.exec()
