#!/usr/bin/env python

import sys
from PyQt4 import QtCore, QtGui


class MainWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.button = QtGui.QPushButton('Change')
        self.button.clicked.connect(self.change_widgets)

        self.widget1 = QtGui.QLabel('Widget1')
        self.widget2 = QtGui.QLabel('Widget2')
        self.widget3 = QtGui.QLabel('Widget3')
        
        self.widget2.hide()
        self.widget3.hide()

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.widget1)
        layout.addWidget(self.widget2)
        layout.addWidget(self.widget3)
        self.setLayout(layout)

        self.resize(640, 180)
        self.show()

    def change_widgets(self):
        if self.widget1.isHidden():
            self.widget1.show()
            self.widget2.hide()
            self.widget3.hide()
            self.resize(640, 180)
        else:
            self.widget1.hide()
            self.widget2.show()
            self.widget3.show()
            self.resize(640, 280)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    widget = MainWidget()
    sys.exit(app.exec_())
