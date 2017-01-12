#!/usr/bin/env python3

import sys
from PyQt4 import QtGui, QtCore

def num(i):
    print i
    i += 1
    if i < 10:
        # run again after 2000ms with argument
        QtCore.QTimer.singleShot(2000, lambda:num(i))

app = QtGui.QApplication(sys.argv)

# run first time with start argument
num(1)
#QtCore.QTimer.singleShot(2000, lambda:num(1))

sys.exit(app.exec_())
