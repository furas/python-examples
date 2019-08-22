
# date: 2019.08.20

import sys
import os
import PyQt4
from PyQt4 import QtGui

class MyWindow(QtGui.QWidget):

    def __init__(self):
        super().__init__()

        self.path = '' # default value at start (useful if you don't select new directory)
        
        #layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom) 
        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)

        btn_out_dir = QtGui.QPushButton("Select Directory", self)
        btn_out_dir.clicked.connect(self.select_directory)
        layout.addWidget(btn_out_dir)

        btn_confirm = QtGui.QPushButton("Exit", self)
        btn_confirm.clicked.connect(self.close)
        layout.addWidget(btn_confirm)

    def select_directory(self):
        self.path = QtGui.QFileDialog.getExistingDirectory()
        if self.path:
            print('[inside] path:', self.path)
        else:
            print('[inside] path: - not selected -')


app = QtGui.QApplication(sys.argv)

GUI = MyWindow()
GUI.show()

status_code = app.exec()
print('[outside] path:', GUI.path)

#sys.exit(status_code)

