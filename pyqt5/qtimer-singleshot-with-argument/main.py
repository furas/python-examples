#!/usr/bin/env python3

import sys
from PyQt5 import QtCore, QtWidgets


def num(i):
    print(i)
    
    i += 1
    
    if i < 10:
        # run again after 2000ms with argument
        QtCore.QTimer.singleShot(2000, lambda:num(i))

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    # run first time with start argument
    num(1)
    #or
    #QtCore.QTimer.singleShot(2000, lambda:num(1))

    app.exec()
